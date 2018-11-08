import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/00356662-4159-E811-895C-F8BC1234F308.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/00CBE937-E359-E811-B4B3-0CC47AD99112.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/08CD7BE6-0A5B-E811-B89C-00238BCE4634.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/0A755464-CE5A-E811-BE9C-0CC47A78A3F8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/14A06120-EF63-E811-A7DE-0CC47A4D7668.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/165BB807-C263-E811-BE72-782BCB530522.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/1C2EF645-7259-E811-8CF4-141877343E6D.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/1CF321BC-465A-E811-A2CF-0CC47A4D760A.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/1EF6C9F2-2D5D-E811-9D2A-1C6A7A263523.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/284BDD24-055A-E811-B092-1866DAEEB344.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/2EDD3B2E-945C-E811-9F00-0CC47A4D762A.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/384FE2BD-C159-E811-A278-0CC47A2B04A6.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/38CD9C98-2B5A-E811-8528-0CC47A7C354C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/3C13D386-675A-E811-8554-24BE05C33C71.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/3C55942E-FB66-E811-8781-00000086FE80.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/3E946B55-4C59-E811-A748-549F3525AE58.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/442C2F23-6264-E811-850F-90B11C0BCBD6.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/44E7401B-EF58-E811-8224-141877343E6D.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/46546FF5-1C59-E811-9F11-1866DAEECFDC.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/4EEE51D6-785B-E811-BB35-0CC47A78A3EC.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/52F269BC-BA59-E811-AB07-549F3525CD78.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/58052E88-065B-E811-9395-0CC47A78A3EC.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/581AA696-FB5B-E811-ADFA-0CC47A7C34C4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/5E76C37A-0B66-E811-8F2A-1866DAEA6D0C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/6A357A29-055A-E811-8C36-008CFA111184.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/6C5A10FA-2D5D-E811-87FD-0025907D24F0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/70AD07DE-2D5D-E811-90A0-24BE05C618F1.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/72A1CE63-FD59-E811-8649-0CC47AA98A3A.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/74999724-2F59-E811-8DE4-E0071B7A6640.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/781DDC9C-2465-E811-A032-1866DAEB3370.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/848B4324-625A-E811-9321-F01FAFD6996C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/86C33B6E-6959-E811-8B35-B083FED18B9F.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/8A52D803-C259-E811-8032-1866DA85DC87.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/8A90686B-185A-E811-9262-1866DAEA7F94.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/8AC524AE-8A59-E811-838D-842B2B61B187.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/8E953B86-7C59-E811-AD8E-1866DAEA7EA8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/94259E71-375B-E811-BFDC-A4BADB3E940F.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/943BD487-2D5D-E811-BB9C-782BCB3BCED2.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/94CEA7FE-1C59-E811-863B-24BE05C48821.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/961A7C25-EC59-E811-8621-B083FED42ECF.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/96697F1D-8459-E811-9425-B083FED42FC3.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/9AAEF25B-2667-E811-8DAA-0CC47A4D7646.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/A8723EF4-DC59-E811-A625-801844E561C0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/B07C0497-5359-E811-B518-1866DAEA8190.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/B487DD2B-DA5A-E811-8A83-1866DAEA6520.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/BAAA6815-4C5A-E811-8DFE-B083FED42FAF.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/BAEB1F81-7F59-E811-994B-EC0D9A8221EE.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/BE989D7C-135A-E811-8190-A0369F310374.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/C2DAB47E-CB5B-E811-A7C6-0CC47A78A42C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/C43511F6-B059-E811-8CA7-E0071B749C80.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/C4C55A3E-A359-E811-A016-549F3525AE18.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/CA83EF76-5859-E811-ADB0-E0071B73C650.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/CEED7027-5E59-E811-B7F7-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/D24414DD-2B5A-E811-BB7E-E0071B7A9810.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/DE38CDBF-F963-E811-99DC-24BE05CEEB81.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/E20E4F60-0F5C-E811-8EC8-842B2B42D35B.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/E21C19C4-755A-E811-89E3-0CC47A4C8F2C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/E2820094-EB58-E811-A778-A0369F301924.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/E2FDF460-255B-E811-B9F9-24BE05CE1E11.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/E8BACEF7-325B-E811-B5C5-0CC47A7C357A.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/ECC65553-F659-E811-8F00-A0369F310374.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/EE58C019-B959-E811-A77C-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/EE8F8AF7-2667-E811-AFB1-549F3525C380.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/F09FC848-7559-E811-A614-00259048BBCA.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/F2A3D318-1B5A-E811-B274-003048F5B2A0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/F2EC6CE9-2D5D-E811-9B63-141877410B4D.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/FA31252E-2459-E811-9FD5-90B11C0BD466.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/FA72FA7A-EC5A-E811-B9F5-0CC47A7C3604.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/100000/FCAF4BED-2D5D-E811-95FD-008CFAC91948.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/007D55BF-5259-E811-B7C4-24BE05C63681.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/024FB389-E55B-E811-A910-0CC47A0AD6E4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/06DDF3B5-315C-E811-AA50-1866DAEEB364.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/0C104B71-CD5B-E811-B6D9-549F3525AE58.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/0C200A14-2B5A-E811-8880-0242AC130003.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/12FA8334-9859-E811-A565-EC0D9A8225FE.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/18E3AFBB-585B-E811-B53C-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/2023F3EC-3E59-E811-BB0D-E0071B73B6C0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/2025DD9F-C759-E811-993D-1866DAEA79A4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/242CA111-715B-E811-A9BF-0CC47A74527A.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/24E32255-B059-E811-B9E8-0CC47A6C1038.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/2AFA0F2E-2C5A-E811-9BB8-0CC47AA992C8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/2E22AFD6-C15A-E811-96F3-0CC47A4D76AA.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/2E8394D1-065C-E811-BFF2-E0071B7A7870.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/30F0967D-F35B-E811-BEB0-0025905488FC.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/3618EFDA-CF5A-E811-A1E6-549F3525CD78.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/362584C4-235D-E811-B30F-0CC47AD99112.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/44989CDA-E85B-E811-97E6-0025905A6070.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/46202CC6-245C-E811-85A1-D4AE5264D964.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/481B302B-615A-E811-B4ED-002590491B1C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/48EF0EEC-C75C-E811-9E3F-0025905A48B2.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/4C3CDBCB-225A-E811-B248-0025901D0C4E.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/4E1F74F7-915A-E811-B554-0CC47A7C354A.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/50FA343A-8A63-E811-8E09-0CC47AA53D72.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/5238DA87-E359-E811-A66D-00000086FE80.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/525928B8-4D5A-E811-9E76-0025905AA9CC.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/52B2CC37-7D5D-E811-BC93-00259055C876.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/54E7EC5D-F959-E811-AFE2-002590E3A0EE.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/5882EE18-005C-E811-8B08-1866DAEA7E64.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/5A029959-9F59-E811-B158-5065F3810301.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/5A92F6AE-1E5B-E811-A624-842B2B1807B0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/5C6E362A-FF59-E811-872B-90B11C2CB7A9.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/5E9AB33B-0A5B-E811-B176-1866DAEA79C8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/6418DAA5-535C-E811-BF50-0025905A48BA.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/6ED69D55-D459-E811-A7C0-0CC47A6C138A.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/7A3F1BE6-FE5B-E811-9EEF-0CC47A4D764C.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/7A721050-455B-E811-BAF7-24BE05CEDC81.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/80C26203-805B-E811-8346-1866DAEA8218.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/825E6666-765B-E811-BDEA-0CC47A78A414.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/8689F6E5-FB5A-E811-B89B-0025905A60AA.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/86FDBDDA-3659-E811-8E8E-4C79BA180D0B.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/8A7E7D17-0F5A-E811-A7CD-E0071B745DC0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/8AF42545-1C5B-E811-AC51-782BCB38FF63.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/94E86410-655A-E811-8442-E0071B73C620.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/94EDF3A6-8A5A-E811-911E-E0071B693B41.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/9A47537D-4A5A-E811-9B6C-002590E3A0EE.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/9EC3653C-7D5D-E811-A4D4-90B11C444042.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/A206543A-BC59-E811-B9C6-5065F381C251.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/A2F0268C-AB5B-E811-8098-0025905A6088.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/A82F92B9-E25A-E811-9694-E0071B745DC0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/A8B1653A-7D5D-E811-905A-1866DAEA7A40.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/ACB7DA8B-505A-E811-B11A-003048F7CC8A.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/AE32FD19-555A-E811-9F1A-5065F3812271.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/B2919F69-455B-E811-BA8B-B083FED42FE3.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/B44FC4DC-7C5D-E811-8094-FA163E8C1AD1.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/B476554A-6059-E811-A3F9-EC0D9A82264E.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/B60F9A84-3D5D-E811-8E65-4C79BA180945.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/B6BCC92C-9A5D-E811-BFCE-0025907859C4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/BA6C4155-125A-E811-B777-1866DAEA7E28.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/C013EFD1-C15A-E811-BE43-141877411970.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/C405FCE0-1A59-E811-9CC7-E0071B6C9DD0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/C4BE7B4D-5A5B-E811-AFCE-0CC47A7452D0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/C66E1787-A65A-E811-862E-0CC47A4C8EE8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/CE6A3C30-5D59-E811-8004-24BE05C616E1.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/CEE380E6-7559-E811-863D-EC0D9A80980A.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/D6E7B832-7D5D-E811-AFC2-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/D8455495-095A-E811-BBFE-B083FED3F2E8.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/E2D808A9-C759-E811-AEE8-002590E2DD10.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/E473E9EE-EF59-E811-9DE1-0CC47AD98D00.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/E89D31E5-EF5B-E811-AE21-24BE05C63651.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/EA2A6435-3F5A-E811-B432-E0071B7901F1.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/F066D92C-4A5A-E811-A5CC-141877411C7F.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/F44F2FDA-3A5B-E811-A65C-0CC47A4D7630.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/F4CDB2B5-E55A-E811-B591-0CC47AD99062.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/F4F3A5C5-8D5C-E811-8377-002590FD5A78.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/F6120DC1-FD59-E811-BAAB-B083FED42FE3.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/FE40BD5C-5D5A-E811-B2E6-801844DEF0E0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/FE8A7CA5-8959-E811-90D8-24BE05CEADD1.root',
] )
