echo "Running 2016 signal MC"
cmsRun ntuplize_cfg.py channels=zz isMC=1 eCalib=1 muCalib=1 isSync=1 year=2016 genInfo=1 genLeptonType=dressedHPFS eventsToProcess=1:4880:972929,1:4877:972449,1:4544:905999,1:4876:972221,1:1661:331070

#echo "Running 2017 signal MC"
#cmsRun ntuplize_cfg.py channels=zz isMC=1 eCalib=1 muCalib=1 isSync=1 year=2017 eventsToProcess=1:3402:340113,1:2016:201533,1:3456:345548,1:476:47521,1:3481:348047,1:3241:324024,1:2585:258464,1:2041:204036

#echo "Running 2018 signal MC"
#cmsRun ntuplize_cfg.py channels=zz isMC=1 eCalib=1 muCalib=1 isSync=1 year=2018 eventsToProcess=1:4818:2056987
