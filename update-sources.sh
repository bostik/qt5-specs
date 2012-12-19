#!/bin/bash

# Force flags
NO_PULL=1
#FORCE_UPLOAD=1

# update-sources.sh
# Modular Qt Build Manager

# marko.helenius@nomovok.com 2012-03-26

# Original Source by Bostik, hooray!


#   ______ _______ _______ _______ __
#  |   __ \_     _|    ___|   |   |  |
#  |      < |   | |    ___|       |__|
#  |___|__| |___| |___|   |__|_|__|__|
#   update-sources.sh --help

while [ $# -gt 0 ]
do
    case "$1" in
        --help)  cat <<XXX
Modulas Qt Build Manager (update-sources.sh)

Usage:	update-sources.sh [<options>]

     Update parameter:
        [--pull             ] Force git source pull.
        [--no-pull	        ] Prevent git source pull. (default)
        [--force-upload	    ] Force source tar upload.

        [--module MODULE    ] List of modules.
        [--beta             ] Pull latest beta release.
        [--release          ] Pull latest release/candidate
        [--tag TAG          ] Pull a certain tag release.

XXX
exit ;;
        --pull) NO_PULL="0";;
        --no-pull) NO_PULL="1";;
        --force-upload) FORCE_UPLOAD="1";;
        --beta) GIT_TAG="v5.0.0-beta2";;
        --release) GIT_TAG="v5.0.0-rc2";;
        --tag) GIT_TAG="$2"; shift;;
        --module) QT5_MODULES="$2"; shift;;

	*) break;;
    esac
    shift
done


# QT5_DIR is the directory where qt5 and all the submodules have been
# checked into
if [ x${QT5_DIR} = x ]; then
    QT5_DIR=/work/qt/qt5
fi

# OBSDIR is the directory holding your OBS qt5 project
if [ x${OBSDIR} = x ]; then
    OBSDIR=/work/qt/obs/qt5
fi

# Modules to build, in order
#QT5_MODULES="qtbase qtjsbackend qtxmlpatterns qtscript qtdeclarative \
#qttools qtsystems qtsvg qtsensors qtlocation qtmultimedia qtwayland  \
#qt3d qtquick1 qtimageformats qtgraphicaleffects qtwebkit"
####
# XXX: Qt 5.0 RC1 has left some of the modules out, and thus not all
# modules have the tag. Build only those modules where tag is available.
QT5_MODULES="qtbase qtjsbackend qtxmlpatterns qtscript qtdeclarative \
qttools qtsvg qtmultimedia \
qtimageformats qtgraphicaleffects qtwebkit"

# WARNING! WARNING! WARNING!
# Force upload of all sources
# XXX: Use only if you want to force regeneration of ALL tarballs
if [ "x${FORCE_UPLOAD}" = "x1" ]; then
    rm -f ${HOME}/.modular-qt5-revs/* >/dev/null 2>&1
fi

# Do we have a valid OBS project defined?
if [ ! -d ${OBSDIR} ]; then
    for dir in ${QT5_MODULES}; do
        if [ ! -d ${OBSDIR}/$dir/.osc ]; then
            echo ERROR: ${OBSDIR} does not contain a valid OBS project
            echo ERROR: module $dir is not tracked
        fi
    done
fi

# Helper routines to manage archive tarballs
function get_last() {
    local _mod=$1

    if [ -d ${HOME}/.modular-qt5-revs ]; then
        if [ -e ${HOME}/.modular-qt5-revs/${_mod} ]; then
            cat ${HOME}/.modular-qt5-revs/${_mod}
        else
            echo "none"
        fi
    else
        echo "none"
    fi
}

function put_last() {
    local _mod=$1 _rev=$2

    if [ ! -d ${HOME}/.modular-qt5-revs ]; then
        mkdir ${HOME}/.modular-qt5-revs
    fi
    echo ${_rev} > ${HOME}/.modular-qt5-revs/${_mod}
}

function update_changelog() {
    local _mod=$1 _rev=$2

    pkg_version="5~git${_rev}"
    tmpfile=$(mktemp --tmpdir ${m}.changes.XXXXXX)
    datestr=$(LC_TIME=C date '+%a %b %e %Y')

    # QtWebkit has a trailing '5' in the filenames
    if [ ${_mod} = "qtwebkit" ]; then
        _trail="5"
    fi

    # generate header line
    echo "* ${datestr} ${GIT_AUTHOR_NAME} <${GIT_AUTHOR_EMAIL}> - ${pkg_version}" > ${tmpfile}

    # Add automatic entry
    echo "- Automated source update" >> ${tmpfile}
    echo "" >> ${tmpfile}

    # Add the rest of the changelog
    # XXX: we're in QT5_DIR, not in module
    cat ${_mod}/${_mod}${_trail}.changes >> ${tmpfile}

    # And copy over
    cp -v ${tmpfile} ${_mod}/${_mod}${_trail}.changes

    # Clean up...
    rm -f ${tmpfile}
}



# GIT_DIR has been set when this function is called
function get_version() {
    local _ref=$1
    if ! git describe >/dev/null 2>&1; then
        count=$(git rev-list ${_ref} | wc -l)
        realcommitid=$(git describe --always ${_ref})
        commitid=$count.g$realcommitid
    else
        # While using tags, git describe returns the tag name
        if [ x${GIT_TAG} = x ]; then
            commitid=$(expr match $(git describe ${_ref}) '.*-\([0-9]*-g[a-z0-9]*\)$' \
                     | tr - .)
        else
            commitid=$(git describe --always ${_ref} \
	             | sed 's/^\(.*\)-v\(.*\)\(-.*\)$/\2\3/' | tr - '~' )
        fi
    fi
    echo $commitid
}

# Update OBS project
(cd ${OBSDIR}; osc ${OSC_OPTS} update)

# Update Qt sources
if [ x${NO_PULL} != "x1" ]; then
    # qt5.git now works as a nice umbrella repository; a pull in
    # top-level repo cascades into a nice set of "pull and checkout
    # last known good revision for each module" operations.
    #
    # So, we pull everything and use submodules as they are
    if [ x${GIT_TAG} = x ]; then
        _tgtref="master"
    else
        _tgtref=${GIT_TAG}
    fi
    #
    (cd ${QT5_DIR}; git checkout master; git pull; git checkout ${_tgtref}; git submodule update --recursive)
fi


# Update source tarballs, patches, specs
for m in ${QT5_MODULES}; do
    # Ensure the target OBS directory exists
    if [ ! -d ${OBSDIR}/${m} ]; then
        mkdir ${OBSDIR}/${m}
        osc add ${OBSDIR}/${m}
    fi
    # Git ref to archive.
    if [ x${GIT_TAG} = x ]; then
        # Commit set by pull/submodule-update
        _gitref="HEAD"
    else
        _gitref="${GIT_TAG}"
    fi
    bn="qt5-${m}"
    export GIT_DIR=${QT5_DIR}/${m}/.git
    last=$(get_last ${m})
    head=$(git show ${_gitref} | grep ^commit | sed s'/^commit //')
    ver=$(get_version ${_gitref})
    if [ "${head}" != "${last}" ]; then
        # New revision. Remove old sources before recreating new.
        rm -fv ${OBSDIR}/${m}/${bn}*.tar.gz
        git archive ${_gitref} --prefix=${bn}/ | gzip > ${OBSDIR}/${m}/${bn}-5~${ver}.tar.gz
        # Store the revision used
        put_last ${m} ${head}
        # Add this version to changelog
        update_changelog ${m} ${ver}
    fi

    # Remove all (leftover) patch files from target dir.
    # The current ones will be copied over; this way there will be no
    # more crud patches in the build system.
    rm -f ${OBSDIR}/${m}/*.patch

    # Spec, changelog, rpmlintrc, patches, extra files,
    # all from this directory
    cp -v ${m}/*.spec ${m}/*.changes ${OBSDIR}/${m}/
    if [ -d ${m}/files ]; then
        cp -v ${m}/files/* ${OBSDIR}/${m}/
    fi

    # Uses retrieved source version from beginning of loop
    sed -i "s/define _qtmodule_snapshot_version %nil/define _qtmodule_snapshot_version 5~${ver}/g" ${OBSDIR}/${m}/*.spec

    # Deals with OBS package dir bookkeeping in one go
    (cd ${OBSDIR}/${m}/ && osc addremove)
done

# And finally commit all the modules at once
(cd ${OBSDIR}; osc ${OSC_OPTS} commit -m 'Updated to latest sources' ${QT5_MODULES})

# Show local changes, allow to clean if needed
echo ""
echo "Running git-status..."
unset GIT_DIR; git status

echo "Execute 'git reset --hard HEAD' to clear any changes"
