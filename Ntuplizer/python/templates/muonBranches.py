import FWCore.ParameterSet.Config as cms

muonBranches = cms.PSet(
    floats = cms.PSet(
        RelPFIsoDBR03 = cms.string('(pfIsolationR03.sumChargedParticlePt'
                                '+max(0.0,pfIsolationR03.sumPhotonEt'
                                '+pfIsolationR03.sumNeutralHadronEt'
                                '-0.5*pfIsolationR03.sumPUPt))'
                                '/pt()'),
        RelPFIsoDBR04  = cms.string(
                                '(pfIsolationR04().sumChargedHadronPt'
                                '+ max(0., pfIsolationR04().sumNeutralHadronEt'
                                '+ pfIsolationR04().sumPhotonEt'
                                '- 0.5*pfIsolationR04().sumPUPt))'
                                '/pt()'
        ),  
        PFChargedIso = cms.string('pfIsolationR03.sumChargedParticlePt'),
        PFPhotonIso = cms.string('pfIsolationR03.sumPhotonEt'),
        PFNeutralIso = cms.string('pfIsolationR03.sumNeutralHadronEt'),
        PFPUIso = cms.string('pfIsolationR03.sumPUPt'),
        TrackIso = cms.string('trackIso()'), 
        
        PtErr = cms.string('? hasUserFloat("correctedPtError") ? '
                           'userFloat("correctedPtError") : '
                           'bestTrack.ptError'),
        #RochesterPATMuonCorrector.cc
        RochesterScaleUnc = cms.string('? hasUserFloat("scale_unc") ? '
                                    'userFloat("scale_unc") : 1.'),
        RochesterSmearUnc = cms.string('? hasUserFloat("smear_unc") ? '
                                    'userFloat("smear_unc") : 1.'),

        EffScaleFactor = cms.string('? hasUserFloat("effScaleFactor") ? '
                                    'userFloat("effScaleFactor") : 1.'),
        EffScaleFactorError = cms.string('? hasUserFloat("effScaleFactorError") ? '
                                         'userFloat("effScaleFactorError") : 0.'),
        # TrkRecoEffScaleFactor = cms.string('? hasUserFloat("trkRecoEffScaleFactor") ? '
        #                                    'userFloat("trkRecoEffScaleFactor") : 1.'),
        MtToMET = cms.string('mtToMET'),
        ),
    uints = cms.PSet(
        MatchedStations = cms.string('MatchedStations'),
        NoOfMatches = cms.string('NoOfMatches'),
        BestTrackType = cms.string('BestTrackType'),
        ),
    bools = cms.PSet(
        IsPFMuon = cms.string('isPFMuon'),
        IsGlobal = cms.string('isGlobalMuon'),
        IsTracker = cms.string('isTrackerMuon'),
        IsLoose = cms.string('isLooseMuon'),
        IsMedium = cms.string('isMediumMuon'),
        IsMediumICHEP = cms.string('? hasUserInt("isMediumMuonICHEP") ?'
                                       'userInt("isMediumMuonICHEP") : 0'),
        IsTight = cms.string('? hasUserInt("isTightMuon") ? '
                                'userInt("isTightMuon") : 0'),
        IsWZMedium = cms.string('? hasUserInt("isWZMediumMuon") ?'
                                       'userInt("isWZMediumMuon") : 0'),
        IsWZTightNoIso = cms.string('? hasUserInt("isWZTightMuonNoIso") ?'
                                       'userInt("isWZTightMuonNoIso") : 0'),
        IsWZTight = cms.string('? hasUserInt("isWZTightMuon") ?'
                                       'userInt("isWZTightMuon") : 0'),
        IsWZMediumNoIso = cms.string('? hasUserInt("isWZMediumMuonNoIso") ?'
                                       'userInt("isWZMediumMuonNoIso") : 0'),
        IsWZLooseNoIso = cms.string('? hasUserInt("isWZLooseMuonNoIso") ?'
                                       'userInt("isWZLooseMuonNoIso") : 0'),
        IsWZLoose = cms.string('? hasUserInt("isWZLooseMuon") ?'
                                       'userInt("isWZLooseMuon") : 0'),

        HighPtID = cms.string('? hasUserFloat("ZZIDPassHighPt") ? '
                              'userFloat("ZZIDPassHighPt") : 0.'),
        PFID = cms.string('? hasUserFloat("ZZIDPassPF") ? '
                          'userFloat("ZZIDPassPF") : 0.'),
        HighPtIDNoVtx = cms.string('? hasUserFloat("ZZIDPassHighPtNoVtx") ? '
                                   'userFloat("ZZIDPassHighPtNoVtx") : 0.'),
        PFIDNoVtx = cms.string('? hasUserFloat("ZZIDPassPFNoVtx") ? '
                               'userFloat("ZZIDPassPFNoVtx") : 0.'),
        ),
    )

muonCalibrationBranches = cms.PSet(
    floats = cms.PSet(
        PtUncorrected = cms.string('? hasUserCand("uncorrected") ? '
                                   'userCand("uncorrected").pt : '
                                   'pt'),
        PtErrUncorrected = cms.string('? hasUserCand("uncorrected") ? '
                                      'userCand("uncorrected").bestTrack.ptError : '
                                      'bestTrack.ptError'),
        ),
    )
