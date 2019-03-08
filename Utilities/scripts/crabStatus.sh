#!/bin/bash
Date=25Jan2019

echo "Checking status of crab jobs"

source /cvmfs/cms.cern.ch/crab3/crab.sh

listOfSamples="EGamma DoubleMuon MuonEG SingleMuon"
eras="A B C"
prompteras="D"
versions="v1 v2"
for name in $listOfSamples; do
  for era in $prompteras; do
    for ver in $versions;do
      echo "=====================" $name "========================"
      crab report --dir=crab_UWVVNtuples_${Date}_${name}_Run2018${era}-PromptReco-${ver}
    done
  done
  for era in $eras; do
    for ver in $versions; do
      crab report --dir=crab_UWVVNtuples_${Date}_${name}_Run2018${era}-17Sep2018-${ver}
    done
  done
done
