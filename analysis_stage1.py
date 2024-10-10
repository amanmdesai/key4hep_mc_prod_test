inputDir  = "Samples"
outputDir = "stage1"

nCPUS     = 8


processList = {    

    'background_qq': {},
    
}


class RDFanalysis():

    def analysers(df):
        df2 = (
            df
            ## get information about reconstructed particles
            .Define("RP_px",          "ReconstructedParticle::get_px(ReconstructedParticles)")
            .Define("RP_py",          "ReconstructedParticle::get_py(ReconstructedParticles)")
            .Define("RP_pz",          "ReconstructedParticle::get_pz(ReconstructedParticles)")
            .Define("RP_phi",          "ReconstructedParticle::get_phi(ReconstructedParticles)")
            .Define("RP_e",           "ReconstructedParticle::get_e(ReconstructedParticles)")
            .Define("RP_m",           "ReconstructedParticle::get_mass(ReconstructedParticles)")
            .Define("RP_q",           "ReconstructedParticle::get_charge(ReconstructedParticles)")


            .Define("MissingP", "ReconstructedParticle::get_p(MissingET)") 

            .Define("pseudo_jets",    "JetClusteringUtils::set_pseudoJets(RP_px, RP_py, RP_pz, RP_e)")

            .Define("FCCAnalysesJets_eekt", "JetClustering::clustering_ee_kt(2, 2, 1, 0)(pseudo_jets)")
            .Define("jets_eekt",           "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_eekt)")

            .Define("jet_e",        "JetClusteringUtils::get_e(jets_eekt)")
            .Define("jet_p",        "JetClusteringUtils::get_p(jets_eekt)")
            .Define("jet_theta",        "JetClusteringUtils::get_theta(jets_eekt)")
            .Define("jet_phi",        "JetClusteringUtils::get_phi(jets_eekt)")




        )
        return df2


    def output():
        branchList = [


            "jet_e",
            "jet_p",
            "jet_phi",
            "jet_theta",


            "MissingP",



        ]
        return branchList