#!/bin/bash
Date=24Sep2018

echo "Copy processedLumis.json "

listOfSamples="DoubleEG DoubleMuon MuonEG SingleElectron SingleMuon"
eras="B C D E F"

rm -rf ZplusL_Lumis_${Date} 
mkdir -p ZplusL_Lumis_${Date}
cd ZplusL_Lumis_${Date}

for name in $listOfSamples; do
  for era in $eras; do
    echo "=====================" $name "========================"
    cp ../crab_UWVVNtuples_${Date}_${name}_Run2017${era}-17Nov2017-v1/results/processedLumis.json ProcessedLumis_${name}${era}.json
  done
done

ls
echo "Merging all the processedLumis.json files into one"

mergeJSON.py ProcessedLumis*.json --output=TotalProcessedLumis.json
#mkdir -p /afs/cern.ch/user/u/uhussain/ZZ4l2017Lumis/Lumis_${Date}
cp TotalProcessedLumis.json /afs/cern.ch/user/u/uhussain/ZplusL2017Lumis/
