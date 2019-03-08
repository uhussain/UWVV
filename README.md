# UWVV
Some tools for CMS analyses

UWVV is designed for analyses that use final state particles (typically leptons) to reconstruct intermediate and initial states. For example, in the H->ZZ->4l analysis, electron and muon pairs are built into Z candidates, and the Z candidates are built into Higgs candidates. It contains tools for building a full analysis flow out of CMS EDM modules, and for making flat ntuples where each row represents one initial state candidate.

It uses the [CMSSW framework](https://github.com/cms-sw/cmssw) and expects [miniAOD](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2017) input. Much of the inspiration (and a little bit of the code) comes from [FSA](https://github.com/uwcms/FinalStateAnalysis/). A few tools, like the batch submission scripts, are specific to the computing infrastructure at the University of Wisconsin - Madison.

## Setup
Current supported CMSSW release: `CMSSW_10_2_0+`

```bash
scram pro -n uwvv CMSSW CMSSW_10_2_10
cd uwvv/src
cmsenv
git cms-init
git clone -b 2018Data --recursive git@github.com:uhussain/UWVV.git
cd UWVV
source recipe/setup.sh
pushd ..
(To avoid compilation errors although we don’t need this anymore in 2017/2018: https://github.com/CJLST/ZZAnalysis/blob/miniAOD_80X/checkout_10X.csh#L89)
git clone https://github.com/bachtis/Analysis.git -b KaMuCa_V4 KaMuCa
scram b -j 12
cd UWVV/Ntuplizer/test/
cmsRun ntuplize_cfg.py channels=zz isMC=0 eCalib=0 muCalib=1 RecomputeElectronID=0
```
## Use
To make a basic ntuple of four-lepton final state candidates, do

```bash
cmsRun ntuplize_cfg.py channels=zz isMC=0 eCalib=0 muCalib=1 RecomputeElectronID=0
```

For more on how to build your own analysis, see the `AnalysisTools` directory. For more on making ntuples, see the `Ntuplizer` directory.

For submitting jobs using crab, see the `Utilities` directory.
```bash
./crabSubmit.sh /data/uhussain/ZZTo4l/ZZ2018/uwvv/src/UWVV/MetaData/ZZDatasets/ZZ2018Data_MiniAOD.dat | grep "ZZ" | . /dev/stdin
```
