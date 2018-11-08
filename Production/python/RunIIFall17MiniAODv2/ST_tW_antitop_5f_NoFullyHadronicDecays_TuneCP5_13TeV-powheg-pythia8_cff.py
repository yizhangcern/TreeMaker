import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/16C80C5F-D942-E811-9810-0025905C2CB8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/281FA8CE-D342-E811-8D12-0025904C637C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/32C4B894-DF42-E811-9842-0025904C51F0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5C19B577-DB42-E811-AEC7-0025904CF93E.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/0A60B3D3-E642-E811-AE35-0CC47AF9B306.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/0C4A77D3-E642-E811-AA38-0025905C431A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/0E8CA028-9D42-E811-A360-0025905C2CA6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/16874F01-9F42-E811-81D9-0CC47A4C8E28.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/3005B40C-EC42-E811-97E2-0025905D1D62.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/4CC07938-9742-E811-995A-0CC47A7C356A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/4EB6C5D4-ED42-E811-8C06-0025905C9742.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/582BE0D3-E642-E811-91C8-0025905D1D60.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/6044AADA-EF42-E811-BD9D-0025905D1CB6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/643DB346-E242-E811-878B-0CC47A74525A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/709F7418-EB42-E811-8F92-0025904C51F0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/72BD88AA-D942-E811-9BDE-0025905C431A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/74555376-A442-E811-9A1E-0CC47A78A436.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/7692B48F-EA42-E811-9788-0025904C6414.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/7C146B81-EC42-E811-9F0D-0025905C53D2.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/8417F9CD-E842-E811-AD28-0025905D1CB6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/968F4247-DD42-E811-993C-0025905C96E8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/96A89E7B-E842-E811-AC5D-0025905C43EC.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/989958C6-E142-E811-B57A-0025905C2CA4.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/9A325279-E542-E811-B74C-0025904C4F52.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/A6177F45-E242-E811-8EC2-0025904C6568.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/C8AEE817-E342-E811-8DD8-0CC47AF9B2C2.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/CCB21BC5-E142-E811-B4CD-0025905D1CB6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/D40B26B7-9342-E811-B0FF-0025905C2C86.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/D813FC44-E242-E811-88F6-0025904C6414.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/DA58D450-E442-E811-8182-0025905C5500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/DE66C3EA-DF42-E811-9D03-0025904C66F0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/DEFF962A-DE42-E811-AA0E-0025905C2CE4.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/E06E5FAF-D442-E811-B888-0025905C42A8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/E6159CC2-0443-E811-8C0B-0025904CF93E.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/EA66784D-E442-E811-8CBF-0025905C9726.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/F067BDAE-9B42-E811-A670-0025905C2C86.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/F82CFDE9-DF42-E811-99D9-0025904C637A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/FAF15A19-EB42-E811-9CEB-0025905C9742.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/FC7FCF4D-E442-E811-B3C8-0025904C6620.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/00A79811-EA43-E811-8214-0025905B857E.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/46580AFA-E343-E811-B4CA-0CC47A4C8E16.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/78509B2A-E443-E811-AF9E-0CC47A4D76AC.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/8E45C1F0-E243-E811-935C-003048FFCBB2.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/9A73EACC-6743-E811-BE40-0025904C66F2.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/9C6A686F-4443-E811-B7CF-0CC47A4D767A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/AAEFFB3A-4343-E811-B2F8-0CC47A4D76B2.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/BA4D12E5-E143-E811-9AFE-0CC47A7452DA.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/CAC421B8-F543-E811-B7F4-0CC47A4C8EE8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D4DF1D55-F643-E811-A625-0CC47A7AB7A0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F45AE432-E443-E811-A144-0025905A611E.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/10CA13F5-F942-E811-99F3-0025904C66E8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/2283956B-F542-E811-A736-0025905C9742.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/26147C4D-FC42-E811-BB8F-0025904C66F6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/30199C73-BB42-E811-8477-0025905BA736.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/34779415-FB42-E811-8BC4-0025905C3E36.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5C142D2A-F742-E811-B8C2-0025904CF710.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/6AFC1281-F142-E811-876E-0025904CF710.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/808A126B-F542-E811-96A3-0025904CDDF8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/84B8A7CD-F842-E811-A6B1-0025905C9742.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/8E503034-FE42-E811-AC82-0CC47AF9B13A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/ACFC8B18-F942-E811-A79F-0025904C66EE.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B8E56C81-F142-E811-AB6B-0025904C68DA.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/BAA766F3-F342-E811-BCEA-0025904C66F0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/C6826DFC-ED42-E811-8DAF-0025905C3D98.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/DA30E6A7-F342-E811-863C-0025904CF710.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/EEA48BE4-F742-E811-80F5-0025904C4F50.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F801985F-F042-E811-8B22-0025904C4F52.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F89BB6E3-B842-E811-8202-0025905C42A8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/0862C2D4-F942-E811-B498-0025905C5484.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/1448CBD6-0143-E811-ADBE-0025904CF93C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/1E022657-9F42-E811-BF5A-0CC47A74525A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/1E994D57-FE42-E811-8F7C-0025905C53D0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/3077B8A7-F842-E811-880C-0025904C6374.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/4847A1E3-A542-E811-A276-0CC47A4C8F30.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/48DAE8D9-FC42-E811-BF53-0025905C94D2.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/58DD52A7-F842-E811-B265-0CC47AF9B2E6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/6480510C-0943-E811-96CE-0CC47AF9B20A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/7012718F-1843-E811-88B5-0CC47A78A426.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/9CFCCFF2-9F42-E811-BF3E-0025905BA734.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/A87A28C0-9542-E811-9D21-0025904C4F9E.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/A8CC05A3-0043-E811-B64A-0025905C53DC.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/ACA5BC1C-A342-E811-BC95-0CC47A4D767A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/B499BAEA-9942-E811-A242-0025905D1E08.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/C27FB822-FC42-E811-BE0F-0CC47AF9B13A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/C8262D8F-FA42-E811-9FE3-0CC47AF9B13A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/C8C98FE4-FE42-E811-A2F3-0025905C94D2.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/D4351445-0643-E811-9073-0025905C431A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/E4C25C15-A142-E811-91F7-0025905C53A4.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/EA156E76-0243-E811-BD7C-003048947BB9.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/EA2286A0-0343-E811-9803-0025904C669C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/F0277C30-9B42-E811-8663-0025905D1E08.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/F8FA5BDD-0A43-E811-B750-0025905C9726.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/FA1E8648-F042-E811-B256-0025905C54FE.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/FA77A01F-FB42-E811-8FCC-0025905D1CAE.root',
] )
