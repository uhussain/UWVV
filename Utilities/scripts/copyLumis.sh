#!/bin/bash
Date=25Apr2018

echo "Copy processedLumis.json "

listOfSamples="DoubleEG DoubleMuon MuonEG SingleElectron SingleMuon"
eras="B C D E F"

#rm -rf Lumis_${Date}
#mkdir -p Lumis_${Date}
cd Lumis_${Date}

for name in $listOfSamples; do
  for era in $eras; do
    echo "=====================" $name "========================"
    cp ../crab_UWVVNtuples_${Date}_${name}_Run2017${era}-17Nov2017-v1/results/lumisToProcess.json LumisToProcess_${name}${era}.json
  done
done

ls
echo "Merging all the processedLumis.json files into one"

mergeJSON.py LumisToProcess*.json --output=TotalLumisToProcess.json
#mkdir -p /afs/cern.ch/user/u/uhussain/ZZ4l2017Lumis/Lumis_${Date}
cp TotalLumisToProcess.json /afs/cern.ch/user/u/uhussain/ZZ4l2017Lumis/Lumis_${Date}/
