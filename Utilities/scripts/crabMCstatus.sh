#!/bin/bash
Date=25Jan2019

echo "Status of ZZ4l 2018 Signal crab jobs"

source /cvmfs/cms.cern.ch/crab3/crab.sh


for dir in */ ; do
    if [[ $dir = *"$Date"* ]]; then
    echo "=====================" $dir "========================"
    crab resubmit --dir=$dir
    fi
done
