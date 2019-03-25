#!/bin/bash
Date=16Aug2018

echo "merge processedLumis.json"

mkdir ProcessedLumis_${Date}

listOfSamples="DoubleEG DoubleMuon MuonEG SingleElectron SingleMuon"
eras="B C D E F"

for name in $listOfSamples; do
  for era in $eras; do
    echo "=====================" $name "========================"
    cp crab_UWVVNtuples_${Date}_${name}_Run2017${era}-17Nov2017-v1/results/processedLumis.json ProcessedLumis_${Date}/${name}_${era}.json
  done
done

#mergeJSON.py ProcessedLumis/*.json --output=totalProcessed.json
