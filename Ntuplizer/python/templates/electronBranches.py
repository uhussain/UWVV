import FWCore.ParameterSet.Config as cms


electronBranches = cms.PSet(
    floats = cms.PSet(
        MVAIDIso = cms.string('? hasUserFloat("MVAIsoID")?' 'userFloat("MVAIsoID"): 1.'),
        RelPFIsoRho = cms.string('(pfIsolationVariables.sumChargedHadronPt'
                                 '+max(0.0,pfIsolationVariables.sumNeutralHadronEt'
                                 '+pfIsolationVariables.sumPhotonEt'
                                 '-userFloat("rho_fastjet")*userFloat("EffectiveArea")))'
                                 '/pt'),
        Rho = cms.string('userFloat("rho_fastjet")'),
        EffectiveArea = cms.string('userFloat("EffectiveArea")'),
        PFChargedIso = cms.string('pfIsolationVariables.sumChargedHadronPt'),
        PFPhotonIso = cms.string('pfIsolationVariables.sumPhotonEt'),
        PFNeutralIso = cms.string('pfIsolationVariables.sumNeutralHadronEt'),
        PFPUIso = cms.string('pfIsolationVariables.sumPUPt'),
        SCEta = cms.string('superCluster.eta'),
        SCPhi = cms.string('superCluster.phi'),
        SCEnergy = cms.string('superCluster.energy'),
        SCRawEnergy = cms.string('superCluster.rawEnergy'),

        UnCorrPt = cms.string('? hasUserFloat("uncorrected_pt") ? '
                           'userFloat("uncorrected_pt") : '
                           '1.'),

        ScaleTotUp = cms.string('? hasUserFloat("scale_total_up") ? '
                                    'userFloat("scale_total_up") : 0.'),
        ScaleSystUp = cms.string('? hasUserFloat("scale_syst_up") ? '
                                    'userFloat("scale_syst_up") : 0.'),
        ScaleStatUp = cms.string('? hasUserFloat("scale_stat_up") ? '
                                    'userFloat("scale_stat_up") : 0.'),
        ScaleGainUp = cms.string('? hasUserFloat("scale_gain_up") ? '
                                    'userFloat("scale_gain_up") : 0.'),
        ScaleTotDn = cms.string('? hasUserFloat("scale_total_dn") ? '
                                    'userFloat("scale_total_dn") : 0.'),
        ScaleSystDn = cms.string('? hasUserFloat("scale_syst_dn") ? '
                                    'userFloat("scale_syst_dn") : 0.'),
        ScaleStatDn = cms.string('? hasUserFloat("scale_stat_dn") ? '
                                    'userFloat("scale_stat_dn") : 0.'),
        ScaleGainDn = cms.string('? hasUserFloat("scale_gain_dn") ? '
                                    'userFloat("scale_gain_dn") : 0.'),

        SigmaTotUp = cms.string('? hasUserFloat("sigma_total_up") ? '
                                    'userFloat("sigma_total_up") : 0.'),
        SigmaRhoUp = cms.string('? hasUserFloat("sigma_rho_up") ? '
                                    'userFloat("sigma_rho_up") : 0.'),
        SigmaPhiUp = cms.string('? hasUserFloat("sigma_phi_up") ? '
                                    'userFloat("sigma_phi_up") : 0.'),
        SigmaTotDn = cms.string('? hasUserFloat("sigma_total_dn") ? '
                                    'userFloat("sigma_total_dn") : 0.'),
        SigmaRhoDn = cms.string('? hasUserFloat("sigma_rho_dn") ? '
                                    'userFloat("sigma_rho_dn") : 0.'),
        SigmaPhiDn = cms.string('? hasUserFloat("sigma_phi_dn") ? '
                                    'userFloat("sigma_phi_dn") : 0.'),
        # apparently there's a bug with multiple ternary operators, so cheat
        EffScaleFactor = cms.string('? hasUserFloat("effScaleFactorGap") && '
                                    '  hasUserFloat("effScaleFactor") && '
                                    '  hasUserFloat("trkRecoEffScaleFactor") ? '
                                    'userFloat("trkRecoEffScaleFactor") * '
                                    '(isGap * userFloat("effScaleFactorGap") + '
                                    ' (1-isGap) * userFloat("effScaleFactor")) :'
                                    '1.'),
        EffScaleFactorError = cms.string('? hasUserFloat("effScaleFactorGapError") && '
                                         '  hasUserFloat("effScaleFactorError") && '
                                         '  hasUserFloat("trkRecoEffScaleFactorError") && '
                                         '  hasUserFloat("trkRecoEffScaleFactorExtraError") ? '
                                         'sqrt((userFloat("trkRecoEffScaleFactorError") + '
                                         '      userFloat("trkRecoEffScaleFactorExtraError"))^2 + '
                                         '(isGap * userFloat("effScaleFactorGapError") + '
                                         '(1-isGap) * userFloat("effScaleFactorError"))^2) :'
                                         '0.'),
        TrkRecoEffScaleFactor = cms.string('? hasUserFloat("trkRecoEffScaleFactor") ? '
                                           'userFloat("trkRecoEffScaleFactor") : 1.'),
        TrkRecoEffScaleFactorError = cms.string('(? hasUserFloat("trkRecoEffScaleFactorError") && '
                                                '   hasUserFloat("trkRecoEffScaleFactorExtraError") ? '
                                                ' userFloat("trkRecoEffScaleFactorError") + '
                                                ' userFloat("trkRecoEffScaleFactorExtraError") : '
                                                ' 0.)'),
        IDIsoEffScaleFactor = cms.string('? hasUserFloat("effScaleFactorGap") && '
                                         '  hasUserFloat("effScaleFactor") ? '
                                         'isGap * userFloat("effScaleFactorGap") + '
                                         '(1-isGap) * userFloat("effScaleFactor") :'
                                         '1.'),
        IDIsoEffScaleFactorError = cms.string('? hasUserFloat("effScaleFactorGapError") && '
                                              '  hasUserFloat("effScaleFactorError") ? '
                                              'isGap * userFloat("effScaleFactorGapError") + '
                                              '(1-isGap) * userFloat("effScaleFactorError") :'
                                              '0.'),

        ),

    uints = cms.PSet(
        MissingHits = cms.string('MissingHits'),
        ),
    bools = cms.PSet(
        IsGap = cms.string('isGap'),
        IsEB = cms.string('isEB'),
        IsCBVIDTightNoIP = cms.string('? hasUserFloat("IsCBVIDTight") ? '
                                  'userFloat("IsCBVIDTight") : 0'),
        IsCBVIDTight = cms.string('? hasUserFloat("IsCBVIDTightwIP") ? '
                                  'userFloat("IsCBVIDTightwIP") : 0'),
        IsCBVIDMediumNoIP = cms.string('? hasUserFloat("IsCBVIDMedium") ?'
                                   'userFloat("IsCBVIDMedium") : 0'),
        IsCBVIDMedium = cms.string('? hasUserFloat("IsCBVIDMediumwIP") ? '
                                  'userFloat("IsCBVIDMediumwIP") : 0'),
        IsCBVIDLooseNoIP = cms.string('? hasUserFloat("IsCBVIDLoose") ? '
                                  'userFloat("IsCBVIDLoose") : 0'),
        IsCBVIDLoose = cms.string('? hasUserFloat("IsCBVIDLoosewIP") ? '
                                  'userFloat("IsCBVIDLoosewIP") : 0'),
        IsCBVIDVetoNoIP = cms.string('? hasUserFloat("IsCBVIDVeto") ? '
                                  'userFloat("IsCBVIDVeto") : 0'),
        IsCBVIDVeto = cms.string('? hasUserFloat("IsCBVIDVetowIP") ? '
                                  'userFloat("IsCBVIDVetowIP") : 0'),
        IsCBVIDHLTSafeNoIP = cms.string('? hasUserFloat("IsCBVIDHLTSafe") ? '
                                  'userFloat("IsCBVIDHLTSafe") : 0'),
        IsCBVIDHLTSafe = cms.string('? hasUserFloat("IsCBVIDHLTSafewIP") ? '
                                  'userFloat("IsCBVIDHLTSafewIP") : 0'),
        IsWWLoose = cms.string('? hasUserInt("IsWWLoose") ? '
                                  'userInt("IsWWLoose") : 0'),
        )
    )
