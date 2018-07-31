#!/bin/bash
Date=31Jul2018

echo "Checking status of crab jobs"

source /cvmfs/cms.cern.ch/crab3/crab.sh

listOfSamples="EGamma DoubleMuon MuonEG SingleElectron SingleMuon"
eras="A B C"
versions="v1 v2 v3"
for name in $listOfSamples; do
  for era in $eras; do
    for ver in $versions;do
      echo "=====================" $name "========================"
      crab status --dir=crab_UWVVNtuples_${Date}_${name}_Run2018${era}-PromptReco-${ver}
    done
  done
done
