#!/bin/bash
Date=24Sep2018

echo "Resubmitting failed crab jobs"

source /cvmfs/cms.cern.ch/crab3/crab.sh


for dir in */ ; do
    if [[ $dir = *"$Date"* ]]; then
    echo "=====================" $dir "========================"
    crab resubmit --dir=$dir 
    fi
done
