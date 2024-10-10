#!/bin/bash

cd /eos/user/a/aman/test_key4hep
#source /cvmfs/sw.hsf.org/spackages7/key4hep-stack/2023-04-08/x86_64-centos7-gcc11.2.0-opt/urwcv/setup.sh

source /cvmfs/sw.hsf.org/key4hep/setup.sh

mg5_aMC madgraphrun.dat
gunzip -c background_qq/Events/run_01/unweighted_events.lhe.gz > background_qq.lhe
DelphesPythia8_EDM4HEP card_IDEA.tcl edm4hep_IDEA.tcl pythia_card.cmd Samples/background_qq.root
fccanalysis run analysis_stage1.py