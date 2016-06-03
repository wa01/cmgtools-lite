#-------- SAMPLES AND TRIGGERS -----------
#from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *
from CMGTools.RootTools.samples.samples_13TeV_RunIISpring16MiniAODv2 import *
from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *
from CMGTools.RootTools.samples.triggers_13TeV_Spring15 import *
from CMGTools.RootTools.samples.triggers_13TeV_Spring15_1l import *

##applying the correct json files to PrompReco and July17 samples
for sample in dataSamples_Run2016B:
  sample.json = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-273730_13TeV_PromptReco_Collisions16_JSON.txt"
#  sample.json = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2_Non17Jul2015.txt"
#  sample.json = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt"
#for sample in dataSamples_17Jul:
##  sample.json = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2_17Jul2015.txt"
#  sample.json = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt"
