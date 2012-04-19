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
        [--pull               ] Force git source pull.
        [--no-pull	      ]	Prevent git source pull. (default)
        [--force-upload	      ]	Force source tar upload.
	
        [--module MODULE      ] List of modules.
        [--alpha              ] Pull latest alpha release.
        [--tag TAG            ] Pull a certain tag release.

XXX
exit ;;
        --pull) NO_PULL="0";;
        --no-pull) NO_PULL="1";;
        --force-upload) FORCE_UPLOAD="1";;
        --alpha) GIT_TAG="qt-v5.0.0-alpha1";;
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
QT5_MODULES="qtbase qtjsbackend qtxmlpatterns qtscript qtdeclarative qttools qtsystems qtsvg qtsensors qtlocation qtmultimedia qtwayland qt3d qtquick1"

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

    # generate header line
    echo "* ${datestr} ${GIT_AUTHOR_NAME} <${GIT_AUTHOR_EMAIL}> - ${pkg_version}" > ${tmpfile}

    # Add automatic entry
    echo "- Automated source update" >> ${tmpfile}
    echo "" >> ${tmpfile}

    # Add the rest of the changelog
    # XXX: we're in QT5_DIR, not in module
    cat ${_mod}/${_mod}.changes >> ${tmpfile}

    # And copy over
    cp -v ${tmpfile} ${_mod}/${_mod}.changes

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

    # Starting from week 29, qt5_tool will try to pull from
    # codereview.qt.nokia.com; however, that host is not yet public and
    # all pulls fail.
    # XXX: comment use of qt5_tool for now
    #(cd ${QT5_DIR}; git pull; ./qtrepotools/bin/qt5_tool -p)

    # Instead, use mirror repos at gitorious.org
    for m in ${QT5_MODULES}; do
    
        # Handling a case where Git Tag is present
        if [ x${GIT_TAG} = x ]; then
            (cd ${QT5_DIR}/${m}/; echo "[### ${m}]"; git checkout master; git pull)
        else
            (cd ${QT5_DIR}/${m}/; echo "[### ${m} - Tag: ${GIT_TAG}]"; git checkout ${GIT_TAG})            
        fi
    done
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
        _gitref="origin/HEAD"
    else
        _gitref="refs/tags/${GIT_TAG}"
    fi
    bn="qt5-${m}"
    export GIT_DIR=${QT5_DIR}/${m}/.git
    last=$(get_last ${m})
    head=$(git show ${_gitref} | head -n 1 | sed s'/^commit //')
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
