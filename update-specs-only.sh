#!/bin/bash

OBSDIR=${HOME}/steelrat/OBS/qt5/
QT5_MODULES="qtbase qtxmlpatterns qtscript qtdeclarative qtsystems qtsvg
qtmultimedia qtsensors qtlocation qtphonon"

for m in ${QT5_MODULES}; do
    cp ${m}/*.spec ${OBSDIR}/${m}/
    cp ${m}/files/* ${OBSDIR}/${m}/
    # Errors shown here, not in main script
    osc add ${OBSDIR}/${m}/*
done

(cd ${OBSDIR}; osc commit -m 'Update specs' ${QT5_MODULES})


