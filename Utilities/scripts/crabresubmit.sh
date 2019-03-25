#!/bin/bash
Date=16Aug2018

echo "Resubmitting failed crab jobs"

source /cvmfs/cms.cern.ch/crab3/crab.sh

listOfSamples="DoubleEG DoubleMuon MuonEG SingleElectron SingleMuon"
eras="B C D E F"

for name in $listOfSamples; do
  for era in $eras; do
    echo "=====================" $name "========================"
    crab resubmit --dir=crab_UWVVNtuples_${Date}_${name}_Run2017${era}-17Nov2017-v1 
  done
done
