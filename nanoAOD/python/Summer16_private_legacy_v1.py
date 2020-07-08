import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
    argParser.add_argument('--check_completeness', action='store_true',    help="Check competeness?")
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

#from Samples.Tools.config import  redirector_global


# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+"/DB_Summer16_private_legacy.sql"

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_LO_ext1   = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO_ext1",  "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M50_LO_ext2   = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO_ext2",  "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M50_ext2      = Sample.nanoAODfromDAS("DYJetsToLL_M50_ext2",     "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M10to50_LO    = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_LO",   "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v6-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=18610)
DYJetsToLL_M10to50       = Sample.nanoAODfromDAS("DYJetsToLL_M10to50",      "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=18610)


DYJetsToLL_M50_HT70to100      =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT70to100"    ,     "/DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=169.9*1.23)
DYJetsToLL_M50_HT100to200_ext =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200_ext",    "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=147.4*1.23)
DYJetsToLL_M50_HT200to400     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400",        "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=40.99*1.23)
DYJetsToLL_M50_HT200to400_ext =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400_ext",    "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=40.99*1.23)
DYJetsToLL_M50_HT400to600     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600",        "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.678*1.23)
DYJetsToLL_M50_HT400to600_ext =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600_ext",    "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.678*1.23)
DYJetsToLL_M50_HT600to800     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT600to800"   ,     "/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.367*1.23 )
DYJetsToLL_M50_HT800to1200    =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT800to1200"  ,     "/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.6304*1.23 )
DYJetsToLL_M50_HT1200to2500   =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT1200to2500" ,     "/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1514*1.23 )
DYJetsToLL_M50_HT2500toInf    =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT2500toInf"  ,     "/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.003565*1.23 )

DYJetsM50HT = [
DYJetsToLL_M50_HT70to100   , 
DYJetsToLL_M50_HT100to200_ext,
DYJetsToLL_M50_HT200to400,
DYJetsToLL_M50_HT200to400_ext,
DYJetsToLL_M50_HT400to600,
DYJetsToLL_M50_HT400to600_ext,
DYJetsToLL_M50_HT600to800  ,
DYJetsToLL_M50_HT800to1200 ,
DYJetsToLL_M50_HT1200to2500,
DYJetsToLL_M50_HT2500toInf ,
]

DYJetsToLL_M5to50_HT70to100      = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT70to100"     , "/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=303.4) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT100to200"    , "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=224.2) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT100to200_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT100to200_ext", "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=224.2) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT200to400"    , "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=37.2) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT200to400_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT200to400_ext", "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=37.2) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT400to600"    , "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.581) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT400to600_ext = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT400to600_ext", "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.581) #LO without 1.23 k-factor
DYJetsToLL_M5to50_HT600toInf     = Sample.nanoAODfromDAS("DYJetsToLL_M5to50_HT600toInf"    , "/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.124) #LO without 1.23 k-factor

DYJetsM5to50HT = [
DYJetsToLL_M5to50_HT70to100,
DYJetsToLL_M5to50_HT100to200,
DYJetsToLL_M5to50_HT100to200_ext,
DYJetsToLL_M5to50_HT200to400,
DYJetsToLL_M5to50_HT200to400_ext,
DYJetsToLL_M5to50_HT400to600,
DYJetsToLL_M5to50_HT400to600_ext,
DYJetsToLL_M5to50_HT600toInf,
]


DY = [
    DYJetsToLL_M50_LO_ext1,
    DYJetsToLL_M50_LO_ext2,
    DYJetsToLL_M10to50,
    DYJetsToLL_M10to50_LO,
    DYJetsToLL_M50_ext2,
    ] + DYJetsM50HT + DYJetsM5to50HT

### ttbar
TTLep_pow       = Sample.nanoAODfromDAS("TTLep_pow",            "/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*((3*0.108)**2))
#TTLep_pow_noSC  = Sample.nanoAODfromDAS("TTLep_pow_noSC",       "/TTTo2L2Nu_noSC_TuneCUETP8M2T4_13TeV-powheg-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*((3*0.108)**2))
#TTSingleLep_pow = Sample.nanoAODfromDAS("TTSingleLep_pow",      "/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*(3*0.108)*(1-3*0.108)*2)
#TTbar           = Sample.nanoAODfromDAS("TTbar",                "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762)
#
### single top
## s-channel missing!! https://hypernews.cern.ch/HyperNews/CMS/get/prep-ops/6062.html
#TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(7.20+4.16)*0.108*3)
#
#T_tch_pow           = Sample.nanoAODfromDAS("T_tch_pow",        "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=136.02) # inclusive sample
#TBar_tch_pow        = Sample.nanoAODfromDAS("TBar_tch_pow",     "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=80.95) # inclusive sample
#
#T_tWch_ext          = Sample.nanoAODfromDAS("T_tWch_ext",       "/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.85*(1-(1-3*0.108)**2))
#TBar_tWch_ext       = Sample.nanoAODfromDAS("TBar_tWch_ext",    "/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.85*(1-(1-3*0.108)**2))
#
### ttH
#TTHbb               = Sample.nanoAODfromDAS("TTHbb",            "/ttHTobb_M125_13TeV_powheg_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                                 dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5085*(0.577))
#TTHnobb_pow         = Sample.nanoAODfromDAS("TTHnobb_pow",      "/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5085*(1-0.577))
#
#THQ                 = Sample.nanoAODfromDAS("THQ",              "/THQ_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.07096)
#THW                 = Sample.nanoAODfromDAS("THW",              "/THW_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1472)
#
### ttV
#TGJets              = Sample.nanoAODfromDAS("TGJets",     "/TGJets_leptonDecays_13TeV_amcatnlo_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.967*(0.108*3))
##TGJets_ext          = Sample.nanoAODfromDAS("TGJets_ext", "/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2.967)
#tZq_ll_ext          = Sample.nanoAODfromDAS("tZq_ll_ext",       "/tZq_ll_4f_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",                             dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.09418 ) #0.0758 )
#tZq_nunu            = Sample.nanoAODfromDAS("tZq_nunu",         "/tZq_nunu_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1/dspitzba-crab_RunIISummer16MiniAODv3-94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",                               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2728 )
#tWll                = Sample.nanoAODfromDAS("tWll",             "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                              dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01123)
#tWnunu              = Sample.nanoAODfromDAS("tWnunu",           "/ST_tWnunu_5f_LO_13TeV-MadGraph-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                            dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01123*1.9822)
#TTWToLNu_ext2       = Sample.nanoAODfromDAS("TTWToLNu_ext2",    "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2043)
#TTWToQQ             = Sample.nanoAODfromDAS("TTWToQQ",          "/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.40620)
#TTZToQQ             = Sample.nanoAODfromDAS("TTZToQQ",          "/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5297)
#TTZToLLNuNu_ext2    = Sample.nanoAODfromDAS("TTZToLLNuNu_ext2", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2728)
#TTZToLLNuNu_ext3    = Sample.nanoAODfromDAS("TTZToLLNuNu_ext3", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2728)
#TTZToLLNuNu_m1to10  = Sample.nanoAODfromDAS("TTZToLLNuNu_m1to10", "/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-94X_mcRun2_asymptotic_v3-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0493)
#TTZ_LO              = Sample.nanoAODfromDAS("TTZ_LO",           "/ttZJets_13TeV_madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                                 dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5297/0.692)
#TTGJets             = Sample.nanoAODfromDAS("TTGJets",          "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.697)
#TTGJets_ext         = Sample.nanoAODfromDAS("TTGJets_ext",      "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.697)
#
## fixed samples!!
#TTGHad_LO                   = Sample.nanoAODfromDAS("TTGHad_LO",             "/TTGamma_Hadronic_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.213*2.565)
#TTGHad_ptG100To200_LO       = Sample.nanoAODfromDAS("TTGHad_ptG100To200_LO", "/TTGamma_Hadronic_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1273*2.565)
#TTGHad_ptG200_LO            = Sample.nanoAODfromDAS("TTGHad_ptG200_LO",      "/TTGamma_Hadronic_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.02727*2.565)
#
#TTGSingleLep_LO             = Sample.nanoAODfromDAS("TTGSingleLep_LO",             "/TTGamma_SingleLept_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.125*1.994)
#TTGSingleLep_TuneUp_LO      = Sample.nanoAODfromDAS("TTGSingleLep_TuneUp_LO",      "/TTGamma_SingleLept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.125*1.994)
#TTGSingleLep_TuneDown_LO    = Sample.nanoAODfromDAS("TTGSingleLep_TuneDown_LO",    "/TTGamma_SingleLept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.125*1.994)
#TTGSingleLep_erdOn_LO       = Sample.nanoAODfromDAS("TTGSingleLep_erdOn_LO",       "/TTGamma_SingleLept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.125*1.994)
#TTGSingleLep_ptG100To200_LO = Sample.nanoAODfromDAS("TTGSingleLep_ptG100To200_LO", "/TTGamma_SingleLept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1334*1.994)
#TTGSingleLep_ptG200_LO      = Sample.nanoAODfromDAS("TTGSingleLep_ptG200_LO",      "/TTGamma_SingleLept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.02735*1.994)
#
#TTGLep_LO                   = Sample.nanoAODfromDAS("TTGLep_LO",             "/TTGamma_Dilept_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.512*1.616)
#TTGLep_TuneUp_LO            = Sample.nanoAODfromDAS("TTGLep_TuneUp_LO",      "/TTGamma_Dilept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.512*1.616)
#TTGLep_TuneDown_LO          = Sample.nanoAODfromDAS("TTGLep_TuneDown_LO",    "/TTGamma_Dilept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.512*1.616)
#TTGLep_erdOn_LO             = Sample.nanoAODfromDAS("TTGLep_erdOn_LO",       "/TTGamma_Dilept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.512*1.616)
#TTGLep_ptG100To200_LO       = Sample.nanoAODfromDAS("TTGLep_ptG100To200_LO", "/TTGamma_Dilept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.03469*1.616)
#TTGLep_ptG200_LO            = Sample.nanoAODfromDAS("TTGLep_ptG200_LO",      "/TTGamma_Dilept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-adb1c0680ca8faceb354b8e08ff53745/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.006874*1.616)
#
#TTV = [
#    TGJets,
##    TGJets_ext,
#    TTGHad_LO,
#    TTGHad_ptG100To200_LO,
#    TTGHad_ptG200_LO,
#    TTGSingleLep_LO,
#    TTGSingleLep_TuneUp_LO,
#    TTGSingleLep_TuneDown_LO,
#    TTGSingleLep_erdOn_LO,
#    TTGSingleLep_ptG100To200_LO,
#    TTGSingleLep_ptG200_LO,
#    TTGLep_LO,
#    TTGLep_TuneUp_LO,
#    TTGLep_TuneDown_LO,
#    TTGLep_erdOn_LO,
#    TTGLep_ptG100To200_LO,
#    TTGLep_ptG200_LO,
#    tZq_ll_ext,
#    tZq_nunu,
#    tWll,
#    tWnunu,
#    TTWToLNu_ext2,
#    TTWToQQ,
##    TTW_LO,
#    TTZToQQ,
#    TTZToLLNuNu_ext2,
#    TTZToLLNuNu_ext3,
#    TTZToLLNuNu_m1to10,
#    TTZ_LO,
#    TTGJets,
#    TTGJets_ext,
#]
#
##TTGG                 = Sample.nanoAODfromDAS("TTGG",          "/TTGG_0Jets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM",              dbFile=dbFile, redirector=redirector_global, overwrite=ov, xSection=0.01731)
##TTWZ                 = Sample.nanoAODfromDAS("TTWZ",            "/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM",              dbFile=dbFile, redirector=redirector_global, overwrite=ov, xSection=0.002938)
##TTZZ                 = Sample.nanoAODfromDAS("TTZZ",            "/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6_ext1-v1/NANOAODSIM" ,              dbFile=dbFile, redirector=redirector_global, overwrite=ov, xSection=0.001563)
##TGG                 = Sample.nanoAODfromDAS("TGG", "/TGGJets_leptonDecays_13TeV_MadGraph_madspin_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM",dbFile=dbFile, overwrite=ov, redirector=redirector_global, xSection=0.007793)
#
#TTVV = [
##    TTGG,
##    TTWZ,
##    TTZZ,
#    #TGG
#    ]
#
top = [
    TTLep_pow,
]
#    TTLep_pow_noSC,
#    TTSingleLep_pow,
#    TTbar,
#    TToLeptons_sch_amcatnlo,
#    T_tch_pow,
#    TBar_tch_pow,
#    T_tWch_ext,
#    TBar_tWch_ext,
#    TTHbb,
#    TTHnobb_pow,
##    TTHnobb_mWCutfix_ext,
#    THQ,
#    THW,
#    ] + TTV + TTVV
#
### di/multiboson
#WWTo2L2Nu           = Sample.nanoAODfromDAS("WWTo2L2Nu",        "/WWTo2L2Nu_13TeV-powheg/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=12.178)
#WWToLNuQQ           = Sample.nanoAODfromDAS("WWToLNuQQ",        "/WWToLNuQQ_13TeV-powheg/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=49.997)
##WWToLNuQQ_ext       = Sample.nanoAODfromDAS("WWToLNuQQ_ext",    "/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=49.997)
#WWTo1L1Nu2Q         = Sample.nanoAODfromDAS("WWTo1L1Nu2Q",          "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=49.997 )
#
#ZZTo2L2Nu           = Sample.nanoAODfromDAS("ZZTo2L2Nu",            "/ZZTo2L2Nu_13TeV_powheg_pythia8_ext1/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.564)
#ZZTo2L2Q            = Sample.nanoAODfromDAS("ZZTo2L2Q",             "/ZZTo2L2Q_13TeV_powheg_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.28)
#ZZTo2Q2Nu           = Sample.nanoAODfromDAS("ZZTo2Q2Nu",            "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",          dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.04)
#ZZTo4L              = Sample.nanoAODfromDAS("ZZTo4L",               "/ZZTo4L_13TeV_powheg_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",                           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.256*1.1)
#
#WZTo1L3Nu           = Sample.nanoAODfromDAS("WZTo1L3Nu"  ,          "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",          dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(47.13)*(3*0.108)*(0.2) )
#WZTo1L1Nu2Q         = Sample.nanoAODfromDAS("WZTo1L1Nu2Q",          "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=10.71)
#WZTo2L2Q            = Sample.nanoAODfromDAS("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.60)
#WZTo3LNu_ext        = Sample.nanoAODfromDAS("WZTo3LNu_ext",         "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.42965)
#WZTo3LNu_amcatnlo   = Sample.nanoAODfromDAS("WZTo3LNu_amcatnlo",    "/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.666)
#
#VVTo2L2Nu           = Sample.nanoAODfromDAS("VVTo2L2Nu",            "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",          dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=11.95)
#VVTo2L2Nu_ext       = Sample.nanoAODfromDAS("VVTo2L2Nu_ext",        "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=11.95)
#
#
#WGToLNuG                = Sample.nanoAODfromDAS("WGToLNuG", "/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=377.7*1.295) # NLO xsec from TOP-17-016 for 2016
#
#WGToLNuG_amcatnlo       = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo", "/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=203.3) 
##WGToLNuG_amcatnlo_ext3  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext3", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext3-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=203.3) 
##WGJets              = Sample.nanoAODfromDAS("WGJets", "/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.6637)
##ZNuNuGJets              = Sample.nanoAODfromDAS("ZNuNuGJets", "/ZNuNuGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.1903)
##ZNuNuGJets_40130    = Sample.nanoAODfromDAS("ZNuNuGJets_40130", "/ZNuNuGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2.816)
#
#ZGTo2LG_ext         = Sample.nanoAODfromDAS("ZGTo2LG_ext",          "/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=131.3)
#ZGToLLG             = Sample.nanoAODfromDAS("ZGToLLG",              "/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=50.2)
#ZGToLLG_lowMLL      = Sample.nanoAODfromDAS("ZGToLLG_lowMLL",       "/ZGToLLG_01J_5f_lowMLL_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=98.3 ) #NLO xsec * NNLO k-factor from 7TeV calculations (Tom) https://hypernews.cern.ch/HyperNews/CMS/get/generators/2772/1/1/1/1/1/1/1/1.html
#WWDoubleTo2L        = Sample.nanoAODfromDAS("WWDoubleTo2L",         "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",              dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1729)
#
#WW                  = Sample.nanoAODfromDAS("WW",                   "/WW_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=63.21 * 1.82)
#WW_ext              = Sample.nanoAODfromDAS("WW_ext",               "/WW_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=63.21 * 1.82)
#WZ                  = Sample.nanoAODfromDAS("WZ",                   "/WZ_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=47.13)
#WZ_ext              = Sample.nanoAODfromDAS("WZ_ext",               "/WZ_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=47.13)
#ZZ                  = Sample.nanoAODfromDAS("ZZ",                   "/ZZ_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=16.523)
#
#WWW_4F              = Sample.nanoAODfromDAS("WWW_4F",               "/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",            dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2086)
#WWZ                 = Sample.nanoAODfromDAS("WWZ",                  "/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1651)
#WZZ                 = Sample.nanoAODfromDAS("WZZ",                  "/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.05565)
#ZZZ                 = Sample.nanoAODfromDAS("ZZZ",                  "/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01398)
#
#
#
#
#boson = [
#    WWTo2L2Nu,
#    WWToLNuQQ,
##    WWToLNuQQ_ext,
#    WWTo1L1Nu2Q,
#    ZZTo2L2Nu,
#    ZZTo2L2Q,
#    ZZTo2Q2Nu,
#    ZZTo4L,
#    WZTo1L3Nu,
#    WZTo1L1Nu2Q,
#    WZTo2L2Q,
#    WZTo3LNu_ext,
#    WZTo3LNu_amcatnlo,
#    VVTo2L2Nu,
#    VVTo2L2Nu_ext,
#    WGToLNuG,
#    WGToLNuG_amcatnlo,
##    WGToLNuG_amcatnlo_ext3,
##    WGJets,
##    ZNuNuGJets_40130,
#    ZGTo2LG_ext,
#    ZGToLLG,
#    ZGToLLG_lowMLL,
#    WWDoubleTo2L,
#    WW,WW_ext,
#    WZ,WZ_ext,
#    ZZ,
#    WWW_4F,
#    WWZ,
#    WZZ,
#    ZZZ,
#    ]
#
## W+jets
#WJetsToLNu      = Sample.nanoAODfromDAS("WJetsToLNu",           "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3* 20508.9)
#WJetsToLNu_ext  = Sample.nanoAODfromDAS("WJetsToLNu_ext",       "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3* 20508.9)
#
#W1JetsToLNu     = Sample.nanoAODfromDAS("W1JetsToLNu",          "/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=11524.) #9602. #NLO xsec from AN-2016/289
#W2JetsToLNu     = Sample.nanoAODfromDAS("W2JetsToLNu",          "/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3788.) #3167. #NLO xsec from AN-2016/289
#W3JetsToLNu     = Sample.nanoAODfromDAS("W3JetsToLNu",          "/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1144.) #948.5 #NLO xsec from AN-2016/289
#W4JetsToLNu     = Sample.nanoAODfromDAS("W4JetsToLNu",          "/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=636.) #492.9 #NLO xsec from AN-2016/289
#
#W1JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W1JetsToLNu_NuPt_200", "/W1JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.049)
#W2JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W2JetsToLNu_NuPt_200", "/W2JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.555)
#W3JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W3JetsToLNu_NuPt_200", "/W3JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.274)
#W4JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W4JetsToLNu_NuPt_200", "/W4JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.991)
#
#wjets = [
#    WJetsToLNu,
#    WJetsToLNu_ext,
#    W1JetsToLNu,
#    W2JetsToLNu,
#    W3JetsToLNu,
#    W4JetsToLNu,
#    W1JetsToLNu_NuPt_200,
#    W2JetsToLNu_NuPt_200,
#    W3JetsToLNu_NuPt_200,
#    W4JetsToLNu_NuPt_200,
#    ]
#
### HT-binned
#WJetsToLNu_HT70to100        = Sample.nanoAODfromDAS("WJetsToLNu_HT70to100",        "/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=1637.13)
#WJetsToLNu_HT100to200       = Sample.nanoAODfromDAS("WJetsToLNu_HT100to200",       "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=1627.45)
##WJetsToLNu_HT100to200_ext   = Sample.nanoAODfromDAS("WJetsToLNu_HT100to200_ext",   "",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=1627.45)
##WJetsToLNu_HT100to200_ext2  = Sample.nanoAODfromDAS("WJetsToLNu_HT100to200_ext2",  "",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=1627.45)
#WJetsToLNu_HT200to400       = Sample.nanoAODfromDAS("WJetsToLNu_HT200to400",       "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=435.237)
#WJetsToLNu_HT200to400_ext   = Sample.nanoAODfromDAS("WJetsToLNu_HT200to400_ext",   "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=435.237)
#WJetsToLNu_HT200to400_ext2  = Sample.nanoAODfromDAS("WJetsToLNu_HT200to400_ext2",  "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=435.237)
#WJetsToLNu_HT400to600       = Sample.nanoAODfromDAS("WJetsToLNu_HT400to600",       "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=59.1811)
#WJetsToLNu_HT400to600_ext   = Sample.nanoAODfromDAS("WJetsToLNu_HT400to600_ext",   "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=59.1811)
#WJetsToLNu_HT600to800       = Sample.nanoAODfromDAS("WJetsToLNu_HT600to800",       "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=14.5805)
#WJetsToLNu_HT600to800_ext   = Sample.nanoAODfromDAS("WJetsToLNu_HT600to800_ext",   "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=14.5805)
#WJetsToLNu_HT800to1200      = Sample.nanoAODfromDAS("WJetsToLNu_HT800to1200",      "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=6.65621)
#WJetsToLNu_HT800to1200_ext  = Sample.nanoAODfromDAS("WJetsToLNu_HT800to1200_ext",  "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=6.65621)
#WJetsToLNu_HT1200to2500     = Sample.nanoAODfromDAS("WJetsToLNu_HT1200to2500",     "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=1.60809)
#WJetsToLNu_HT1200to2500_ext = Sample.nanoAODfromDAS("WJetsToLNu_HT1200to2500_ext", "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=1.60809)
#WJetsToLNu_HT2500toInf      = Sample.nanoAODfromDAS("WJetsToLNu_HT2500toInf",      "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=0.0389136)
#WJetsToLNu_HT2500toInf_ext  = Sample.nanoAODfromDAS("WJetsToLNu_HT2500toInf_ext",  "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=0.0389136)
#
#
#wjets_ht = [
#    WJetsToLNu_HT70to100,
#    WJetsToLNu_HT100to200,
##    WJetsToLNu_HT100to200_ext,
##    WJetsToLNu_HT100to200_ext2,
#    WJetsToLNu_HT200to400,
#    WJetsToLNu_HT200to400_ext,
#    WJetsToLNu_HT200to400_ext2,
#    WJetsToLNu_HT400to600,
#    WJetsToLNu_HT400to600_ext,
#    WJetsToLNu_HT600to800,
#    WJetsToLNu_HT600to800_ext,
#    WJetsToLNu_HT800to1200,
#    WJetsToLNu_HT800to1200_ext,
#    WJetsToLNu_HT1200to2500,
#    WJetsToLNu_HT1200to2500_ext,
#    WJetsToLNu_HT2500toInf,
#    WJetsToLNu_HT2500toInf_ext,
#    ]
#
#wjets += wjets_ht
#
### rare
#TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER", dbFile=dbFile, redirector=redirector, instance="phys03", xSection=0.009103)
#TTWW = Sample.nanoAODfromDAS("TTWW", "/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER", dbFile=dbFile, redirector=redirector, instance="phys03", xSection=0.007829)
#TTWZ = Sample.nanoAODfromDAS("TTWZ", "/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER", dbFile=dbFile, redirector=redirector, instance="phys03", xSection=0.002919)
#TTZZ = Sample.nanoAODfromDAS("TTZZ", "/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER", dbFile=dbFile, redirector=redirector, instance="phys03", xSection=0.001573)
#
#rare = [
#    TTTT,
#    TTWW,
#    TTWZ,
#    TTZZ,
#    ]
#
#
#signals = [
#    ]
#
#
#GluGluHToZZTo4L             = Sample.nanoAODfromDAS("GluGluHToZZTo4L",   "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01297)
#GluGluToContinToZZTo2e2mu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423)
#GluGluToContinToZZTo2e2tau  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423)
#GluGluToContinToZZTo2mu2tau = Sample.nanoAODfromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423)
#GluGluToContinToZZTo4e      = Sample.nanoAODfromDAS("GluGluToContinToZZTo4e",      "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)
#GluGluToContinToZZTo4mu     = Sample.nanoAODfromDAS("GluGluToContinToZZTo4mu",     "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)
#GluGluToContinToZZTo4tau    = Sample.nanoAODfromDAS("GluGluToContinToZZTo4tau",    "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)
#
#gluglu = [
#    GluGluHToZZTo4L,
#    GluGluToContinToZZTo2e2mu,
#    GluGluToContinToZZTo2e2tau,
#    GluGluToContinToZZTo2mu2tau,
#    GluGluToContinToZZTo4e,
#    GluGluToContinToZZTo4mu,
#    GluGluToContinToZZTo4tau,
#]
#
#QCD_Mu_pt15to20         = Sample.nanoAODfromDAS("QCD_Mu_pt15to20",            "/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3629000.0)
#QCD_Mu_pt20to30         = Sample.nanoAODfromDAS("QCD_Mu_pt20to30",            "/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3168000.0)
#QCD_Mu_pt30to50         = Sample.nanoAODfromDAS("QCD_Mu_pt30to50",            "/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1649000.0)
#QCD_Mu_pt50to80         = Sample.nanoAODfromDAS("QCD_Mu_pt50to80",            "/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=445700.0)
#QCD_Mu_pt80to120        = Sample.nanoAODfromDAS("QCD_Mu_pt80to120",           "/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=105500.0)
#QCD_Mu_pt80to120_ext1   = Sample.nanoAODfromDAS("QCD_Mu_pt80to120_ext1",      "/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=105500.0)
#QCD_Mu_pt120to170       = Sample.nanoAODfromDAS("QCD_Mu_pt120to170",          "/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=25540.0)
#QCD_Mu_pt170to300       = Sample.nanoAODfromDAS("QCD_Mu_pt170to300",          "/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=8670.0)
#QCD_Mu_pt170to300_ext1  = Sample.nanoAODfromDAS("QCD_Mu_pt170to300_ext1",     "/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=8670.0)
#QCD_Mu_pt300to470       = Sample.nanoAODfromDAS("QCD_Mu_pt300to470",          "/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=797.5)
#QCD_Mu_pt300to470_ext1  = Sample.nanoAODfromDAS("QCD_Mu_pt300to470_ext1",     "/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=797.5)
#QCD_Mu_pt470to600       = Sample.nanoAODfromDAS("QCD_Mu_pt470to600",          "/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=78.67)
#QCD_Mu_pt470to600_ext1  = Sample.nanoAODfromDAS("QCD_Mu_pt470to600_ext1",     "/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=78.67)
#QCD_Mu_pt600to800       = Sample.nanoAODfromDAS("QCD_Mu_pt600to800",          "/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=25.33)
#QCD_Mu_pt600to800_ext1  = Sample.nanoAODfromDAS("QCD_Mu_pt600to800_ext1",     "/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=25.33)
#QCD_Mu_pt800to1000      = Sample.nanoAODfromDAS("QCD_Mu_pt800to1000",         "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.715)
#QCD_Mu_pt800to1000_ext1 = Sample.nanoAODfromDAS("QCD_Mu_pt800to1000_ext1",    "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.715)
#QCD_Mu_pt1000toInf      = Sample.nanoAODfromDAS("QCD_Mu_pt1000toInf",         "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.605)
#QCD_Mu_pt1000toInf_ext1 = Sample.nanoAODfromDAS("QCD_Mu_pt1000toInf_ext1",    "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.605)
#
#
#QCD_Ele_pt20to30        = Sample.nanoAODfromDAS("QCD_Ele_pt20to30",           "/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5533000.0)
#QCD_Ele_pt30to50        = Sample.nanoAODfromDAS("QCD_Ele_pt30to50",           "/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=9928000.0)
#QCD_Ele_pt30to50_ext1   = Sample.nanoAODfromDAS("QCD_Ele_pt30to50_ext1",      "/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v4-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=9928000.0)
#QCD_Ele_pt50to80        = Sample.nanoAODfromDAS("QCD_Ele_pt50to80",           "/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2890800.0)
#QCD_Ele_pt50to80_ext1   = Sample.nanoAODfromDAS("QCD_Ele_pt50to80_ext1",      "/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2890800.0)
#QCD_Ele_pt80to120       = Sample.nanoAODfromDAS("QCD_Ele_pt80to120",          "/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=415400.0)
#QCD_Ele_pt80to120_ext1  = Sample.nanoAODfromDAS("QCD_Ele_pt80to120_ext1",     "/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=415400.0)
#QCD_Ele_pt120to170      = Sample.nanoAODfromDAS("QCD_Ele_pt120to170",         "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=75820.0)
#QCD_Ele_pt120to170_ext1 = Sample.nanoAODfromDAS("QCD_Ele_pt120to170_ext1",    "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=75820.0)
#QCD_Ele_pt170to300      = Sample.nanoAODfromDAS("QCD_Ele_pt170to300",         "/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=18860.0)
#QCD_Ele_pt300toInf      = Sample.nanoAODfromDAS("QCD_Ele_pt300toInf",         "/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1210.0)
#
#QCD = [
#        QCD_Mu_pt15to20,
#        QCD_Mu_pt20to30,
#        QCD_Mu_pt30to50,
#        QCD_Mu_pt50to80,
#        QCD_Mu_pt80to120,
#        QCD_Mu_pt80to120_ext1,
#        QCD_Mu_pt120to170,
#        QCD_Mu_pt170to300,
#        QCD_Mu_pt170to300_ext1,
#        QCD_Mu_pt300to470,
#        QCD_Mu_pt300to470_ext1,
#        QCD_Mu_pt470to600,
#        QCD_Mu_pt470to600_ext1,
#        QCD_Mu_pt600to800,
#        QCD_Mu_pt600to800_ext1,
#        QCD_Mu_pt800to1000,
#        QCD_Mu_pt800to1000_ext1,
#        QCD_Mu_pt1000toInf,
#        QCD_Mu_pt1000toInf_ext1,
#
#        QCD_Ele_pt20to30,
#        QCD_Ele_pt30to50,
#        QCD_Ele_pt30to50_ext1,
#        QCD_Ele_pt50to80,
#        QCD_Ele_pt50to80_ext1,
#        QCD_Ele_pt80to120,
#        QCD_Ele_pt80to120_ext1,
#        QCD_Ele_pt120to170,
#        QCD_Ele_pt120to170_ext1,
#        QCD_Ele_pt170to300,
#        QCD_Ele_pt300toInf,
#]
#
#GJets_HT40to100        = Sample.nanoAODfromDAS("GJets_HT40to100",      "/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=20730)
#GJets_HT40to100_ext    = Sample.nanoAODfromDAS("GJets_HT40to100_ext",  "/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=20730)
#GJets_HT100to200       = Sample.nanoAODfromDAS("GJets_HT100to200",     "/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=9226)
#GJets_HT100to200_ext   = Sample.nanoAODfromDAS("GJets_HT100to200_ext", "/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=9226)
#GJets_HT200to400       = Sample.nanoAODfromDAS("GJets_HT200to400",     "/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2300)
#GJets_HT200to400_ext   = Sample.nanoAODfromDAS("GJets_HT200to200_ext", "/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2300)
#GJets_HT400to600       = Sample.nanoAODfromDAS("GJets_HT400to600",     "/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=274.4)
#GJets_HT400to600_ext   = Sample.nanoAODfromDAS("GJets_HT400to600_ext", "/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=274.4)
#GJets_HT600toInf       = Sample.nanoAODfromDAS("GJets_HT600toInf",     "/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v2-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=93.38)
#GJets_HT600toInf_ext   = Sample.nanoAODfromDAS("GJets_HT600toInf_ext", "/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/llechner-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=93.38)
#
#GJetsHT = [
#           GJets_HT40to100,
#           GJets_HT40to100_ext,
#           GJets_HT100to200,
#           GJets_HT100to200_ext,
#           GJets_HT200to400,
#           GJets_HT200to400_ext,
#           GJets_HT400to600,
#           GJets_HT400to600_ext,
#           GJets_HT600toInf,
#           GJets_HT600toInf_ext,
#]
#
#other = [
#    ]
#
#
##SMS_T2tt_mStop_150to250     = Sample.nanoAODfromDAS("SMS_T2tt_mStop_150to250",     "/SMS-T2tt_mStop-150to250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-2fd0700da493b12a64ddbf2abc06aaaa/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
##SMS_T2tt_mStop_250to350     = Sample.nanoAODfromDAS("SMS_T2tt_mStop_250to350",     "/SMS-T2tt_mStop-250to350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-2fd0700da493b12a64ddbf2abc06aaaa/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
##SMS_T2tt_mStop_350to400     = Sample.nanoAODfromDAS("SMS_T2tt_mStop_350to400",     "/SMS-T2tt_mStop-350to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-2fd0700da493b12a64ddbf2abc06aaaa/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
##SMS_T2tt_mStop_400to1200    = Sample.nanoAODfromDAS("SMS_T2tt_mStop_400to1200",    "/SMS-T2tt_mStop-400to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v3-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#
#SMS_T2tt_mStop_150to250     = Sample.nanoAODfromDAS("SMS_T2tt_mStop_150to250",     "/SMS-T2tt_mStop-150to250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_250to350     = Sample.nanoAODfromDAS("SMS_T2tt_mStop_250to350",     "/SMS-T2tt_mStop-250to350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_350to400     = Sample.nanoAODfromDAS("SMS_T2tt_mStop_350to400",     "/SMS-T2tt_mStop-350to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_400to1200    = Sample.nanoAODfromDAS("SMS_T2tt_mStop_400to1200",    "/SMS-T2tt_mStop-400to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_1200to2000   = Sample.nanoAODfromDAS("SMS_T2tt_mStop_1200to2000",   "/SMS-T2tt_mStop-1200to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#
#SMS_T2bW                    = Sample.nanoAODfromDAS("SMS_T2bW",                        "/SMS-T2bW_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#
#SMS_T8bbllnunu_XCha0p5_XSlep0p05 = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p05", "/SMS-T8bbllnunu_XCha0p5_XSlep0p05_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000 = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000", "/SMS-T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#
#SMS_T8bbllnunu_XCha0p5_XSlep0p5 = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p5", "/SMS-T8bbllnunu_XCha0p5_XSlep0p5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v6-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300 = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300", "/SMS-T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T8bbllnunu_XCha0p5_XSlep0p95 = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p95", "/SMS-T8bbllnunu_XCha0p5_XSlep0p95_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600 = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600", "/SMS-T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-03876b29d9629691244bd3d116a73f21/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#
#SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25 = Sample.nanoAODfromDAS("SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25",     "/SMS-T8bbstausnu_XCha0p5_mStop-200to1800_XStau0p25_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-03876b29d9629691244bd3d116a73f21/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
#
#SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5 = Sample.nanoAODfromDAS("SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5",     "/SMS-T8bbstausnu_mStop-200to1800_XCha0p5_XStau0p5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-03876b29d9629691244bd3d116a73f21/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
#
#SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p75 = Sample.nanoAODfromDAS("SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p75",     "/SMS-T8bbstausnu_mStop-200to1800_XCha0p5_XStau0p75_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-03876b29d9629691244bd3d116a73f21/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
#
#SMS_T2tt_mStop_150_mLSP_50  = Sample.nanoAODfromDAS("SMS_T2tt_mStop_150_mLSP_50",   "/SMS-T2tt_3J_xqcut-20_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_175_mLSP_1   = Sample.nanoAODfromDAS("SMS_T2tt_mStop_175_mLSP_1",    "/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_corridor_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_200_mLSP_50  = Sample.nanoAODfromDAS("SMS_T2tt_mStop_200_mLSP_50",   "/SMS-T2tt_3J_xqcut-20_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_225_mLSP_50  = Sample.nanoAODfromDAS("SMS_T2tt_mStop_225_mLSP_50",   "/SMS-T2tt_3J_xqcut-20_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_250_mLSP_50  = Sample.nanoAODfromDAS("SMS_T2tt_mStop_250_mLSP_50",   "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_250_mLSP_75  = Sample.nanoAODfromDAS("SMS_T2tt_mStop_250_mLSP_75",   "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-75_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_corridor_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.) 
#SMS_T2tt_mStop_250_mLSP_150 = Sample.nanoAODfromDAS("SMS_T2tt_mStop_250_mLSP_150",  "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_300_mLSP_150 = Sample.nanoAODfromDAS("SMS_T2tt_mStop_300_mLSP_150",  "/SMS-T2tt_3J_xqcut-20_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_325_mLSP_150 = Sample.nanoAODfromDAS("SMS_T2tt_mStop_325_mLSP_150",  "/SMS-T2tt_3J_xqcut-20_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_350_mLSP_150 = Sample.nanoAODfromDAS("SMS_T2tt_mStop_350_mLSP_150",  "/SMS-T2tt_3J_xqcut-20_mStop-350_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#
#SMS_T2tt_mStop_650_mLSP_350 = Sample.nanoAODfromDAS("SMS_T2tt_mStop_650_mLSP_350", "/SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#SMS_T2tt_mStop_850_mLSP_100 = Sample.nanoAODfromDAS("SMS_T2tt_mStop_850_mLSP_100", "/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v4-b4020277631f1d9d0f34f5be03518e3c/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#
#SMS_T2tt_dM_10to80          = Sample.nanoAODfromDAS("SMS_T2tt_dM_10to80", "/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/prhussai-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_v0-23775f5a395d6e9cdb45e128e602f3b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
#
#SUSY = [
#    SMS_T2tt_mStop_150to250,
#    SMS_T2tt_mStop_250to350,
#    SMS_T2tt_mStop_350to400,
#    SMS_T2tt_mStop_400to1200,
#    SMS_T2tt_mStop_1200to2000,
#    SMS_T2bW,
#    # FullSim points for corridor
#    SMS_T2tt_mStop_150_mLSP_50,
#    SMS_T2tt_mStop_175_mLSP_1,
#    SMS_T2tt_mStop_200_mLSP_50,
#    SMS_T2tt_mStop_225_mLSP_50,
#    SMS_T2tt_mStop_250_mLSP_50,
#    SMS_T2tt_mStop_250_mLSP_75,
#    SMS_T2tt_mStop_250_mLSP_150,
#    SMS_T2tt_mStop_300_mLSP_150,
#    SMS_T2tt_mStop_325_mLSP_150,
#    SMS_T2tt_mStop_350_mLSP_150,
#    SMS_T2tt_mStop_650_mLSP_350,
#    SMS_T2tt_mStop_850_mLSP_100,
#
#    # T8
#    SMS_T8bbllnunu_XCha0p5_XSlep0p05,
#    SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000,
#    SMS_T8bbllnunu_XCha0p5_XSlep0p5,
#    SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300,
#    SMS_T8bbllnunu_XCha0p5_XSlep0p95,
#    SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600,
#    SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25,
#    SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5,
#    SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p75
#    ]
#compSUSY = [SMS_T2tt_dM_10to80]
#
#### v7
#TTbarDMJets_Dilepton_scalar         = Sample.nanoAODfromDAS("TTbarDMJets_Dilepton_scalar",    "/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_rp_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v7-0715d40ac32fba3ea0bb6d089cced1b5/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
#TTbarDMJets_Dilepton_pseudoscalar   = Sample.nanoAODfromDAS("TTbarDMJets_Dilepton_pseudoscalar",    "/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_rp_94X_mcRun2_asymptotic_v3-v1_legacy_nano_v7-0715d40ac32fba3ea0bb6d089cced1b5/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
#
#ttDM = [ TTbarDMJets_Dilepton_scalar, TTbarDMJets_Dilepton_pseudoscalar ]
#
#allSamples = DY + top + boson + wjets + rare + other + signals + gluglu + QCD + GJetsHT + SUSY + compSUSY + ttDM


allSamples = DY + top #+ boson + wjets + rare + other + signals + gluglu + QCD + GJetsHT + SUSY + compSUSY + ttDM
for s in allSamples:
    s.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 )

