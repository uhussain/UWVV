#!/bin/bash
Date=09May2019

echo "Status of ZZ4l crab jobs"

source /cvmfs/cms.cern.ch/crab3/crab.sh

#crab resubmit --dir=crab_UWVVNtuples_26Feb2019_SingleMuon_Run2017F-31Mar2018-v1 --siteblacklist=T2_TR_METU,T2_US_Caltech
#crab resubmit --dir=crab_UWVVNtuples_19Feb2019_SingleMuon_Run2017C-31Mar2018-v1 --siteblacklist=T2_BE_IIHE,T2_US_UCSD,T2_US_Caltech
#crab resubmit --dir=crab_UWVVNtuples_13Feb2019_SingleElectron_Run2017C-31Mar2018-v1 --siteblacklist=T2_BE_IIHE,T2_US_UCSD,T2_US_Caltech
for dir in */ ; do
    if [[ $dir = *"$Date"* ]]; then
    echo "=====================" $dir "========================"
    #crab resubmit --dir=$dir --siteblacklist=T2_US_UCSD,T2_US_Caltech --maxjobruntime=400
    crab status --dir=$dir
    fi
done
