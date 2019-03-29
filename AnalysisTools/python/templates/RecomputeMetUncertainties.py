from UWVV.AnalysisTools.AnalysisFlowBase import AnalysisFlowBase

import FWCore.ParameterSet.Config as cms

class RecomputeMetUncertainties(AnalysisFlowBase):
    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'isMC'):
            self.isMC = kwargs.pop('isMC', True)
        super(RecomputeMetUncertainties, self).__init__(*args, **kwargs)

    def makeAnalysisStep(self, stepName, **inputs):
        step = super(RecomputeMetUncertainties, self).makeAnalysisStep(stepName, **inputs)

        if stepName == 'preliminary':
            # Recompute MET uncertainties with new JEC
            from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
            runMetCorAndUncFromMiniAOD(self.process,
                isData=not self.isMC,
                fixEE2017 = True,
                fixEE2017Params = {"userawPt": True, "ptThreshold":50.0, "minEtaThreshold":2.65, "maxEtaThreshold": 3.139} ,
                postfix = "ModifiedMET"
            )   
            step.addModule('fullPatMetSequenceModifiedMET', self.process.fullPatMetSequenceModifiedMET,
                'met_fromUncertaintyTool', met_fromUncertaintyTool = ':Ntuple')
        return step

