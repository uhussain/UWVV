#!/bin/bash
echo "Find Events in Datasets"

listOfSamples="DoubleEG DoubleMuon MuonEG SingleElectron SingleMuon"
eras="B C D E F"

echo "Find Events - 302597:190:173426597,306138:1172:1521943340,306125:23:38840909,305377:553:997883474"
for name in $listOfSamples; do
  for era in $eras; do
    echo "=====================" $name "========================"
    edmPickEvents.py /${name}/Run2017${era}-17Nov2017-v1/MINIAOD 302597:190:173426597 306138:1172:1521943340 306125:23:38840909 305377:553:997883474
  done
done
