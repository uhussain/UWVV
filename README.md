# UWVV
Some tools for CMS analyses

UWVV is designed for analyses that use final state particles (typically leptons) to reconstruct intermediate and initial states. For example, in the H->ZZ->4l analysis, electron and muon pairs are built into Z candidates, and the Z candidates are built into Higgs candidates. It contains tools for building a full analysis flow out of CMS EDM modules, and for making flat ntuples where each row represents one initial state candidate.

It uses the [CMSSW framework](https://github.com/cms-sw/cmssw) and expects [miniAOD](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2017) input. Much of the inspiration (and a little bit of the code) comes from [FSA](https://github.com/uwcms/FinalStateAnalysis/). A few tools, like the batch submission scripts, are specific to the computing infrastructure at the University of Wisconsin - Madison.

## Setup
Current supported CMSSW release: `CMSSW_9_4_0+`
_As of right now (28/11/2017), triggers and MET/bad muon filters are turned off on this branch, and it has not been tested on Monte Carlo (because appropriate files are not yet available). It has been tested only minimally on 2017 data, so use with caution._


```bash
scram pro -n uwvv CMSSW_9_4_10
cd uwvv/src
cmsenv
git cms-init # do before anything else
git clone -b 9_4_X_dev --recursive git@github.com:uhussain/UWVV.git
cd UWVV
source recipe/setup.sh # install necessary packages
pushd ..
scram b -j 8 # compile
popd
```
Several fragile dependencies that are used in only some analyses are included only if the `--hzzExtras` or `--met` options are used with `setup.sh`. Modules that depend on the optional packages are saved in `.txt` files which are copied to `.cc` files.

## Use
To make a basic ntuple of four-lepton final state candidates, do

```bash
cmsRun Ntuplizer/test/ntuplize_cfg.py channels='zz' isMC=1 inputFiles=file:aNiceMonteCarloFile.root
```

For more on how to build your own analysis, see the `AnalysisTools` directory. For more on making ntuples, see the `Ntuplizer` directory.
