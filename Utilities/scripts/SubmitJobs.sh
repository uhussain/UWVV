#echo "Submitting 2018 Data Jobs"
#./crabSubmit.sh /data/uhussain/ZZTo4l/ZZ2019/Moriond19/uwvv/src/UWVV/MetaData/ZZDatasets/ZZ2018Data_MiniAOD.dat | grep "ZZ" |. /dev/stdin
# 
#echo "Submitting 2018 Signal Jobs"
#./crabSubmit.sh /data/uhussain/ZZTo4l/ZZ2019/Moriond19/uwvv/src/UWVV/MetaData/ZZDatasets/ZZ2018_SignalMonteCarlo.dat | grep "ZZ" |. /dev/stdin
#
#echo "Submitting 2018 Background Jobs"
#./crabSubmit.sh /data/uhussain/ZZTo4l/ZZ2019/Moriond19/uwvv/src/UWVV/MetaData/ZZDatasets/ZZ2018_BackgroundMonteCarlo.dat | grep "ZZ" |. /dev/stdin

echo "Submit leftover jobs without auto splitting"
./crabSubmit.sh /data/uhussain/ZZTo4l/ZZ2019/Moriond19/uwvv/src/UWVV/MetaData/ZZDatasets/ZZ2018_Leftover.dat | grep "ZZ" |. /dev/stdin
