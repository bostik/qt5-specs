#!/bin/bash

# QT5_DIR is the directory where qt5 and all the submodules have been
# checked into
QT5_DIR=${HOME}/kala/qt5

# OBSDIR is the directory holding your OBS qt5 project
OBSDIR=${HOME}/steelrat/OBS/qt5/

# Modules to build, in order
QT5_MODULES="qtbase qtxmlpatterns qtscript qtdeclarative qtsystems qtsvg qtmultimedia qtsensors qtlocation qtphonon"

# Do we have a valid OBS project defined?
if [ ! -d ${OBSDIR} ]; then
    for dir in ${QT5_MODULES}; do
        if [ ! -d ${OBSDIR}/$dir/.osc ]; then
            echo ERROR: ${OBSDIR} does not contain a valid OBS project
            echo ERROR: module $dir is not tracked
        fi
    done
fi

# Update OBS project
(cd ${OBSDIR}; osc update)

# Update Qt sources
(cd ${QT5_DIR}; git pull; ./qtrepotools/bin/qt5_tool -p)


# Update source tarballs, patches, specs
# FIXME: tarballs only if latest source has changed
for m in ${QT5_MODULES}; do
    # XXX: bashism
    bn="qt5-${m:2}"
    GIT_DIR=${QT5_DIR}/${m}/.git git archive master --prefix=${bn}/ | gzip > ${OBSDIR}/${m}/${bn}.tar.gz
    
    # Spec, rpmlintrc, patches, extra files,
    # all from this directory
    cp ${m}/*.spec ${OBSDIR}/${m}/
    if [ -d ${m}/files ]; then
        cp ${m}/files/* ${OBSDIR}/${m}/
    fi
done

# And finally commit all the modules at once
(cd ${OBSDIR}; osc commit -m 'Updated to latest sources' ${QT5_MODULES})

