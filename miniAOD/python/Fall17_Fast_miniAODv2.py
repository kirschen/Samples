'''
miniAOD FastSim samples of Fall17 campaign, miniAODv2 (94X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIIFall17MiniAODv2*Fast*/MINIAODSIM"
'''

from RootTools.fwlite.FWLiteSample import FWLiteSample

## T2tt
SMS_T2tt_mStop_150to250     = FWLiteSample.fromDAS("SMS_T2tt_mStop_150to250"  , "/SMS-T2tt_mStop-150to250_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
SMS_T2tt_mStop_250to350     = FWLiteSample.fromDAS("SMS_T2tt_mStop_250to350"  , "/SMS-T2tt_mStop-250to350_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
SMS_T2tt_mStop_350to400     = FWLiteSample.fromDAS("SMS_T2tt_mStop_350to400"  , "/SMS-T2tt_mStop-350to400_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
SMS_T2tt_mStop_400to1200    = FWLiteSample.fromDAS("SMS_T2tt_mStop_400to1200" , "/SMS-T2tt_mStop-400to1200_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
SMS_T2tt_mStop_1200to2000   = FWLiteSample.fromDAS("SMS_T2tt_mStop_1200to2000", "/SMS-T2tt_mStop-1200to2000_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

T2tt = [
    SMS_T2tt_mStop_150to250  ,
    SMS_T2tt_mStop_250to350  ,
    SMS_T2tt_mStop_350to400  ,
    SMS_T2tt_mStop_400to1200 ,
    SMS_T2tt_mStop_1200to2000,
    ]


## sum up
allSamples = T2tt

