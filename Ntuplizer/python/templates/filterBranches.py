import FWCore.ParameterSet.Config as cms


# MET filters for 2017 and 2018 following: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#MET_Filter_Recommendations_for_R
metAndBadMuonFilters = cms.PSet(
    trigNames = cms.vstring(
         'Flag_HBHENoiseFilter',
         'Flag_HBHENoiseIsoFilter',
         'Flag_EcalDeadCellTriggerPrimitiveFilter',
         'Flag_goodVertices',
         'Flag_eeBadScFilter',
         'Flag_globalSuperTightHalo2016Filter',
         #'Flag_BadChargedCandidateFilter',#not recommended,under review
         'Flag_BadPFMuonFilter',
    ),
    Flag_HBHENoiseFilterPaths = cms.vstring('Flag_HBHENoiseFilter'),
    Flag_HBHENoiseIsoFilterPaths = cms.vstring('Flag_HBHENoiseIsoFilter'),
    Flag_EcalDeadCellTriggerPrimitiveFilterPaths = cms.vstring('Flag_EcalDeadCellTriggerPrimitiveFilter'),
    Flag_goodVerticesPaths = cms.vstring('Flag_goodVertices'),
    Flag_eeBadScFilterPaths = cms.vstring('Flag_eeBadScFilter'),
    Flag_globalSuperTightHalo2016FilterPaths = cms.vstring('Flag_globalSuperTightHalo2016Filter'),
    #Flag_BadChargedCandidateFilterPaths = cms.vstring('Flag_BadChargedCandidateFilter'),
    Flag_BadPFMuonFilterPaths = cms.vstring('Flag_BadPFMuonFilter'),

    trigResultsSrc = cms.InputTag("TriggerResults", "", "RECO"),
    trigPrescaleSrc = cms.InputTag("patTrigger"),
    checkPrescale = cms.bool(False),
    )

# MET filters for 2017 and 2018 following: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#MET_Filter_Recommendations_for_R
metFilters = cms.PSet(
    trigNames = cms.vstring(
         'Flag_HBHENoiseFilter',
         'Flag_HBHENoiseIsoFilter',
         'Flag_EcalDeadCellTriggerPrimitiveFilter',
         'Flag_goodVertices',
         'Flag_globalSuperTightHalo2016Filter',
         #'Flag_BadChargedCandidateFilter',
         'Flag_BadPFMuonFilter',
    ),
    Flag_HBHENoiseFilterPaths = cms.vstring('Flag_HBHENoiseFilter'),
    Flag_HBHENoiseIsoFilterPaths = cms.vstring('Flag_HBHENoiseIsoFilter'),
    Flag_EcalDeadCellTriggerPrimitiveFilterPaths = cms.vstring('Flag_EcalDeadCellTriggerPrimitiveFilter'),
    Flag_goodVerticesPaths = cms.vstring('Flag_goodVertices'),
    Flag_globalSuperTightHalo2016FilterPaths = cms.vstring('Flag_globalSuperTightHalo2016Filter'),
    #Flag_BadChargedCandidateFilterPaths = cms.vstring('Flag_BadChargedCandidateFilter'),
    Flag_BadPFMuonFilterPaths = cms.vstring('Flag_BadPFMuonFilter'),

    trigResultsSrc = cms.InputTag("TriggerResults", "", "PAT"),
    trigPrescaleSrc = cms.InputTag("patTrigger"),
    checkPrescale = cms.bool(False),
    )

# MET filters for 2016 following: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#MET_Filter_Recommendations_for_R
metAndBadMuonFilters_2016 = cms.PSet(
    trigNames = cms.vstring(
         'Flag_HBHENoiseFilter',
         'Flag_HBHENoiseIsoFilter',
         'Flag_EcalDeadCellTriggerPrimitiveFilter',
         'Flag_goodVertices',
         'Flag_eeBadScFilter',
         'Flag_globalSuperTightHalo2016Filter',
         #'Flag_BadChargedCandidateFilter',#not recommended,under review
         #'Flag_BadPFMuonFilter',#not available in 2016 miniAOD directly?
    ),
    Flag_HBHENoiseFilterPaths = cms.vstring('Flag_HBHENoiseFilter'),
    Flag_HBHENoiseIsoFilterPaths = cms.vstring('Flag_HBHENoiseIsoFilter'),
    Flag_EcalDeadCellTriggerPrimitiveFilterPaths = cms.vstring('Flag_EcalDeadCellTriggerPrimitiveFilter'),
    Flag_goodVerticesPaths = cms.vstring('Flag_goodVertices'),
    Flag_eeBadScFilterPaths = cms.vstring('Flag_eeBadScFilter'),
    Flag_globalSuperTightHalo2016FilterPaths = cms.vstring('Flag_globalSuperTightHalo2016Filter'),
    #Flag_BadChargedCandidateFilterPaths = cms.vstring('Flag_BadChargedCandidateFilter'),
    #Flag_BadPFMuonFilterPaths = cms.vstring('Flag_BadPFMuonFilter'),#not available in 2016 miniAOD directly

    trigResultsSrc = cms.InputTag("TriggerResults", "", "RECO"),
    trigPrescaleSrc = cms.InputTag("patTrigger"),
    checkPrescale = cms.bool(False),
    )

# MET filters for 2016 following: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#MET_Filter_Recommendations_for_R
metFilters_2016 = cms.PSet(
    trigNames = cms.vstring(
         'Flag_HBHENoiseFilter',
         'Flag_HBHENoiseIsoFilter',
         'Flag_EcalDeadCellTriggerPrimitiveFilter',
         'Flag_goodVertices',
         'Flag_globalSuperTightHalo2016Filter',
         #'Flag_BadChargedCandidateFilter',
         #'Flag_BadPFMuonFilter',
    ),
    Flag_HBHENoiseFilterPaths = cms.vstring('Flag_HBHENoiseFilter'),
    Flag_HBHENoiseIsoFilterPaths = cms.vstring('Flag_HBHENoiseIsoFilter'),
    Flag_EcalDeadCellTriggerPrimitiveFilterPaths = cms.vstring('Flag_EcalDeadCellTriggerPrimitiveFilter'),
    Flag_goodVerticesPaths = cms.vstring('Flag_goodVertices'),
    Flag_globalSuperTightHalo2016FilterPaths = cms.vstring('Flag_globalSuperTightHalo2016Filter'),
    #Flag_BadChargedCandidateFilterPaths = cms.vstring('Flag_BadChargedCandidateFilter'),
    #Flag_BadPFMuonFilterPaths = cms.vstring('Flag_BadPFMuonFilter'),

    trigResultsSrc = cms.InputTag("TriggerResults", "", "PAT"),
    trigPrescaleSrc = cms.InputTag("patTrigger"),
    checkPrescale = cms.bool(False),
    )
