#!/bin/bash
Date=15Aug2018

echo "Checking status of crab jobs"

source /cvmfs/cms.cern.ch/crab3/crab.sh

listOfSamples="EGamma DoubleMuon MuonEG SingleMuon"
eras="A B C"
versions="v1 v2 v3"
for name in $listOfSamples; do
  for era in $eras; do
    for ver in $versions;do
      echo "=====================" $name "========================"
      crab report --dir=crab_UWVVNtuples_${Date}_${name}_Run2018${era}-PromptReco-${ver}
    done
  done
done
