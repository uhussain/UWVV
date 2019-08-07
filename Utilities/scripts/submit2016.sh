source /cvmfs/cms.cern.ch/crab3/crab.sh

./crabSubmit.sh /data/uhussain/ZZTo4l/FullRun2/uwvv/src/UWVV/MetaData/ZZDatasets/ZZ2016_SignalMonteCarlo.dat 2016 | grep "ZZ" | . /dev/stdin

./crabSubmit.sh /data/uhussain/ZZTo4l/FullRun2/uwvv/src/UWVV/MetaData/ZZDatasets/ZZ2016Data_MiniAOD.dat 2016 | grep "ZZ" | . /dev/stdin

./crabSubmit.sh /data/uhussain/ZZTo4l/FullRun2/uwvv/src/UWVV/MetaData/ZZDatasets/ZZ2016_BackgroundMonteCarlo.dat 2016 | grep "ZZ" | . /dev/stdin
