import FWCore.ParameterSet.Config as cms

triggerBranches_2016 = cms.PSet(
    trigNames = cms.vstring(
         "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",#2016diEle
         "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",#2016diEle
         "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL",#2016diEle
         "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",#2016diMu
         "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",#2016diMu
         "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL",#2016diMu
         "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",#2016diMu
         "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL",#2016MuEle
         "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",#2016MuEle
         "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",#2016MuEle
         "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",#2016MuEle
         "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",#2016MuEle
         "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",#2016MuEle
         "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL",#2016MuEle
         "HLT_Mu8_DiEle12_CaloIdL_TrackIdL",#2016MuEle
         "HLT_DiMu9_Ele9_CaloIdL_TrackIdL",#2016MuEle
         "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL",#2016triEle
         "HLT_TripleMu_12_10_5",#2016triMu
         "HLT_Ele25_eta2p1_WPTight_Gsf",#2016SingleEle
         "HLT_Ele27_WPTight_Gsf",#2016SingleEle
         "HLT_Ele27_eta2p1_WPLoose_Gsf",#2016SingleEle
         "HLT_Ele32_eta2p1_WPTight_Gsf",#2016SingleEle
         "HLT_IsoMu20",#2016SingleMu
         "HLT_IsoTkMu20",#2016SingleMu
         "HLT_IsoMu22",#2016SingleMu
         "HLT_IsoTkMu22",#2016SingleMu
         "HLT_IsoMu24",#2016SingleMu
         "HLT_IsoTkMu24",#2016SingleMu
    ),
    HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZPaths = cms.vstring('HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v[0-9]+'),#2016diEle
    HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZPaths = cms.vstring('HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v[0-9]+'),#2016diEle
    HLT_DoubleEle33_CaloIdL_GsfTrkIdVLPaths = cms.vstring('HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v[0-9]+'),#2016diEle
    HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZPaths = cms.vstring('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v[0-9]+'),#2016diMu
    HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZPaths = cms.vstring('HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v[0-9]+'),#2016diMu
    HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVLPaths = cms.vstring('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v[0-9]+'),#2016diMu
    HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVLPaths = cms.vstring('HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v[0-9]+'),#2016diMu
    HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVLPaths = cms.vstring('HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v[0-9]+'),#2016MuEle
    HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVLPaths = cms.vstring('HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v[0-9]+'),#2016MuEle
    HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZPaths = cms.vstring('HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v[0-9]+'),#2016MuEle
    HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVLPaths = cms.vstring('HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v[0-9]+'),#2016MuEle
    HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVLPaths = cms.vstring('HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v[0-9]+'),#2016MuEle
    HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZPaths = cms.vstring('HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v[0-9]+'),#2016MuEle
    HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVLPaths = cms.vstring('HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v[0-9]+'),#2016MuEle
    HLT_Mu8_DiEle12_CaloIdL_TrackIdLPaths = cms.vstring('HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v[0-9]+'),#2016MuEle
    HLT_DiMu9_Ele9_CaloIdL_TrackIdLPaths = cms.vstring('HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v[0-9]+'),#2016MuEle
    HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdLPaths = cms.vstring('HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v[0-9]+'),#2016triEle
    HLT_TripleMu_12_10_5Paths = cms.vstring('HLT_TripleMu_12_10_5_v[0-9]+'),#2016triMu
    HLT_Ele25_eta2p1_WPTight_GsfPaths = cms.vstring('HLT_Ele25_eta2p1_WPTight_Gsf_v[0-9]+'),#2016SingleEle
    HLT_Ele27_WPTight_GsfPaths = cms.vstring('HLT_Ele27_WPTight_Gsf_v[0-9]+'),#2016SingleEle
    HLT_Ele27_eta2p1_WPLoose_GsfPaths = cms.vstring('HLT_Ele27_eta2p1_WPLoose_Gsf_v[0-9]+'),#2016SingleEle
    HLT_Ele32_eta2p1_WPTight_GsfPaths = cms.vstring('HLT_Ele32_eta2p1_WPTight_Gsf_v[0-9]+'),#2016SingleEle
    HLT_IsoMu20Paths = cms.vstring('HLT_IsoMu20_v[0-9]+'),#2016SingleMu
    HLT_IsoTkMu20Paths = cms.vstring('HLT_IsoTkMu20_v[0-9]+'),#2016SingleMu
    HLT_IsoMu22Paths = cms.vstring('HLT_IsoMu22_v[0-9]+'),#2016SingleMu
    HLT_IsoTkMu22Paths = cms.vstring('HLT_IsoTkMu22_v[0-9]+'),#2016SingleMu
    HLT_IsoMu24Paths = cms.vstring('HLT_IsoMu24_v[0-9]+'),#2016SingleMu
    HLT_IsoTkMu24Paths = cms.vstring('HLT_IsoTkMu24_v[0-9]+'),#2016SingleMu
    trigResultsSrc = cms.InputTag("TriggerResults", "", "HLT"),
    trigPrescaleSrc = cms.InputTag("patTrigger"),

    checkPrescale = cms.bool(False),
    ignoreMissing = cms.untracked.bool(True),
    )
triggerBranches_2017 = cms.PSet(
    trigNames = cms.vstring(
         "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL",#2017diEle
         "HLT_DoubleEle33_CaloIdL_MW",#2017diEle
         "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8",#2017diMu
         "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8",#2017diMu
         "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",#2017MuEle
         'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ',#2017MuEle
         "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",#2017MuEle
         "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",#2017MuEle
         "HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ",#2017MuEle
         "HLT_Mu8_DiEle12_CaloIdL_TrackIdL",#2017MuEle
         "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ",#2017MuEle
         "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL",#2017triEle
         "HLT_TripleMu_12_10_5",#2017triMu
         "HLT_TripleMu_10_5_5_DZ",#2017triMu
         "HLT_Ele35_WPTight_Gsf",#2017SingleEle
         "HLT_Ele38_WPTight_Gsf",#2017SingleEle
         "HLT_Ele40_WPTight_Gsf",#2017SingleEle
         "HLT_IsoMu27",#2017SingleMu
    ),
    HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVLPaths = cms.vstring('HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v[0-9]+'),#2017diEle
    HLT_DoubleEle33_CaloIdL_MWPaths = cms.vstring('HLT_DoubleEle33_CaloIdL_MW_v[0-9]+'),#2017diEle
    HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8Paths = cms.vstring('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v[0-9]+'),#2017diMu
    HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8Paths = cms.vstring('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v[0-9]+'),#2017diMu
    HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVLPaths = cms.vstring('HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v[0-9]+'),#2017MuEle
    HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZPaths = cms.vstring('HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v[0-9]+'),#2017MuEle
    HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZPaths = cms.vstring('HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v[0-9]+'),#2017MuEle
    HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZPaths = cms.vstring('HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v[0-9]+'),#2017MuEle
    HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZPaths = cms.vstring('HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v[0-9]+'),#2017MuEle
    HLT_Mu8_DiEle12_CaloIdL_TrackIdLPaths = cms.vstring('HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v[0-9]+'),#2017MuEle
    HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZPaths = cms.vstring('HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v[0-9]+'),#2017MuEle
    HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdLPaths = cms.vstring('HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v[0-9]+'),#2017triEle
    HLT_TripleMu_12_10_5Paths = cms.vstring('HLT_TripleMu_12_10_5_v[0-9]+'),#2017triMu
    HLT_TripleMu_10_5_5_DZPaths = cms.vstring('HLT_TripleMu_10_5_5_DZ_v[0-9]+'),#2017triMu
    HLT_Ele35_WPTight_GsfPaths = cms.vstring('HLT_Ele35_WPTight_Gsf_v[0-9]+'),#2017SingleEle
    HLT_Ele38_WPTight_GsfPaths = cms.vstring('HLT_Ele38_WPTight_Gsf_v[0-9]+'),#2017SingleEle
    HLT_Ele40_WPTight_GsfPaths = cms.vstring('HLT_Ele40_WPTight_Gsf_v[0-9]+'),#2017SingleEle
    HLT_IsoMu27Paths = cms.vstring('HLT_IsoMu27_v[0-9]+'),#2017SingleMu
    trigResultsSrc = cms.InputTag("TriggerResults", "", "HLT"),
    trigPrescaleSrc = cms.InputTag("patTrigger"),

    checkPrescale = cms.bool(False),
    ignoreMissing = cms.untracked.bool(True),
    )

triggerBranches_2018 = cms.PSet(
    trigNames = cms.vstring(
         "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL",#2018diEle
         "HLT_DoubleEle25_CaloIdL_MW",#2018diEle
         "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8",#2018diMu
         "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",#2018MuEle
         'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ',#2018MuEle
         "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",#2018MuEle
         "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",#2018MuEle
         "HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ",#2018MuEle
         "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ",#2018MuEle
         "HLT_TripleMu_10_5_5_DZ",#2018triMu
         "HLT_TripleMu_12_10_5",#2018triMu
         "HLT_Ele32_WPTight_Gsf",#2018SingleEle
         "HLT_IsoMu24",#2018SingleMu
    ),
    HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVLPaths = cms.vstring('HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v[0-9]+'),#2018diEle
    HLT_DoubleEle25_CaloIdL_MWPaths = cms.vstring('HLT_DoubleEle25_CaloIdL_MW_v[0-9]+'),#2018diEle
    HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8Paths = cms.vstring('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v[0-9]+'),#2018diMu
    HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVLPaths = cms.vstring('HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v[0-9]+'),#2018MuEle
    HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZPaths = cms.vstring('HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v[0-9]+'),#2018MuEle
    HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZPaths = cms.vstring('HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v[0-9]+'),#2018MuEle
    HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZPaths = cms.vstring('HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v[0-9]+'),#2018MuEle
    HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZPaths = cms.vstring('HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v[0-9]+'),#2018MuEle
    HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZPaths = cms.vstring('HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v[0-9]+'),#2018MuEle
    HLT_TripleMu_10_5_5_DZPaths = cms.vstring('HLT_TripleMu_10_5_5_DZ_v[0-9]+'),#2018triMu
    HLT_TripleMu_12_10_5Paths = cms.vstring('HLT_TripleMu_12_10_5_v[0-9]+'),#2018triMu
    HLT_Ele32_WPTight_GsfPaths = cms.vstring('HLT_Ele32_WPTight_Gsf_v[0-9]+'),#2018SingleEle
    HLT_IsoMu24Paths = cms.vstring('HLT_IsoMu24_v[0-9]+'),#2018SingleMu
    trigResultsSrc = cms.InputTag("TriggerResults", "", "HLT"),
    trigPrescaleSrc = cms.InputTag("patTrigger"),

    checkPrescale = cms.bool(False),
    ignoreMissing = cms.untracked.bool(True),
    )
