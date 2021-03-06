# variables

#variables['bdt'] = {      'name'  : 'VH2j_TMVAReader(Entry$)',# variable name
#                          'range' : (20, -1., 1.),            # variable range
#                          'xaxis' : 'BDT discriminant VH2j',  # x-axis name
#                          'fold'  : 3,                        # 0 = not fold (default), 1 = fold underflow bin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                          'linesToAdd' : ['.L /afs/cern.ch/user/p/piedra/work/VH2jBDT/VH2j_TMVAReader.C+']}

#
# Centrality
#
variables['Ctot'] = {     'name': 'log((abs(2*Lepton_eta[0]-CleanJet_eta[0]-CleanJet_eta[1])+abs(2*Lepton_eta[1]-CleanJet_eta[0]-CleanJet_eta[1]))/detajj)',
                          'range' : (20, -4, 6),
                          'xaxis' : 'Ctot',
                          'fold'  : 3}

variables['jet1_qgl'] = { 'name'  : 'Jet_qgl[0]',
                          'range' : (20, 0., 1.),
                          'xaxis' : 'Quark Gluon likelihood (1^{st} Jet)',
                          'fold'  : 3}

variables['jet2_qgl'] = { 'name'  : 'Jet_qgl[1]',
                          'range' : (20, 0., 1.),
                          'xaxis' : 'Quark Gluon likelihood (2^{nd} Jet)',
                          'fold'  : 3}

variables['detajj'] = {   'name'  : 'detajj',
                          'range' : (40, 0., 4.),
                          'xaxis' : '|#Delta#eta_{jj}|',
                          'fold'  : 0}

variables['detal1j1'] = { 'name'  : 'Lepton_eta[0]-CleanJet_eta[0]',
                          'range' : (40, -4., 4.),
                          'xaxis' : '#Delta#eta_{l1j1}',
                          'fold'  : 0}

          
variables['drjj'] = {     'name'  : 'sqrt(CleanJet_eta[0]*CleanJet_eta[1] + CleanJet_phi[0]*CleanJet_phi[1])',
                         'range' : (30, 0., 5.),
                         'xaxis' : '#DeltaR_{jj}',
                         #'linesToAdd': ['.L $CMSSW_BASE/src/PlotsConfigurations/Configurations/WW/Full2016_v6/extended/drjj.C+'], #if want to use a script
                         'fold'  : 2}
          
          

#variables['detaljmin'] = {'name'  : 'detaljmin(Lepton_eta[0], Lepton_eta[1], CleanJet_eta[0], CleanJet_eta[1])',
#                          'range' : (40, -4., 4.),
#                          'xaxis' : 'min #Delta#eta_{lj}',
#                          'fold'  : 0,
#                          'linesToAdd' : ['.L /afs/cern.ch/work/p/piedra/public/latinos/CMSSW_10_2_15_patch2/src/PlotsConfigurations/Configurations/VH2j/Full2016_v6/detaljmin.C+']}

variables['dphijjmet'] = {'name'  : 'abs(dphijjmet)',     
                          'range' : (20, 0., 3.2),   
                          'xaxis' : '#Delta#phi_{jjmet}',
                          'fold'  : 3}

variables['dphill'] = {   'name'  : 'abs(dphill)',     
                          'range' : (20, 0., 3.2),   
                          'xaxis' : '#Delta#phi_{ll}',
                          'fold'  : 3}

variables['dphillj'] = {  'name'  : 'abs(dphilljet)',     
                          'range' : (20, 0., 3.2),   
                          'xaxis' : '#Delta#phi_{llj}',
                          'fold'  : 3}

variables['dphilljj'] = { 'name'  : 'abs(dphilljetjet)',     
                          'range' : (20, 0., 3.2),   
                          'xaxis' : '#Delta#phi_{lljj}',
                          'fold'  : 3}

variables['drll'] = {     'name'  : 'drll',
                          'range' : (30, 0., 5.),
                          'xaxis' : '#DeltaR_{ll}',
                          'fold'  : 2}

variables['eta1'] = {     'name'  : 'Lepton_eta[0]',     
                          'range' : (40, -3.2, 3.2),   
                          'xaxis' : '#eta 1st lepton',
                          'fold'  : 3}

variables['eta2'] = {     'name'  : 'Lepton_eta[1]',     
                          'range' : (40, -3.2, 3.2),
                          'xaxis' : '#eta 2nd lepton',
                          'fold'  : 3}

variables['events'] = {   'name'  : '1',
                          'range' : (1, 0, 2),
                          'xaxis' : 'events',
                          'fold'  : 3}

variables['jeteta1'] = {  'name'  : 'CleanJet_eta[0]',
                          'range' : (80, -4., 4.),
                          'xaxis' : '#eta 1st jet',
                          'fold'  : 0}

variables['jeteta2'] = {  'name'  : 'CleanJet_eta[1]',
                          'range' : (80, -4., 4.),
                          'xaxis' : '#eta 2nd jet',
                          'fold'  : 0}

variables['jetphi1'] = {  'name'  : 'CleanJet_phi[0]',
                          'range' : (40, -3.2, 3.2),
                          'xaxis' : '#phi 1st jet',
                          'fold'  : 0}

variables['jetphi2'] = {  'name'  : 'CleanJet_phi[1]',
                          'range' : (40, -3.2, 3.2),
                          'xaxis' : '#phi 2nd jet',
                          'fold'  : 0}

variables['jetpt1'] = {   'name'  : 'CleanJet_pt[0]*(CleanJet_pt[0]>30)',     
                          'range' : (40, 30., 190.),   
                          'xaxis' : 'p_{T} 1st jet',
                          'fold'  : 2}

variables['jetpt1_0j'] = {'name'  : 'CleanJet_pt[0]*(CleanJet_pt[0]<30)',     
                          'range' : (30, 0., 30.),   
                          'xaxis' : 'p_{T} 1st jet (p_{T} < 30 GeV) ',
                          'fold'  : 0}

variables['mjj'] = {      'name'  : 'mjj',
                          'range' : (25, 200., 400.),
                          'xaxis' : 'm_{jj} [GeV]',
                          'fold'  : 0}

variables['mll'] = {      'name'  : 'mll',
                          'range' : (8, 0., 200.),
                          'xaxis' : 'm_{ll} [GeV]',
                          'fold'  : 0}

variables['mll10GeV'] = { 'name'  : 'mll',
                          'range' : (20, 0., 200.),
                          'xaxis' : 'm_{ll} [GeV]',
                          'fold'  : 0}

variables['mllpeak'] = {  'name'  : 'mll',
                          'range' : (20, 80., 100.),
                          'xaxis' : 'm_{ll} [GeV]',
                          'fold'  : 0}

variables['mpmet'] = {    'name'  : 'mpmet',      
                          'range' : (50, 0., 150.),  
                          'xaxis' : 'min. (proj. tk. E_{T}^{miss}, proj. E_{T}^{miss}) [GeV]', 
                          'fold'  : 3}

variables['mth'] = {      'name'  : 'mth',
                          'range' : (40, 0., 200.),
                          'xaxis' : 'm_{T}^{H} [GeV]',
                          'fold'  : 0}

variables['njet'] = {     'name'  : 'Sum$(CleanJet_pt>30)',     
                          'range' : (5, 0, 5),   
                          'xaxis' : 'number of jets',
                          'fold'  : 2}

variables['bjet'] = {     'name'  : 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217)',     
                          'range' : (5, 0, 5),   
                          'xaxis' : 'number of jets',
                          'fold'  : 2}

variables['nvtx'] = {     'name'  : 'PV_npvsGood',      
                          'range' : (50, 0, 50),  
                          'xaxis' : 'number of vertices', 
                          'fold'  : 3}

variables['phi1'] = {     'name'  : 'Lepton_phi[0]',
                          'range' : (40, -3.2, 3.2),
                          'xaxis' : '#phi 1st lepton',
                          'fold'  : 3}

variables['phi2'] = {     'name'  : 'Lepton_phi[1]',
                          'range' : (40, -3.2, 3.2),
                          'xaxis' : '#phi 2nd lepton',
                          'fold'  : 3}

variables['pfmet'] = {    'name'  : 'MET_pt',     
                          'range' : (50, 0., 150.),   
                          'xaxis' : 'PF MET [GeV]',
                          'fold'  : 3}

variables['pt1'] = {      'name'  : 'Lepton_pt[0]',     
                          'range' : (40, 0., 200.),   
                          'xaxis' : 'p_{T} 1st lepton [GeV]',
                          'fold'  : 3}

variables['pt2'] = {      'name'  : 'Lepton_pt[1]',     
                          'range' : (40, 0., 200.),   
                          'xaxis' : 'p_{T} 2nd lepton [GeV]',
                          'fold'  : 3}

variables['ptll'] = {     'name'  : 'ptll',
                          'range' : (40, 30., 200.),
                          'xaxis' : 'p_{T}^{ll} [GeV]',
                          'fold'  : 0}

variables['puppimet'] = { 'name'  : 'PuppiMET_pt',
                          'range' : (50, 0., 150.),
                          'xaxis' : 'puppi MET [GeV]',
                          'fold'  : 3}

variables['qgl0'] = {     'name'  : 'Jet_qgl[CleanJet_jetIdx[0]]',
                          'range' : (10, 0., 1.),
                          'xaxis' : '1st jet quark-gluon likelihood',
                          'fold'  : 0}

variables['qgl1'] = {     'name'  : 'Jet_qgl[CleanJet_jetIdx[1]]',
                          'range' : (10, 0., 1.),
                          'xaxis' : '2nd jet quark-gluon likelihood',
                          'fold'  : 0}

variables['rawmet'] = {   'name'  : 'RawMET_pt',     
                          'range' : (50, 0., 150.),   
                          'xaxis' : 'raw MET [GeV]',
                          'fold'  : 3}

variables['TkMET'] = {    'name'  : 'TkMET_pt',     
                          'range' : (50, 0., 150.),   
                          'xaxis' : 'tracker MET [GeV]',
                          'fold'  : 3}

variables['btagDeepB'] = { 'name'  : 'Jet_btagDeepB[CleanJet_jetIdx]',
                          'range' : (25, 0., 1.),
                          'xaxis' : 'Deep B discriminator',
                          'fold'  : 3}

variables['btagCSVv2'] = { 'name'  : 'Jet_btagCSVV2[CleanJet_jetIdx]',
                          'range' : (25, 0., 1.),
                          'xaxis' : 'CSVv2 discriminator',
                          'fold'  : 3}

variables['btagCMVA'] = { 'name'  : 'Jet_btagCMVA[CleanJet_jetIdx]',
                          'range' : (25, -1., 1.),
                          'xaxis' : 'CMVA discriminator',
                          'fold'  : 3}

variables['btagDeepFlavB'] = { 'name'  : 'Jet_btagDeepFlavB[CleanJet_jetIdx]',
                          'range' : (25, 0., 1.),
                          'xaxis' : 'Deep Flavour B discriminator',
                          'fold'  : 3}

variables['ptlljjmet'] = { 'name'  : 'Lepton_pt[0] + Lepton_pt[1] + CleanJet_pt[0] + CleanJet_pt[1] + MET_pt',
                          'range' : (16, 0., 400.),
                          'xaxis' : 'p_{T} leptons+jets+MET',
                          'fold'  : 3}

variables['mlljj'] = {    'name'       : 'mlljj(Lepton_pt[0], Lepton_eta[0], Lepton_phi[0], Lepton_pt[1], Lepton_eta[1], Lepton_phi[1], CleanJet_pt[0], CleanJet_eta[0], CleanJet_phi[0], CleanJet_mass[0], CleanJet_pt[1], CleanJet_eta[1], CleanJet_phi[1], CleanJet_mass[1])',
                          'range'      : (16, 0., 400.),
                          'xaxis'      : 'm_{lljj}',
                          'fold'       : 3,
                          'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/WW/Full2016_v6/mlljj.C++']}



