#!/bin/bash
Date=06Mar2019

echo "Status of ZZ4l MC crab jobs"

source /cvmfs/cms.cern.ch/crab3/crab.sh


for dir in */ ; do
    if [[ $dir = *"$Date"* ]]; then
    echo "=====================" $dir "========================"
    crab status --dir=$dir
    fi
done
