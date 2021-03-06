#!/bin/bash
python UWVV/Ntuplizer/test/ntuplize_cfg.py \
    inputFiles=/store/mc/RunIISummer16MiniAODv2/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0018B491-F0C3-E611-B568-D8D385AF882A.root \
    outputFile=testMC.root \
    channels=wz \
    isMC=1 \
    eCalib=1 \
    muCalib=1 \
    globalTag=80X_mcRun2_asymptotic_2016_TrancheIV_v7 \
    $1
