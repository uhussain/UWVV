#!/bin/bash
Date=25Jan2019
echo "merge processedLumis.json"

mkdir ProcessedLumis_${Date}
listOfSamples="EGamma DoubleMuon MuonEG SingleMuon"
eras="A B C"
prompteras="D"
versions="v1 v2"
for name in $listOfSamples; do
  for era in $prompteras; do
    for ver in $versions;do
      echo "=====================" $name "========================"
      cp crab_UWVVNtuples_${Date}_${name}_Run2018${era}-PromptReco-${ver}/results/processedLumis.json ProcessedLumis_${Date}/${name}_${era}_${ver}.json
    done
  done
  for era in $eras; do
    for ver in $versions; do
      cp crab_UWVVNtuples_${Date}_${name}_Run2018${era}-17Sep2018-${ver}/results/processedLumis.json ProcessedLumis_${Date}/${name}_${era}_${ver}.json
    done
  done
done
#mergeJSON.py ProcessedLumis/*.json --output=totalProcessed.json
