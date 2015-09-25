import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/584/00000/D4DF072A-855D-E511-B91B-02163E01468C.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/587/00000/560F124D-925D-E511-BC70-02163E011D99.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/629/00000/74234EC1-085F-E511-A016-02163E0134F1.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/630/00000/827EBF7D-5D5F-E511-A2A8-02163E01454A.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/662/00000/2A50C19B-F65E-E511-9BE4-02163E014520.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/672/00000/E6D247AC-F85E-E511-92F4-02163E014237.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/673/00000/E253E1DE-185F-E511-891F-02163E01455C.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/674/00000/1432D688-FB5E-E511-B1BC-02163E0146C0.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/675/00000/22390A97-855F-E511-8E42-02163E0143E9.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/675/00000/4448AC8C-855F-E511-B6D1-02163E0143B6.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/675/00000/6632AE9C-855F-E511-A7BB-02163E011D16.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/675/00000/CE3B008E-855F-E511-A0FD-02163E01410B.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/12A511A8-C55F-E511-A78A-02163E01464C.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/1CEFD917-C65F-E511-8EF9-02163E014294.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/20A31E3A-C55F-E511-9D4F-02163E0124FF.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/42FB9FB1-C55F-E511-9546-02163E017131.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/464AB5D5-C55F-E511-AB4D-02163E0143A6.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/6C4DF04E-C55F-E511-8438-02163E012187.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/800647D0-C55F-E511-BD2E-02163E013892.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/84DDD6D3-C55F-E511-80E9-02163E014496.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/8AC99519-C55F-E511-AEA7-02163E0143E6.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/A29107D1-C55F-E511-BAFD-02163E0146F5.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/A2D091DA-C55F-E511-9ECE-02163E0128A6.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/DEC0F5D1-C55F-E511-A64F-02163E011F9B.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/E28603D7-C55F-E511-9366-02163E011D48.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/E6FC61D6-C55F-E511-88D2-02163E011BE0.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/E8A2AFD1-C55F-E511-84D5-02163E012057.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/F8EF630C-C55F-E511-8A33-02163E0145D4.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/FC4615E4-C75F-E511-B82C-02163E01430E.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/676/00000/FCAF27F8-C45F-E511-A006-02163E0138B2.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/677/00000/2EC6F8F9-865F-E511-BADD-02163E0120AC.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/677/00000/5CBB2905-875F-E511-B0AF-02163E01346C.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/677/00000/7AEF2502-875F-E511-8C6F-02163E0137BA.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/677/00000/9C593CF1-865F-E511-9198-02163E0135A8.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/677/00000/AC193BFA-865F-E511-A16D-02163E012697.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/677/00000/C85D9413-875F-E511-887C-02163E011EA9.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/677/00000/D0CF47FA-865F-E511-BBD6-02163E011E25.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/721/00000/4C6AFDED-085F-E511-844C-02163E013786.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/725/00000/046153BE-385F-E511-847C-02163E01246B.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/727/00000/DECC5A01-3A5F-E511-ACE3-02163E01464A.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/728/00000/8A63A81B-3F5F-E511-8A28-02163E0128CE.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/02D7A5C2-6760-E511-9FDB-02163E011E7A.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/10235B95-6C60-E511-B2E5-02163E0145CB.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/16BD5B39-6E60-E511-8347-02163E011D99.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/2C323B93-6860-E511-BE7E-02163E0144EA.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/2EBF1E92-4C60-E511-942A-02163E011D99.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/3A90B318-6D60-E511-B099-02163E0143A2.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/722B3E9C-6860-E511-9B57-02163E011D99.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/7A641F79-4B60-E511-9943-02163E0137F5.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/80D06D45-6E60-E511-81C5-02163E013425.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/8A4E716F-7760-E511-915E-02163E014421.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/8E066DF7-9160-E511-83BB-02163E013966.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/90B1FB83-4C60-E511-82D9-02163E011942.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/90C46598-6A60-E511-9A0C-02163E011E7A.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/9AE2E691-6860-E511-8C90-02163E01447D.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/9ED00039-7460-E511-B6D4-02163E011E10.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/A0A97E4C-6C60-E511-AD57-02163E011942.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/AE6EFE4E-6C60-E511-AD59-02163E013745.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/B20A9D25-6660-E511-BCA8-02163E01463F.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/B291A07A-7260-E511-97DE-02163E01265F.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/B4EB8052-6D60-E511-88FA-02163E014265.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/B6579FAF-6A60-E511-8705-02163E014792.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/BE932A26-6660-E511-8D26-02163E01385B.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/C61E367A-4B60-E511-BE7D-02163E01447D.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/CE1386C0-6760-E511-A0A4-02163E0145DA.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/D6417390-4C60-E511-8AB2-02163E014173.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/729/00000/E2478144-6E60-E511-919F-02163E0137C1.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/734/00000/5A473EEF-8960-E511-A685-02163E014279.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/734/00000/A8E5CDB1-7860-E511-BC44-02163E0132AD.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/734/00000/AAAD9764-6960-E511-ACCE-02163E011C91.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/734/00000/ACFE886E-7A60-E511-9A4F-02163E012095.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/798/00000/100F8828-B25F-E511-BB1A-02163E011A7D.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/801/00000/0871F07B-5560-E511-B8D2-02163E012096.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/801/00000/947DC17B-5560-E511-8366-02163E011E10.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/801/00000/B867317B-5560-E511-915D-02163E0137FA.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/801/00000/FC2FE37B-5560-E511-B977-02163E012096.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/834/00000/8665FC13-0360-E511-B419-02163E011A9B.root',
       '/store/data/Run2015D/DoubleEG/MINIAOD/PromptReco-v3/000/256/842/00000/582996FA-5060-E511-9DED-02163E011B5E.root' ] );


secFiles.extend( [
               ] )
