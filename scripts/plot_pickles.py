import numpy as np
import sys
import pylab
import cPickle


filename = sys.argv[1]

def load_cpickle(filename):
    f = open(filename,"rb")
    p = cPickle.load(f)
    f.close()
    return p


cpickle_data = load_cpickle(filename)
#cpickle_data["E_native"] = E_native
#cpickle_data["E_non_native"] = E_non_native
#cpickle_data["rmsd_native"] = rmsd_native
#cpickle_data["rmsd_non_native"] = rmsd_non_native
#cpickle_data["E_cam"] = E_cam
#cpickle_data["basilisk"] = basilisk
#cpickle_data["backbone_dbn"] = backbone_dbn
#cpickle_data["eh"] = eh
#cpickle_data["mumu"] = mumu
#cpickle_data["rmsds"] = rmsds
#cpickle_data["opls"] = opls
#cpickle_data["profasi"] = profasi
#cpickle_data["custom"] = custom


#print dict((i,low_E_rmsd_index.count(i)) for i in low_E_rmsd_index)
    
print "Making Plots" 

pylab.plot(cpickle_data["rmsd_native"],cpickle_data["E_native"],"r.")
pylab.plot(cpickle_data["rmsd_non_native"],cpickle_data["E_non_native"],"k.")
pylab.savefig("total_energy.png")
pylab.clf()
#
pylab.plot(cpickle_data["rmsd_native"],cpickle_data["E_native"],"r.")
pylab.plot(cpickle_data["rmsd_non_native"],cpickle_data["E_non_native"],"k.")
pylab.xlim([0.2,4.1])
pylab.savefig("total_low_energy.png")
pylab.clf()

pylab.plot(cpickle_data["rmsds"],cpickle_data["custom"],"k.")
pylab.savefig("custom.png")
pylab.clf()

pylab.plot(cpickle_data["rmsds"],cpickle_data["E_cam"],"k.")
#pylab.xlim([0.0,5.0])
pylab.savefig("cam.png")
pylab.clf()

#pylab.plot(rmsds,kbp_profasi_sidechain_charge_improved,"k.")
#pylab.savefig("kbp_profasi_sidechain_charge_improved.png")
#pylab.clf()
#
#pylab.plot(rmsds,kbp_profasi_hydrophobicity_improved,"k.")
#pylab.savefig("kbp_profasi_hydrophobicity_improved.png")
#pylab.clf()
#
pylab.plot(cpickle_data["rmsds"],cpickle_data["mumu"],"k.")
pylab.savefig("mumu.png")
pylab.clf()

#pylab.plot(rmsds,E_all,"k.")
#pylab.savefig("all.png")
#pylab.clf()
#
pylab.plot(cpickle_data["rmsds"],cpickle_data["profasi"],"k.")
pylab.savefig("profasi.png")
pylab.clf()

pylab.plot(cpickle_data["rmsds"],cpickle_data["opls"],"k.")
pylab.savefig("opls.png")
pylab.clf()
#
#pylab.plot(rmsds,opls_charge,"k.")
#pylab.savefig("opls_charge.png")
#pylab.clf()
#
#pylab.plot(rmsds,opls_vdw,"k.")
#pylab.savefig("opls_vdw.png")
#pylab.clf()
#
#pylab.plot(rmsds,opls_angle_bend,"k.")
#pylab.savefig("opls_angle_bend.png")
#pylab.clf()
#
#pylab.plot(rmsds,opls_torsion,"k.")
#pylab.savefig("opls_torsion.png")
#pylab.clf()
#
#pylab.plot(rmsds,opls_improper_torsion,"k.")
#pylab.savefig("opls_improper_torsion.png")
#pylab.clf()
#
#pylab.plot(rmsds,opls_bond_stretch,"k.")
#pylab.savefig("opls_bond_stretch.png")
#pylab.clf()
#
#pylab.plot(rmsds,opls_non_bonded,"k.")
#pylab.savefig("opls_non_bonded.png")
#pylab.clf()
#
#pylab.plot(rmsds,gbsa,"k.")
#pylab.savefig("gbsa.png")
#pylab.clf()
#
#pylab.plot(rmsds,profasi_local,"k.")
#pylab.savefig("profasi_local.png")
#pylab.clf()
#
#pylab.plot(rmsds,profasi_local_sidechain,"k.")
#pylab.savefig("profasi_local_sidechain.png")
#pylab.clf()
#
#pylab.plot(rmsds,profasi_excluded_volume,"k.")
#pylab.savefig("profasi_excluded_volume.png")
#pylab.clf()
#
#pylab.plot(rmsds,profasi_excluded_volume_local,"k.")
#pylab.savefig("profasi_excluded_volume_local.png")
#pylab.clf()
#
#pylab.plot(rmsds,profasi_hydrogen_bond,"k.")
#pylab.savefig("profasi_hydrogen_bond.png")
#pylab.clf()
#
#pylab.plot(rmsds,profasi_hydrophobicity,"k.")
#pylab.savefig("profasi_hydrophobicity.png")
#pylab.clf()
#
#pylab.plot(rmsds,profasi_sidechain_charge,"k.")
#pylab.savefig("profasi_sidechain_charge.png")
#pylab.clf()
#
#pylab.plot(rmsds,profasi_proline_phi_torsion,"k.")
#pylab.savefig("profasi_proline_phi_torsion.png")
#pylab.clf()
#
pylab.plot(cpickle_data["rmsds"],cpickle_data["basilisk"],"k.")
pylab.savefig("basilisk.png")
pylab.clf()
#
pylab.plot(cpickle_data["rmsds"],cpickle_data["backbone_dbn"],"k.")
pylab.savefig("backbone_dbn.png")
pylab.clf()
#
pylab.plot(cpickle_data["rmsds"],cpickle_data["eh"],"k.")
#pylab.ylim(-200,-700)
pylab.savefig("eh.png")
pylab.clf()

print "calculating rmsds"
lowest_energies = [9999999 for _ in range(255)]
low_E_rmsds = [99999 for _ in range(255)]
low_E_rmsd_index = [99999 for _ in range(255)]

for i, profasi_i in enumerate(cpickle_data["profasi"]):
    energies = []
    names = ["custom","E_cam", "opls", "basilisk", "backbone_dbn", "eh", "mumu", "profasi"]
    combinations = [cpickle_data[x][i] for x in names]
    combination_names = []
    for ja in range(8):
        energies.append(combinations[ja])
        combination_names.append(names[ja])
        for jb in range(8):
            if jb > ja:
                energies.append(combinations[ja]+combinations[jb])
                combination_names.append(names[ja]+names[jb])
                for jc in range(8):
                    if jc > jb:
                        energies.append(combinations[ja]+combinations[jb]+combinations[jc])
                        combination_names.append(names[ja]+names[jb]+names[jc])
                        for jd in range(8):
                            if jd > jc:
                                energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd])
                                combination_names.append(names[ja]+names[jb]+names[jc]+names[jd])
                                for je in range(8):
                                    if je > jd:
                                        energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je])
                                        combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je])
                                        for jf in range(8):
                                            if jf > je:
                                                energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf])
                                                combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf])
                                                for jg in range(8):
                                                    if jg > jf:
                                                        energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf]+combinations[jg])
                                                        combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf]+names[jg])
                                                        for jh in range(8):
                                                            if jh > jg:
                                                                energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf]+combinations[jg]+combinations[jh])
                                                                combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf]+names[jg]+names[jh])
    for j, E in enumerate(energies):
        if E < lowest_energies[j]:
            lowest_energies[j] = E
            low_E_rmsds[j] = cpickle_data["rmsds"][i]
            low_E_rmsd_index[j] = i
   
for j, J in enumerate(lowest_energies):
    print j, low_E_rmsd_index[j], low_E_rmsds[j], combination_names[j]
