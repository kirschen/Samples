import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
    return argParser

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
    if options.update:
        ov = 'update'
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

# Redirector
try:
    redirector = sys.modules['__main__'].redirector
except:
    if "clip" in os.getenv("HOSTNAME").lower():
        from Samples.Tools.config import redirector_clip_local as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Autumn18_nanoAODv6.sql'

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_LO        = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO",       "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=False, xSection=2075.14*3)
<<<<<<< HEAD
#DYJetsToLL_M50_LO_ext2   = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO_ext2",  "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2075.14*3)
=======
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
DYJetsToLL_M50           = Sample.nanoAODfromDAS("DYJetsToLL_M50",          "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M10to50_LO    = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_LO",   "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=18610)

# x-secs using runXSecAnalyzer
DYJetsToLL_M50_HT70to100      =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT70to100",         "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=146.5*1.23)
DYJetsToLL_M50_HT100to200     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200",        "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=160.1*1.23)
DYJetsToLL_M50_HT200to400     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400",        "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=49.22*1.23)
DYJetsToLL_M50_HT400to600     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600",        "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=6.996*1.23)
DYJetsToLL_M50_HT400to600_ext =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600_ext",    "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=6.996*1.23)
DYJetsToLL_M50_HT600to800     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT600to800"   ,     "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.754*1.23 )
DYJetsToLL_M50_HT800to1200    =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT800to1200"  ,     "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.8718*1.23 )
DYJetsToLL_M50_HT1200to2500   =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT1200to2500" ,     "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1938*1.23 )
DYJetsToLL_M50_HT2500toInf    =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT2500toInf"  ,     "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003511*1.23 )

DYJetsM50HT = [
    DYJetsToLL_M50_HT70to100, 
    DYJetsToLL_M50_HT100to200,
    DYJetsToLL_M50_HT200to400,
    DYJetsToLL_M50_HT400to600,
    DYJetsToLL_M50_HT400to600_ext,
    DYJetsToLL_M50_HT600to800  ,
    DYJetsToLL_M50_HT800to1200 ,
    DYJetsToLL_M50_HT1200to2500,
    DYJetsToLL_M50_HT2500toInf ,
]

# x-secs using runXSecAnalyzer
DYJetsToLL_M4to50_HT70to100      = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT70to100"     , "/DYJetsToLL_M-4to50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=147.7) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT100to200"    , "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=203.2) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT200to400"    , "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=54.06) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT400to600"    , "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.696) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT600toInf     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT600toInf"    , "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.843) #LO without 1.23 k-factor

DYJetsM4to50HT = [
   DYJetsToLL_M4to50_HT70to100,
   DYJetsToLL_M4to50_HT100to200,
   DYJetsToLL_M4to50_HT200to400,
   DYJetsToLL_M4to50_HT400to600,
   DYJetsToLL_M4to50_HT600toInf,
]


DY = [
    DYJetsToLL_M50_LO,
<<<<<<< HEAD
#    DYJetsToLL_M50_LO_ext2,
=======
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
    DYJetsToLL_M10to50_LO,
    DYJetsToLL_M50,
] + DYJetsM50HT + DYJetsM4to50HT

## ttbar
TTLep_pow       = Sample.nanoAODfromDAS("TTLep_pow",       "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",           dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*((3*0.108)**2))
TTSingleLep_pow = Sample.nanoAODfromDAS("TTSingleLep_pow", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",           dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*(3*0.108)*(1-3*0.108)*2)
TTHad_pow       = Sample.nanoAODfromDAS("TTHad_pow",       "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v3/NANOAODSIM",           dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*((1-3*0.108)**2))
TTbar           = Sample.nanoAODfromDAS("TTbar",           "/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=831.762)
TTLep_NLO       = Sample.nanoAODfromDAS("TTLep_NLO",       "/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=831.762*((3*0.108)**2))

## single top
TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=(7.20+4.16)*0.108*3)
<<<<<<< HEAD
=======
TToHad_sch              = Sample.nanoAODfromDAS("TToHad_sch",              "/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=(7.20+4.16)*(1-0.108*3))
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c

T_tch_pow           = Sample.nanoAODfromDAS("T_tch_pow",        "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=136.02) # inclusive sample
TBar_tch_pow        = Sample.nanoAODfromDAS("TBar_tch_pow",     "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=80.95) # inclusive sample

T_tWch              = Sample.nanoAODfromDAS("T_tWch",           "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85)
TBar_tWch           = Sample.nanoAODfromDAS("TBar_tWch",        "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85)

<<<<<<< HEAD
=======
T_tWch_incl         = Sample.nanoAODfromDAS("T_tWch_incl",      "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85)
TBar_tWch_incl      = Sample.nanoAODfromDAS("TBar_tWch_incl",   "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=35.85)

>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
## ttH
TTHbbSemiLep        = Sample.nanoAODfromDAS("TTHbbSemiLep",     "/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                                 dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(0.577)*(3*0.108)*(1-3*0.108)*2)
TTHbbLep            = Sample.nanoAODfromDAS("TTHbbLep",         "/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                                 dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(0.577)*((3*0.108)**2))
TTHnobb_pow         = Sample.nanoAODfromDAS("TTHnobb_pow",      "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5085*(1-0.577))

THQ                 = Sample.nanoAODfromDAS("THQ",              "/THQ_4f_Hincl_13TeV_madgraph_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.07096)
THW                 = Sample.nanoAODfromDAS("THW",              "/THW_5f_Hincl_13TeV_madgraph_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                     dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1472)

## ttV
<<<<<<< HEAD
TGJets              = Sample.nanoAODfromDAS("TGJets",     "/TGJets_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.967)
=======
TGJets              = Sample.nanoAODfromDAS("TGJets",           "/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.967)
TGJets_ext          = Sample.nanoAODfromDAS("TGJets_ext",       "/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_ext1_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.967)
TGJets_lep          = Sample.nanoAODfromDAS("TGJets_lep",       "/TGJets_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.967*0.108*3)
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
tZq_ll              = Sample.nanoAODfromDAS("tZq_ll",           "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",                             dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.09418 ) #0.0758 )
tWll                = Sample.nanoAODfromDAS("tWll",             "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01123)
tWnunu              = Sample.nanoAODfromDAS("tWnunu",           "/ST_tWnunu_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01123*1.9822)
TTWToLNu            = Sample.nanoAODfromDAS("TTWToLNu",         "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2043)
TTWToQQ             = Sample.nanoAODfromDAS("TTWToQQ",          "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.40620)
TTW_LO              = Sample.nanoAODfromDAS("TTW_LO",           "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.6105)
TTZToQQ             = Sample.nanoAODfromDAS("TTZToQQ",          "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5297)
TTZToLLNuNu         = Sample.nanoAODfromDAS("TTZToLLNuNu",        "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2728)
TTZToLLNuNu_m1to10  = Sample.nanoAODfromDAS("TTZToLLNuNu_m1to10", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0493)
TTZ_LO              = Sample.nanoAODfromDAS("TTZ_LO",           "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",                                 dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.5297/0.692)

# fixed samples!!
TTGHad_LO                   = Sample.nanoAODfromDAS("TTGHad_LO",             "/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.213*2.565)
TTGHad_ptG100To200_LO       = Sample.nanoAODfromDAS("TTGHad_ptG100To200_LO", "/TTGamma_Hadronic_ptGamma200inf_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1273*2.565)
TTGHad_ptG200_LO            = Sample.nanoAODfromDAS("TTGHad_ptG200_LO",      "/TTGamma_Hadronic_ptGamma100-200_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.02727*2.565)

TTGSingleLep_LO             = Sample.nanoAODfromDAS("TTGSingleLep_LO",             "/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994)
TTGSingleLep_TuneUp_LO      = Sample.nanoAODfromDAS("TTGSingleLep_TuneUp_LO",      "/TTGamma_SingleLept_TuneCP5Up_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994)
TTGSingleLep_TuneDown_LO    = Sample.nanoAODfromDAS("TTGSingleLep_TuneDown_LO",    "/TTGamma_SingleLept_TuneCP5Down_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994)
TTGSingleLep_erdOn_LO       = Sample.nanoAODfromDAS("TTGSingleLep_erdOn_LO",       "/TTGamma_SingleLept_TuneCP5_erdON_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994)
TTGSingleLep_ptG100To200_LO = Sample.nanoAODfromDAS("TTGSingleLep_ptG100To200_LO", "/TTGamma_SingleLept_ptGamma100-200_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1334*1.994)
TTGSingleLep_ptG200_LO      = Sample.nanoAODfromDAS("TTGSingleLep_ptG200_LO",      "/TTGamma_SingleLept_ptGamma200inf_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.02735*1.994)

TTGLep_LO                   = Sample.nanoAODfromDAS("TTGLep_LO",             "/TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.512*1.616)
TTGLep_TuneUp_LO            = Sample.nanoAODfromDAS("TTGLep_TuneUp_LO",      "/TTGamma_Dilept_TuneCP5Up_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.512*1.616)
TTGLep_TuneDown_LO          = Sample.nanoAODfromDAS("TTGLep_TuneDown_LO",    "/TTGamma_Dilept_TuneCP5Down_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.512*1.616)
TTGLep_erdOn_LO             = Sample.nanoAODfromDAS("TTGLep_erdOn_LO",       "/TTGamma_Dilept_TuneCP5_erdON_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.512*1.616)
TTGLep_ptG100To200_LO       = Sample.nanoAODfromDAS("TTGLep_ptG100To200_LO", "/TTGamma_Dilept_ptGamma100-200_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.03469*1.616)
TTGLep_ptG200_LO            = Sample.nanoAODfromDAS("TTGLep_ptG200_LO",      "/TTGamma_Dilept_ptGamma200inf_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.006874*1.616)

TTV = [
    TGJets,
<<<<<<< HEAD
=======
    TGJets_ext,
    TGJets_lep,
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
    TTGHad_LO,
    TTGHad_ptG100To200_LO,
    TTGHad_ptG200_LO,
    TTGSingleLep_LO,
    TTGSingleLep_TuneUp_LO,
    TTGSingleLep_TuneDown_LO,
    TTGSingleLep_erdOn_LO,
    TTGSingleLep_ptG100To200_LO,
    TTGSingleLep_ptG200_LO,
    TTGLep_LO,
    TTGLep_TuneUp_LO,
    TTGLep_TuneDown_LO,
    TTGLep_erdOn_LO,
    TTGLep_ptG100To200_LO,
    TTGLep_ptG200_LO,
    tZq_ll,
    tWll,
    tWnunu,
    TTWToLNu,
    TTWToQQ,
    TTW_LO,
    TTZToQQ,
    TTZToLLNuNu,
    TTZToLLNuNu_m1to10,
    TTZ_LO,
]

top = [
    TTLep_pow,
    TTSingleLep_pow,
    TTHad_pow,
    TTbar,
    TTLep_NLO,
    TToLeptons_sch_amcatnlo,
    T_tch_pow,
    TBar_tch_pow,
    T_tWch,
    TBar_tWch,
<<<<<<< HEAD
=======
    T_tWch_incl,
    TBar_tWch_incl,
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
    TTHbbLep,
    TTHbbSemiLep,
    TTHnobb_pow,
    THQ,
    THW,
    ] + TTV

## di/multiboson
<<<<<<< HEAD
WWTo2L2Nu           = Sample.nanoAODfromDAS("WWTo2L2Nu",        "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=12.178 )
WWDoubleTo2L        = Sample.nanoAODfromDAS("WWDoubleTo2L",         "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1729)
WWToLNuQQ           = Sample.nanoAODfromDAS("WWToLNuQQ",        "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=49.997)
#WWToLNuQQ_ext       = Sample.nanoAODfromDAS("WWToLNuQQ_ext",    "/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=49.997)
WWTo1L1Nu2Q         = Sample.nanoAODfromDAS("WWTo1L1Nu2Q",          "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=49.997)
=======
WWTo2L2Nu           = Sample.nanoAODfromDAS("WWTo2L2Nu",       "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=12.178 )
WWDoubleTo2L        = Sample.nanoAODfromDAS("WWDoubleTo2L",    "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1729)
WWToLNuQQ           = Sample.nanoAODfromDAS("WWToLNuQQ",       "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=49.997)
WWTo1L1Nu2Q         = Sample.nanoAODfromDAS("WWTo1L1Nu2Q",     "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=49.997)
WWTo4Q              = Sample.nanoAODfromDAS("WWTo4Q",          "/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=-1)
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c

ZZTo2L2Nu           = Sample.nanoAODfromDAS("ZZTo2L2Nu",            "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",                   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.564)
ZZTo2L2Q            = Sample.nanoAODfromDAS("ZZTo2L2Q",             "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                   dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3.28)
ZZTo2Q2Nu           = Sample.nanoAODfromDAS("ZZTo2Q2Nu",            "/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.04)
ZZTo4L              = Sample.nanoAODfromDAS("ZZTo4L",               "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",                      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.256*1.1)

WZTo1L3Nu           = Sample.nanoAODfromDAS("WZTo1L3Nu"  ,          "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=(47.13)*(3*0.108)*(0.2) )
<<<<<<< HEAD
#WZTo1L1Nu2Q         = Sample.nanoAODfromDAS("WZTo1L1Nu2Q",          "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=10.71)
WZTo2L2Q            = Sample.nanoAODfromDAS("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",           dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.60)
=======
WZTo1L1Nu2Q         = Sample.nanoAODfromDAS("WZTo1L1Nu2Q",          "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=10.71)
WZTo2L2Q            = Sample.nanoAODfromDAS("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",           dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.60)
WZTo3LNu            = Sample.nanoAODfromDAS("WZTo3LNu",             "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.42965)
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
WZTo3LNu_ext        = Sample.nanoAODfromDAS("WZTo3LNu_ext",         "/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",       dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.42965)
WZTo3LNu_amcatnlo   = Sample.nanoAODfromDAS("WZTo3LNu_amcatnlo",    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",              dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.666)

VVTo2L2Nu           = Sample.nanoAODfromDAS("VVTo2L2Nu",            "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=14.00)

WGToLNuG                = Sample.nanoAODfromDAS("WGToLNuG", "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=489.) # NLO xsec from TOP-17-016 * NNLO scale factor from Tom Cornelis 489 (NLO) * 1.14
WGToLNuG_amcatnlo_ext1  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext1", "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=203.3)
<<<<<<< HEAD
#WGToLNuG_amcatnlo_ext3  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext3", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext3-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=203.3)
#WGJets              = Sample.nanoAODfromDAS("WGJets", "", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.6637)
#ZNuNuGJets              = Sample.nanoAODfromDAS("ZNuNuGJets", "/ZNuNuGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1903)
#ZNuNuGJets_40130    = Sample.nanoAODfromDAS("ZNuNuGJets_40130", "/ZNuNuGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.816)

#ZH_HtoBB_ZtoLL      = Sample.nanoAODfromDAS("ZH_HtoBB_ZtoLL", "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=)
ZGToLLG             = Sample.nanoAODfromDAS("ZGToLLG",         "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=50.2)
ZGToLLG_lowMLL      = Sample.nanoAODfromDAS("ZGToLLG_lowMLL",  "/ZGToLLG_01J_5f_lowMLL_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=106.1) #NLO xsec * NNLO k-factor from 7TeV calculations (Tom) https://hypernews.cern.ch/HyperNews/CMS/get/generators/2772/1/1/1/1/1/1/1/1.html

WW                  = Sample.nanoAODfromDAS("WW",                   "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=63.21 * 1.82)
#WW_ext              = Sample.nanoAODfromDAS("WW_ext",               "/WW_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=63.21 * 1.82)
WZ                  = Sample.nanoAODfromDAS("WZ",                   "/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=47.13)
#WZ_ext              = Sample.nanoAODfromDAS("WZ_ext",               "/WZ_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=47.13)
=======

ZGToLLG              = Sample.nanoAODfromDAS("ZGToLLG",              "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=50.2)
ZGToLLG_lowMLL       = Sample.nanoAODfromDAS("ZGToLLG_lowMLL",       "/ZGToLLG_01J_5f_lowMLL_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=106.1) #NLO xsec * NNLO k-factor from 7TeV calculations (Tom) https://hypernews.cern.ch/HyperNews/CMS/get/generators/2772/1/1/1/1/1/1/1/1.html
ZGToLLG_LoosePtlPtg  = Sample.nanoAODfromDAS("ZGToLLG_LoosePtlPtg",  "/ZGToLLG_01J_LoosePtlPtg_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=-1) #NLO xsec * NNLO k-factor from 7TeV calculations (Tom) https://hypernews.cern.ch/HyperNews/CMS/get/generators/2772/1/1/1/1/1/1/1/1.html

WW                  = Sample.nanoAODfromDAS("WW",                   "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=63.21 * 1.82)
WZ                  = Sample.nanoAODfromDAS("WZ",                   "/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=47.13)
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
ZZ                  = Sample.nanoAODfromDAS("ZZ",                   "/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",                         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=16.523)

WWW_4F              = Sample.nanoAODfromDAS("WWW_4F",               "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",            dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.2086)
WWZ                 = Sample.nanoAODfromDAS("WWZ",                  "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.1651)
WZZ                 = Sample.nanoAODfromDAS("WZZ",                  "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.05565)
ZZZ                 = Sample.nanoAODfromDAS("ZZZ",                  "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",               dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01398)




boson = [
<<<<<<< HEAD
#    ZH_HtoBB_ZtoLL,
    WWTo2L2Nu,
    WWToLNuQQ,
#    WWToLNuQQ_ext,
    WWTo1L1Nu2Q,
=======
    WWTo2L2Nu,
    WWToLNuQQ,
    WWTo1L1Nu2Q,
    WWTo4Q,
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
    WWDoubleTo2L,
    ZZTo2L2Nu,
    ZZTo2L2Q,
    ZZTo2Q2Nu,
    ZZTo4L,
    WZTo1L3Nu,
<<<<<<< HEAD
#    WZTo1L1Nu2Q,
    WZTo2L2Q,
=======
    WZTo1L1Nu2Q,
    WZTo2L2Q,
    WZTo3LNu,
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
    WZTo3LNu_ext,
    WZTo3LNu_amcatnlo,
    VVTo2L2Nu,
    WGToLNuG,
    WGToLNuG_amcatnlo_ext1,
<<<<<<< HEAD
#    WGToLNuG_amcatnlo_ext3,
#    WGJets,
#    ZNuNuGJets_40130,
    ZGToLLG,
    ZGToLLG_lowMLL,
    WW,
#    WW_ext,
    WZ,
#    WZ_ext,
=======
    ZGToLLG,
    ZGToLLG_lowMLL,
    ZGToLLG_LoosePtlPtg,
    WW,
    WZ,
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
    ZZ,
    WWW_4F,
    WWZ,
    WZZ,
    ZZZ,
    ]

# W+jets
WJetsToLNu      = Sample.nanoAODfromDAS("WJetsToLNu",           "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3* 20508.9)
<<<<<<< HEAD
#WJetsToLNu_ext  = Sample.nanoAODfromDAS("WJetsToLNu_ext",       "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3* 20508.9)
=======
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c

W1JetsToLNu     = Sample.nanoAODfromDAS("W1JetsToLNu",           "/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=11524.) #NLO xsec from AN-2016/289
W2JetsToLNu     = Sample.nanoAODfromDAS("W2JetsToLNu",           "/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3788.) #NLO xsec from AN-2016/289
W3JetsToLNu     = Sample.nanoAODfromDAS("W3JetsToLNu",           "/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1144.) #NLO xsec from AN-2016/289
W4JetsToLNu     = Sample.nanoAODfromDAS("W4JetsToLNu",           "/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=636.) #NLO xsec from AN-2016/289

W1JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W1JetsToLNu_NuPt_200", "/W1JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2.397)
W2JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W2JetsToLNu_NuPt_200", "/W2JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3.897)
W3JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W3JetsToLNu_NuPt_200", "/W3JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3.298)
W4JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W4JetsToLNu_NuPt_200", "/W4JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.453)

wjets = [
    WJetsToLNu,
<<<<<<< HEAD
#    WJetsToLNu_ext,
=======
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
    W1JetsToLNu,
    W2JetsToLNu,
    W3JetsToLNu,
    W4JetsToLNu,
    W1JetsToLNu_NuPt_200,
    W2JetsToLNu_NuPt_200,
    W3JetsToLNu_NuPt_200,
    W4JetsToLNu_NuPt_200,
    ]

## rare
TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.009103)
<<<<<<< HEAD
#TTWH = Sample.nanoAODfromDAS("TTWH", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=) #sample is processed, xsec is missing
=======
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
TTWW = Sample.nanoAODfromDAS("TTWW", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.007829)
TTWZ = Sample.nanoAODfromDAS("TTWZ", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.002919)
TTZZ = Sample.nanoAODfromDAS("TTZZ", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001573)

rare = [
    TTTT,
<<<<<<< HEAD
#    TTWH,
=======
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
    TTWW,
    TTWZ,
    TTZZ,
    ]

GluGluHToZZTo4L             = Sample.nanoAODfromDAS("GluGluHToZZTo4L",             "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.01297)
<<<<<<< HEAD
#GluGluToContinToZZTo2e2mu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/*/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.005423) #No nanoAODv6 found
#GluGluToContinToZZTo2e2tau  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/*/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.005423) #No nanoAODv6 found
=======
GluGluToContinToZZTo2e2mu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_ext1_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.005423) #No nanoAODv6 found
GluGluToContinToZZTo2e2tau  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_ext1_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.005423) #No nanoAODv6 found
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
GluGluToContinToZZTo2mu2tau = Sample.nanoAODfromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.005423)
GluGluToContinToZZTo4e      = Sample.nanoAODfromDAS("GluGluToContinToZZTo4e",      "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0027)
GluGluToContinToZZTo4mu     = Sample.nanoAODfromDAS("GluGluToContinToZZTo4mu",     "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0027)
GluGluToContinToZZTo4tau    = Sample.nanoAODfromDAS("GluGluToContinToZZTo4tau",    "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.0027)



gluglu = [
    GluGluHToZZTo4L,
<<<<<<< HEAD
#    GluGluToContinToZZTo2e2mu,
#    GluGluToContinToZZTo2e2tau,
=======
    GluGluToContinToZZTo2e2mu,
    GluGluToContinToZZTo2e2tau,
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
    GluGluToContinToZZTo2mu2tau,
    GluGluToContinToZZTo4e,
    GluGluToContinToZZTo4mu,
    GluGluToContinToZZTo4tau,
]

QCD_Mu_pt15to20         = Sample.nanoAODfromDAS("QCD_Mu_pt15to20",         "/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3629000.0)
QCD_Mu_pt20to30         = Sample.nanoAODfromDAS("QCD_Mu_pt20to30",         "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=3168000.0)
QCD_Mu_pt30to50         = Sample.nanoAODfromDAS("QCD_Mu_pt30to50",         "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1649000.0)
QCD_Mu_pt50to80         = Sample.nanoAODfromDAS("QCD_Mu_pt50to80",         "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=445700.0)
QCD_Mu_pt80to120        = Sample.nanoAODfromDAS("QCD_Mu_pt80to120",        "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=105500.0)
QCD_Mu_pt120to170       = Sample.nanoAODfromDAS("QCD_Mu_pt120to170",       "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=25540.0)
QCD_Mu_pt120to170_ext   = Sample.nanoAODfromDAS("QCD_Mu_pt120to170_ext",   "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=25540.0)
QCD_Mu_pt170to300       = Sample.nanoAODfromDAS("QCD_Mu_pt170to300",       "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=8670.0)
QCD_Mu_pt300to470       = Sample.nanoAODfromDAS("QCD_Mu_pt300to470",       "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=797.5)
QCD_Mu_pt300to470_ext   = Sample.nanoAODfromDAS("QCD_Mu_pt300to470_ext",   "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext3-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=797.5)
QCD_Mu_pt470to600       = Sample.nanoAODfromDAS("QCD_Mu_pt470to600",       "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=78.67)
QCD_Mu_pt600to800       = Sample.nanoAODfromDAS("QCD_Mu_pt600to800",       "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=25.33)
<<<<<<< HEAD
#QCD_Mu_pt800to1000      = Sample.nanoAODfromDAS("QCD_Mu_pt800to1000",      "", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.715)
QCD_Mu_pt800to1000_ext  = Sample.nanoAODfromDAS("QCD_Mu_pt800to1000_ext",  "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext3-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.715)
=======
QCD_Mu_pt800to1000      = Sample.nanoAODfromDAS("QCD_Mu_pt800to1000_ext",  "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext3-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.715)
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
QCD_Mu_pt1000toInf      = Sample.nanoAODfromDAS("QCD_Mu_pt1000toInf",      "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.605)

QCD_Ele_pt20to30     = Sample.nanoAODfromDAS("QCD_Ele_pt20to30",    "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5533000.0)
QCD_Ele_pt30to50     = Sample.nanoAODfromDAS("QCD_Ele_pt30to50",    "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=6952000.0)
QCD_Ele_pt50to80     = Sample.nanoAODfromDAS("QCD_Ele_pt50to80",    "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2206000.0)
QCD_Ele_pt80to120    = Sample.nanoAODfromDAS("QCD_Ele_pt80to120",   "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=415400.0)
QCD_Ele_pt120to170   = Sample.nanoAODfromDAS("QCD_Ele_pt120to170",  "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=75820.0)
QCD_Ele_pt170to300   = Sample.nanoAODfromDAS("QCD_Ele_pt170to300",  "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=18860.0)
QCD_Ele_pt300toInf   = Sample.nanoAODfromDAS("QCD_Ele_pt300toInf",  "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1210.0)

QCD = [
        QCD_Mu_pt15to20,
        QCD_Mu_pt20to30,
        QCD_Mu_pt30to50,
        QCD_Mu_pt50to80,
        QCD_Mu_pt80to120,
        QCD_Mu_pt120to170,
        QCD_Mu_pt120to170_ext,
        QCD_Mu_pt170to300,
        QCD_Mu_pt300to470,
        QCD_Mu_pt300to470_ext,
        QCD_Mu_pt470to600,
        QCD_Mu_pt600to800,
<<<<<<< HEAD
#        QCD_Mu_pt800to1000,
        QCD_Mu_pt800to1000_ext,
=======
        QCD_Mu_pt800to1000,
>>>>>>> 4ed32c13b6c673352c3e2542d8cc70a405225f8c
        QCD_Mu_pt1000toInf,

        QCD_Ele_pt20to30,
        QCD_Ele_pt30to50,
        QCD_Ele_pt50to80,
        QCD_Ele_pt80to120,
        QCD_Ele_pt120to170,
        QCD_Ele_pt170to300,
        QCD_Ele_pt300toInf,
]

GJets_HT40to100        = Sample.nanoAODfromDAS("GJets_HT40to100",      "/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=20730)
GJets_HT100to200       = Sample.nanoAODfromDAS("GJets_HT100to200",     "/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_4cores5k_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=9226)
GJets_HT200to400       = Sample.nanoAODfromDAS("GJets_HT200to400",     "/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=2300)
GJets_HT400to600       = Sample.nanoAODfromDAS("GJets_HT400to600",     "/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=274.4)
GJets_HT600toInf       = Sample.nanoAODfromDAS("GJets_HT600toInf",     "/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=93.38)
GJets_HT600toInf_ext   = Sample.nanoAODfromDAS("GJets_HT600toInf_ext", "/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=93.38)

GJetsHT = [
           GJets_HT40to100,
           GJets_HT100to200,
           GJets_HT200to400,
           GJets_HT400to600,
           GJets_HT600toInf,
           GJets_HT600toInf_ext,
]


other = [
    ]

allSamples = DY + top + boson + wjets + rare + other + gluglu + QCD + GJetsHT

for s in allSamples:
    s.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
