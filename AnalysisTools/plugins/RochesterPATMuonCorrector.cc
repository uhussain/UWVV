/*
  \class    modules::RochesterPATMuonCorrector
  \brief    Applies Rochester corrections to muons
  \author   */


#include <FWCore/Framework/interface/Frameworkfwd.h>
#include <FWCore/Framework/interface/EDProducer.h>
#include <FWCore/Framework/interface/Event.h>
#include <FWCore/ParameterSet/interface/ParameterSet.h>
#include <FWCore/Framework/interface/ESHandle.h>

#include <DataFormats/PatCandidates/interface/Muon.h>

// Rochester Muon Corrections
#include <UWVV/AnalysisTools/plugins/RoccoR.h>


#include "TLorentzVector.h"
#include "TRandom3.h"


#include <vector>
#include <string>
#include <sstream>

using namespace edm;
using namespace std;
using namespace reco;


class RochesterPATMuonCorrector : public edm::EDProducer {
 public:
  /// Constructor
  explicit RochesterPATMuonCorrector(const edm::ParameterSet& params);
	
  /// Destructor
  ~RochesterPATMuonCorrector(){
    delete calibrator;
  };

 private:
  virtual void beginJob(){};
  virtual void produce(edm::Event& event, const edm::EventSetup& setup);
  virtual void endJob(){};

  const edm::EDGetTokenT<edm::View<pat::Muon> > srcToken;
  const string identifier;
  const bool isMC;
  const bool isSync;
  const double maxPt;

  RoccoR* calibrator;
  TRandom3* rgen_;

};


RochesterPATMuonCorrector::RochesterPATMuonCorrector(const edm::ParameterSet& params) :
  srcToken(consumes<edm::View<pat::Muon> >(params.getParameter<edm::InputTag>("src"))),
  identifier(params.getParameter<string>("identifier")),
  isMC(params.getParameter<bool>("isMC")),
  isSync(params.getParameter<bool>("isSync")),
  maxPt(params.exists("maxPt") ? params.getParameter<double>("maxPt") : 200.),
  calibrator(0),
  rgen_(0)
{
  stringstream ss;
  ss << "UWVV/data/RochesterCorrections/" << identifier << ".txt";
  string path_string = ss.str();
  edm::FileInPath corrPath("UWVV/data/RochesterCorrections/"+identifier+".txt");
	
  calibrator = new RoccoR(corrPath.fullPath());
  rgen_ = new TRandom3(0);
	
  produces<pat::MuonCollection>();
}


void
RochesterPATMuonCorrector::produce(edm::Event& event, const edm::EventSetup& setup)
{
  // Input collection
  edm::Handle<edm::View<pat::Muon> > in;
  event.getByToken(srcToken, in);

  // Output collection
  std::unique_ptr<std::vector<pat::Muon> > out(new std::vector<pat::Muon>);
  	
  for (unsigned i=0; i<in->size(); ++i) {

    edm::Ptr<pat::Muon> muIn = in->ptrAt(i);

    double pt = muIn->pt();

    out->push_back(*muIn);
	 
    int nl;
    auto gen_particle = muIn->genParticle();
    double scale_factor=1.0;
    double scale_error = 0.;
    double smear_error = 0.;
    double u1 = rgen_->Rndm();
    double u2 = rgen_->Rndm();
	
	 if(isSync) {u1 = 1.; u2 = 1.;}
	 
	  

    if (calibrator != 0  && muIn->muonBestTrackType() == 1 && pt <= maxPt)
    {
    double eta = muIn->eta();
    double phi = muIn->phi();
    double ptErr = muIn->bestTrack()->ptError();
		nl = muIn->track()->hitPattern().trackerLayersWithMeasurement();
		
      if(isMC && nl > 5)//Protection against muons with low number of layers, they are not used in the analysis anyway as we apply thight muon ID
      {
			
			/// ====== ON MC (correction plus smearing) =====
			if ( gen_particle != 0)
			{
				scale_factor = calibrator->kScaleFromGenMC(muIn->charge(), pt, muIn->eta(), muIn->phi(), nl, gen_particle->pt(), u1);
				smear_error = calibrator->kScaleFromGenMCerror(muIn->charge(), pt, muIn->eta(), muIn->phi(), nl, gen_particle->pt(), u1);
				
			}
			else
			{
				scale_factor = calibrator->kScaleAndSmearMC(muIn->charge(), pt, muIn->eta(), muIn->phi(), nl, u1, u2);
				smear_error = calibrator->kScaleAndSmearMCerror(muIn->charge(), pt, muIn->eta(), muIn->phi(), nl, u1, u2);
				
			}
			
			scale_error = calibrator->kScaleDTerror(muIn->charge(), pt, muIn->eta(), muIn->phi());
			
			pt = pt*scale_factor;
			ptErr = ptErr*scale_factor;
      }
		 
      else if(!isMC && nl > 5)
      {
			/// ====== ON DATA (correction only) =====
			if(muIn->pt()>2.0 && fabs(muIn->eta())<2.4)
			{
			  scale_factor = calibrator->kScaleDT(muIn->charge(), pt, muIn->eta(), muIn->phi());
			  scale_error = calibrator->kScaleDTerror(muIn->charge(), pt, muIn->eta(), muIn->phi());
			  smear_error = calibrator->kScaleAndSmearMCerror(muIn->charge(), pt, muIn->eta(), muIn->phi(), nl, u1, u2);
			}
			else
			{
			  // keep old values
			  scale_factor = 1.;
			  scale_error = 0.;
			  smear_error = 0.;
			}
			
			pt = pt*scale_factor;
			ptErr = ptErr*scale_factor;
      } 
      //std::vector::back returns a direct reference to the last element in the vector
      out->back().setP4(reco::Particle::PolarLorentzVector(pt, eta, phi, muIn->mass()));
      out->back().addUserFloat("correctedPtError", ptErr);
	    out->back().addUserFloat("scale_unc", 1. + scale_error);
      out->back().addUserFloat("smear_unc", 1. + smear_error);
      out->back().addUserCand("uncorrected", muIn);
      }
    }
  event.put(std::move(out));

}


#include <FWCore/Framework/interface/MakerMacros.h>
DEFINE_FWK_MODULE(RochesterPATMuonCorrector);
