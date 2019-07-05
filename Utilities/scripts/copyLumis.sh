#!/bin/bash
Date=09Mar2019

echo "Copy processedLumis.json "

listOfSamples="EGamma DoubleMuon MuonEG SingleMuon"
eras="A B C"
ver="v1 v2"
#rm -rf Lumis_${Date}
mkdir -p Lumis_${Date}
cd Lumis_${Date}

for name in $listOfSamples; do
  for era in $eras; do
    for v in $ver; do
      echo "=====================" $name "========================"
      #crab report --dir=crab_UWVVNtuples_${Date}_${name}_Run2018${era}-17Sep2018-${v}
      cp ../crab_UWVVNtuples_${Date}_${name}_Run2018${era}-17Sep2018-${v}/results/processedLumis.json ProcessedLumis_${name}${era}.json
    done
  done
done

for name in $listOfSamples; do
  echo "=====================" $name "========================"
  #crab report --dir=crab_UWVVNtuples_${Date}_${name}_Run2018${era}-17Sep2018-${v}
  cp ../crab_UWVVNtuples_${Date}_${name}_Run2018D-PromptReco-v2/results/processedLumis.json ProcessedLumis_${name}D.json
done

ls
echo "Merging all the processedLumis.json files into one"

mergeJSON.py ProcessedLumis*.json --output=TotalProcessedLumis_${Date}.json
#mkdir -p /afs/cern.ch/user/u/uhussain/ZZ4l2017Lumis/Lumis_${Date}
cp TotalProcessedLumis_${Date}.json /afs/cern.ch/user/u/uhussain/ZZ4l2018Lumis/Lumis_${Date}/
