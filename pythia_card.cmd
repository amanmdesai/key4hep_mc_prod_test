! File: lhe2pythia.cmnd
Random:setSeed = on
Random:seed = 34188
Main:timesAllowErrors = 10 ! how many aborts before run stops
Main:numberOfEvents = 1000000 ! number of events to generate
! 2) Settings related to output in init(), next() and stat().
Next:numberCount = 100 ! print message every n events
!Beams:idA = 11 ! first beam, e+ = 11
!Beams:idB = -11 ! second beam, e- = -11
Beams:frameType = 4 ! read info from a LHEF
! Change the LHE file here
Beams:LHEF = background_qq.lhe
! 3) Settings for the event generation process in the Pythia8 library.
PartonLevel:ISR = on ! initial-state radiation
PartonLevel:FSR = on ! final-state radiation
