#!/usr/bin/bash


if [ "$1" == "-h" ] || [ "$1" == "--help" ]
then
    echo "$0 usage: ./$0 [-h|--help] [--hzzExtras] [-j NTHREADS]"
    echo "    --hzzExtras: Get and compile HZZ matrix element and kinematic fit stuff, and generate the UWVV plugins that use them."
    echo "               This is not the default because most people do not need them and one of the packages' authors frequently make changes that break everything without intervention on our side."
    echo "               NB if you use this option and later use scram b clean, you should rerun this script with this option or your CONDOR jobs may fail."
    echo "    --met: Download updated MET correction recipes (needed for MET filters and uncertainties)"
    echo "    -j NTHREADS: [with --hzzExtras] Compile ZZMatrixElement package with NTHREADS threads (default 12)."
    exit 1
fi

while [ "$1" ]
do
    case "$1" in
        --hzzExtras)
            HZZ=1
            ;;
        --met)
            MET=1
            ;;
        -j)
            shift
            UWVVNTHREADS="$1"
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac

    shift
done

if [ ! "$UWVVNTHREADS" ]; then
    UWVVNTHREADS=12
fi

pushd $CMSSW_BASE/src

#Follow: https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsZZ4l2018
#Global Tag
#Data: 94X_dataRun2_v6
#MC: 94X_mc2017_realistic_v13

#ECAL scale and resolution corrections for Moriond18: Run2017_17Nov2017_v1 (time-eta-r9 categories)
#Release is based on CMSSW_9_4_0. Scale and resolution corrections are based on the Golden JSON file of 2017 data (17Nov re-reco)
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt

if [ ! -d ./EgammaAnalysis ]; then
  echo "Setting up electron energy scale corrections"
  #add the repository with the updated Egamma package
  git cms-merge-topic cms-egamma:EGM_94X_v1
  pushd EgammaAnalysis/ElectronTools/data
  # download the txt files with the corrections
  git clone https://github.com/ECALELFS/ScalesSmearings.git
  pushd ScalesSmearings/
  git checkout Run2017_17Nov2017_v1
  popd
fi

#ElectronMVA ID in 94X according to https://twiki.cern.ch/twiki/bin/viewauth/CMS/MultivariateElectronIdentificationRun2#Recipes_for_regular_users
# MVA ID V2 now, not yet available as part of official recepie
git cms-merge-topic guitargeek:ElectronID_MVA2017_V2_HZZ_940pre3
rm -rf RecoEgamma/ElectronIdentification/data #Delete old BDT weights so we can clone new ones
git clone -b ElectronID_MVA2017_V2 https://github.com/guitargeek/RecoEgamma-ElectronIdentification RecoEgamma/ElectronIdentification/data/

#in the EgammaAnalysis/ElectronTools/python/calibrationTablesRun2.py file the you have to make sure that the correctionType 
#is the appropriate for your dataset. For the Run2017_17Nov2017_v1 it has to be:
# correctionType = "Run2017_17Nov2017_v1"  
# The corrections contained in the repository with tag "Run2017_17Nov2017_v1" include updated numbers for the corrections and 
#preliminary conservative version of the systematics.

#####################################NOT USING THIS AT THE MOMENT
if [ "$HZZ" ]; then

    if [ ! -d ./ZZMatrixElement ]; then
        echo -e "\nSetting up ZZ matrix element stuff"
        git clone https://github.com/cms-analysis/HiggsAnalysis-ZZMatrixElement.git ZZMatrixElement

        pushd ZZMatrixElement
        git checkout -b from-v205 v2.0.5

        # Fix their bullshit.
        # We have to authenticate to the CERN server the MCFM library is stored on with a cookie
        # If something is going wrong with ZZMatrixElement stuff, it's probably
        # related to this.
        MCFM_URL=`cat MELA/data/"$SCRAM_ARCH"/download.url`
        # Make cookie
        env -i KRB5CCNAME="$KRB5CCNAME" cern-get-sso-cookie -u "$MCFM_URL" -o MELA/data/"$SCRAM_ARCH"/cookie.txt --krb -r
        if [ ! -e MELA/data/retrieveBkp.csh ]; then
            # Backup the library retrieve script if necessary
            cp MELA/data/retrieve.csh MELA/data/retrieveBkp.csh
        fi
        # Edit their wget command to use the cookie
        sed 's/wget/wget --load-cookies=cookie.txt/' MELA/data/retrieveBkp.csh > MELA/data/retrieve.csh

        # They download the library during their build process.
        # And with our fix, they actually get it instead of the html for the
        # CERN login page...
        source setup.sh -j "$UWVVNTHREADS"
        popd
    fi

    # copy libraries dowloaded by MELA to lib so they get packaged and used by CONDOR
    cp ZZMatrixElement/MELA/data/"$SCRAM_ARCH"/*.so "$CMSSW_BASE"/lib/"$SCRAM_ARCH"

    if [ ! -d ./KinZfitter ]; then
        echo -e "\nSetting up Z kinematic fit stuff"
        git clone https://github.com/VBF-HZZ/KinZfitter.git
    fi

    # generate UWVV's MELA plugin
    cp UWVV/AnalysisTools/plugins/ZZDiscriminantEmbedderCode.txt UWVV/AnalysisTools/plugins/ZZDiscriminantEmbedder.cc
    cp UWVV/AnalysisTools/plugins/ZKinematicFitEmbedderCode.txt UWVV/AnalysisTools/plugins/ZKinematicFitEmbedder.cc
fi
#####################################NOT USING THIS AT THE MOMENT

##IF intetested in re-clustering MET
#https://twiki.cern.ch/twiki/bin/view/CMS/MissingETUncertaintyPrescription#Instructions_for_9_4_X_X_0_for_M
#metTag = cms.InputTag("slimmedMETs")
#from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
#process.testCands = cms.EDFilter("CandPtrSelector",
#                     src=cms.InputTag("packedPFCandidates"),
#                     cut=cms.string("abs(eta)<2.5")
#                      )
#runMetCorAndUncFromMiniAOD(process,
#                           isData=(not IsMC),
#                           pfCandColl=cms.InputTag("testCands"),
#                           reclusterJets=True,
#                           recoMetFromPFCs=True,
#                           postfix="Test",)
#metTag = cms.InputTag("slimmedMETsTest","","ZZ")
#process.MET = cms.Path(process.testCands + process.fullPatMetSequenceTest)

if [ ! -d ./KaMuCa ]; then
    echo "Setting up muon calibration"
    git clone https://github.com/bachtis/analysis.git -b KaMuCa_V4 KaMuCa
fi

popd
