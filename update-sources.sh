#!/bin/bash

# QT5_DIR is the directory where qt5 and all the submodules have been
# checked into
if [ x${QT5_DIR} = x ]; then
    QT5_DIR=${HOME}/kala/qt5
fi

# OBSDIR is the directory holding your OBS qt5 project
if [ x${OBSDIR} = x ]; then
    OBSDIR=${HOME}/steelrat/OBS/qt5/
fi

# Modules to build, in order
QT5_MODULES="qtbase qtxmlpatterns qtscript qtdeclarative qttools qtsystems qtsvg qtsensors qtlocation qtphonon qtmultimedia qtquick3d qtwayland"


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
    if ! git describe >/dev/null 2>&1; then
        count=$(git rev-list origin/HEAD | wc -l)
        realcommitid=$(git describe --always)
        commitid=$count.g$realcommitid
    else
        commitid=$(expr match $(git describe) '.*-\([0-9]*-g[a-z0-9]*\)$' \
                | tr - .)
    fi
    echo $commitid
}

# Update OBS project
(cd ${OBSDIR}; osc update)

# Update Qt sources
if [ x${NO_PULL} = x ]; then

    # Starting from week 29, qt5_tool will try to pull from
    # codereview.qt.nokia.com; however, that host is not yet public and
    # all pulls fail.
    # XXX: comment use of qt5_tool for now
    #(cd ${QT5_DIR}; git pull; ./qtrepotools/bin/qt5_tool -p)

    # Instead, use mirror repos at gitorious.org
    for m in ${QT5_MODULES}; do
        (cd ${QT5_DIR}/${m}/; echo "[### ${m}]"; git checkout master; git pull)
        # In case of declarative module, sync v8 submodule
        if [ ${m} = "qtbase" ]; then
            (cd ${QT5_DIR}/${m}; git submodule update)
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
    bn="qt5-${m}"
    export GIT_DIR=${QT5_DIR}/${m}/.git
    last=$(get_last ${m})
    head=$(git show origin/HEAD | head -n 1 | sed s'/^commit //')
    ver=$(get_version)
    if [ "${head}" != "${last}" ]; then
        # New revision. Remove old sources before recreating new.
        rm -fv ${OBSDIR}/${m}/${bn}*.tar.gz
        git archive origin/HEAD --prefix=${bn}/ | gzip > ${OBSDIR}/${m}/${bn}-5~git${ver}.tar.gz
        # Store the revision used
        put_last ${m} ${head}
        # Add this version to changelog
        update_changelog ${m} ${ver}
    fi
    # QtBase needs v8 sources.
    # Treat v8 source tarball individually; this way we will always have
    # v8id to use in spec-file mangling.
    if [ ${m} = "qtbase" ]; then
        export GIT_DIR=${QT5_DIR}/${m}/src/3rdparty/v8/.git
        v8id=$(git describe --always)
        v8old=$(get_last v8)
        if [ "${v8id}" != ${v8old} ]; then
            # Treat v8 the same way
            rm -fv ${OBSDIR}/${m}/v8-git*.tar.gz
            git archive HEAD --prefix=v8/ | gzip > ${OBSDIR}/${m}/v8-git${v8id}.tar.gz
            put_last v8 ${v8id}
        fi
    fi
    
    # Spec, changelog, rpmlintrc, patches, extra files,
    # all from this directory
    cp -v ${m}/*.spec ${m}/*.changes ${OBSDIR}/${m}/
    if [ -d ${m}/files ]; then
        cp -v ${m}/files/* ${OBSDIR}/${m}/
    fi

    # Uses retrieved source version from beginning of loop
    sed -i "s/define _qtmodule_snapshot_version %nil/define _qtmodule_snapshot_version 5~git${ver}/g" ${OBSDIR}/${m}/*.spec
    if [ ${m} = "qtbase" ]; then
        sed -i "s/define _v8_snapshot_version %nil/define _v8_snapshot_version git${v8id}/g" ${OBSDIR}/${m}/*.spec
    fi

    # Deals with OBS package dir bookkeeping in one go
    (cd ${OBSDIR}/${m}/ && osc addremove)
done

# And finally commit all the modules at once
(cd ${OBSDIR}; osc commit -m 'Updated to latest sources' ${QT5_MODULES})

# Show local changes, allow to clean if needed
echo ""
echo "Running git-status..."
unset GIT_DIR; git status

echo "Execute 'git reset --hard HEAD' to clear any changes"
