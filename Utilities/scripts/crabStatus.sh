#!/bin/bash
Date=13Feb2019

echo "Checking status of crab jobs"

source /cvmfs/cms.cern.ch/crab3/crab.sh

listOfSamples="DoubleEG DoubleMuon MuonEG SingleElectron SingleMuon"
eras="B C D E F"

for name in $listOfSamples; do
  for era in $eras; do
    echo "=====================" $name "========================"
    crab report --dir=crab_UWVVNtuples_${Date}_${name}_Run2017${era}-31Mar2018-v1
  done
done
