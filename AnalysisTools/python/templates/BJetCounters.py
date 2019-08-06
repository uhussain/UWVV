from UWVV.AnalysisTools.AnalysisFlowBase import AnalysisFlowBase

from UWVV.Utilities.helpers import parseChannels

import FWCore.ParameterSet.Config as cms


class BJetCounters(AnalysisFlowBase):
    def __init__(self, *args, **kwargs):
        super(BJetCounters, self).__init__(*args, **kwargs)


    def makeAnalysisStep(self, stepName, **inputs):
        step = super(BJetCounters, self).makeAnalysisStep(stepName, **inputs)
        
        if stepName == 'initialStateEmbedding':
            jetCounters = {
                # Recommendations via https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
                #https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsZZ4lRunIILegacy#b_tagging
                "DeepCSV_2016" : '? bDiscriminator("pfDeepCSVJetTags:probb + pfDeepCSVJetTags:probbb") > 0.6321 ? 1 : 0',  #medium
                "DeepCSV_2017" : '? bDiscriminator("pfDeepCSVJetTags:probb + pfDeepCSVJetTags:probbb") > 0.4941 ? 1 : 0',  #medium
                "DeepCSV_2018" : '? bDiscriminator("pfDeepCSVJetTags:probb + pfDeepCSVJetTags:probbb") > 0.4184 ? 1 : 0',  #medium
            }
            mod = cms.EDProducer(
                "PATJetCounter",
                src = step.getObjTag('j'),
                labels = cms.vstring(*['nJet'+label for label in jetCounters.keys()]),
                cuts = cms.vstring(*[jetCounters[key] for key in jetCounters.keys()])
                )
            step.addModule("jetCounter", mod)

            labels = ['nJet'+name for name in jetCounters.keys()]
            tags = [cms.InputTag("jetCounter:nJet"+name) for name in jetCounters.keys()]

            for chan in parseChannels('zl'):
                countEmbedding = cms.EDProducer(
                    'PATCompositeCandidateValueEmbedder',
                    src = step.getObjTag(chan),
                    intLabels = cms.vstring(*labels),
                    intSrc = cms.VInputTag(*tags),
                    )
                step.addModule(chan+'JetCountEmbedding', countEmbedding, chan)

        return step

