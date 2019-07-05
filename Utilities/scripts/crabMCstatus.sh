#!/bin/bash
Date=09Mar2019

echo "Status of ZZ4l 2018 Signal crab jobs"

source /cvmfs/cms.cern.ch/crab3/crab.sh


for dir in */ ; do
    if [[ $dir = *"$Date"* ]]; then
    echo "=====================" $dir "========================"
    crab status --dir=$dir
    fi
done
