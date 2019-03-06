#!/bin/bash
Date=13Feb2019

echo "Copy processedLumis.json "

listOfSamples="DoubleEG DoubleMuon MuonEG SingleElectron SingleMuon"
eras="B C D E F"

#rm -rf Lumis_${Date}
#mkdir -p Lumis_${Date}
cd Lumis_${Date}

#for name in $listOfSamples; do
#  for era in $eras; do
#    echo "=====================" $name "========================"
#    cp ../crab_UWVVNtuples_${Date}_${name}_Run2017${era}-31Mar2018-v1/results/processedLumis.json ProcessedLumis_${name}${era}.json
#  done
#done

ls
echo "Merging all the processedLumis.json files into one"

#mergeJSON.py ProcessedLumis*.json --output=ProcessedLumis.json
#mkdir -p /afs/cern.ch/user/u/uhussain/ZZ4l2017Lumis/Lumis_${Date}
cp ProcessedLumis.json /afs/cern.ch/user/u/uhussain/ZZ4l2017Lumis/Lumis_${Date}/
