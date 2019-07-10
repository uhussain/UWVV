from UWVV.AnalysisTools.AnalysisFlowBase import AnalysisFlowBase

import FWCore.ParameterSet.Config as cms

class MuonCalibration(AnalysisFlowBase):
    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'isMC'):
            self.isMC = kwargs.pop('isMC', True)
        if not hasattr(self, 'isSync'):
            self.isSync = self.isMC and kwargs.pop('isSync', False)
        if not hasattr(self, 'year'):
            self.year = kwargs.pop('year', '2016')
        if not hasattr(self, 'muonClosureShift'):
            self.muonClosureShift = kwargs.pop('muonClosureShift', 0) if self.isMC else 0
        super(MuonCalibration, self).__init__(*args, **kwargs)

    def makeAnalysisStep(self, stepName, **inputs):
        step = super(MuonCalibration, self).makeAnalysisStep(stepName, **inputs)

        if stepName == 'preliminary':
            #if self.isMC:
            #    calibType = 'MC_80X_13TeV'
            #else:
            #    calibType = 'DATA_80X_13TeV'
            LeptonSetup = cms.string(self.year)

            if LeptonSetup=="2016":
                muCalibrator = cms.EDProducer(
                    "RochesterPATMuonCorrector",
                    src = step.getObjTag('m'),
                    identifier = cms.string("RoccoR2016"),
                    isMC = cms.bool(self.isMC),
                    isSync = cms.bool(self.isSync),
                    maxPt = cms.double(200),
                    #relics of the old KalmanCorrector 
                    #calibType = cms.string(calibType),
                    #closureShift = cms.int32(self.muonClosureShift),
                    )
            if LeptonSetup=="2017":
                muCalibrator = cms.EDProducer(
                    "RochesterPATMuonCorrector",
                    src = step.getObjTag('m'),
                    identifier = cms.string("RoccoR2017"),
                    isMC = cms.bool(self.isMC),
                    isSync = cms.bool(self.isSync),
                    maxPt = cms.double(200),
                    #relics of the old KalmanCorrector 
                    #calibType = cms.string(calibType),
                    #closureShift = cms.int32(self.muonClosureShift),
                    )
            if LeptonSetup=="2018":
                muCalibrator = cms.EDProducer(
                    "RochesterPATMuonCorrector",
                    src = step.getObjTag('m'),
                    identifier = cms.string("RoccoR2018"),
                    isMC = cms.bool(self.isMC),
                    isSync = cms.bool(self.isSync),
                    maxPt = cms.double(200),
                    #relics of the old KalmanCorrector 
                    #calibType = cms.string(calibType),
                    #closureShift = cms.int32(self.muonClosureShift),
                    )
            step.addModule('calibratedPatMuons', muCalibrator, 'm')

            # need to re-sort now that we're calibrated
            mSort = cms.EDProducer(
                "PATMuonCollectionSorter",
                src = step.getObjTag('m'),
                function = cms.string('pt'),
                )
            step.addModule('muonSorting', mSort, 'm')

        return step








