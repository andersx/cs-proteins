import numpy as np
import sys
import pylab
import cPickle


output_filename = sys.argv[1]
filenames = sys.argv[2:]

E_native = []
E_non_native = []
E_all = []
E_all_profasi = []
E_all_opls = []

rmsd_native = []
rmsd_non_native = []

E_cam = []
kbp_profasi_sidechain_charge_improved = []
kbp_profasi_hydrophobicity_improved = []
opls_charge = []
opls_vdw = []
opls_angle_bend = []
opls_torsion = []
opls_improper_torsion = []
opls_bond_stretch = []
opls_non_bonded = []
gbsa = []
profasi_local = []
profasi_local_sidechain = []
profasi_excluded_volume = []
profasi_excluded_volume_local = []
profasi_hydrogen_bond = []
profasi_hydrophobicity = []
profasi_sidechain_charge= []
profasi_proline_phi_torsion= []
basilisk = []
backbone_dbn = []
eh = []
mumu = []
rmsds = []
opls = []
profasi = []
custom = []

for filename in filenames[:]:
    print filename
    #data = np.loadtxt(filename, dtype=np.str)
    data = open(filename, "r").readlines()
    #if filename.split("/")[-1][:6] == "native":
    #    for line in data[1000:]:
    #        i = line.split()
    #        try:
    #            float(i[1]), float(i[-3])
    #        except ValueError:
    #            continue
    #        if float(i[1]) < -3500 or float(i[1]) > 500:
    #            continue
    #        E_native.append(float(i[1]))
    #        rmsd_native.append(float(i[-3]))
    #        #rmsd_native.append(float(i[-1]))
    #    continue
    #else:
    #    for line in data[1:]:
    #        i = line.split()
    #        try:
    #            float(i[1]), float(i[-3])
    #        except (ValueError, IndexError):
    #            continue
    #        if float(i[1]) < -3500 or float(i[1]) > 500:
    #            continue
    #        E_non_native.append(float(i[1]))
    #        rmsd_non_native.append(float(i[-3]))
    #        #rmsd_non_native.append(float(i[-1]))
    #    #print len(rmsd_non_native)*10, min(rmsd_non_native), filename
    #    #rmsd_non_native = []
    #except:
    #    continue
    for line in data[5000:]:
        i = line.split()
        offset = len(i) - 21
        #offset = len(i) - 20
        #if offset < 1:
        #    continue
        try:
            float(i[2]), float(i[8+offset]), i[9+offset], [float(i[x]) for x in range(10+offset,20+offset)]
            [float(j.split(":")[1]) for j in i[9+offset].split(",")]
            if "nan" in line or "inf" in line:
                continue
        except (ValueError, IndexError):
            continue
        rmsds.append(float(i[-3]))
        #custom.append([i[2]])
        E_cam.append(float(i[8+offset]))
        #kbp_profasi_sidechain_charge_improved.append(float(i[4+offset]))
        #kbp_profasi_hydrophobicity_improved.append(float(i[5+offset]))
        #opls_charge = float(i[2+offset])
        #opls_vdw = float(i[3+offset])
        #opls_angle_bend = float(i[4+offset])
        #opls_torsion = float(i[5+offset])
        #opls_improper_torsion = float(i[6+offset])
        #opls_bond_stretch = float(i[7+offset])
        #opls_non_bonded = float(i[8+offset])
        #gbsa = float(i[9+offset])
        #opls.append(opls_charge+opls_vdw+opls_angle_bend+opls_torsion+opls_improper_torsion+opls_bond_stretch+opls_non_bonded+gbsa)
        profasi_local = float(i[10+offset])
        profasi_local_sidechain = float(i[11+offset])
        profasi_excluded_volume = float(i[12+offset])
        profasi_excluded_volume_local = float(i[13+offset])
        profasi_hydrogen_bond = float(i[14+offset])
        profasi_hydrophobicity = float(i[15+offset])
        profasi_sidechain_charge = float(i[16+offset])
        #profasi_proline_phi_torsion.append(float(i[22+offset]))
        profasi.append(profasi_local+profasi_local_sidechain+profasi_excluded_volume+profasi_excluded_volume_local+profasi_hydrogen_bond+profasi_hydrophobicity+profasi_sidechain_charge)
        basilisk.append(float(i[17+offset]))
        backbone_dbn.append(float(i[-2]))
        eh.append(float(i[-1]))
        mumu_terms = i[9+offset].split(",")
        mumu_energies = []
        try:
            for j in mumu_terms:
                mumu_energies.append(float(j.split(":")[1]))
            mumu.append(sum(mumu_energies))
        except:
            mumu.append(0)

        #profasi.append(float(i[1]))
        #opls.append(opls_charge[-1]+opls_vdw[-1]+opls_angle_bend[-1]+opls_torsion[-1]+opls_improper_torsion[-1]+opls_bond_stretch[-1]+opls_non_bonded[-1])
        #E_all_profasi.append(float(i[1])+mumu[-1]
        #                     #+backbone_dbn[-1]
        #                     +E_cam[-1]
        #                     #+basilisk[-1]
        #                     )
        #E_all.append(float(i[1])
        #             -profasi_local[-1]-profasi_local_sidechain[-1]-profasi_excluded_volume[-1]-profasi_excluded_volume_local[-1]-profasi_hydrogen_bond[-1]-profasi_hydrophobicity[-1]-profasi_sidechain_charge[-1]-profasi_proline_phi_torsion[-1]
        #             +mumu[-1]
        #             #+backbone_dbn[-1]
        #             +E_cam[-1]#+basilisk[-1]
        #             )
        #E_all_opls.append(float(i[1])
        #             -profasi_local[-1]-profasi_local_sidechain[-1]-profasi_excluded_volume[-1]-profasi_excluded_volume_local[-1]-profasi_hydrogen_bond[-1]-profasi_hydrophobicity[-1]-profasi_sidechain_charge[-1]-profasi_proline_phi_torsion[-1]
        #             +opls_charge[-1]
        #             +opls_vdw[-1]
        #             +opls_angle_bend[-1]
        #             +opls_torsion[-1]+opls_improper_torsion[-1]+opls_bond_stretch[-1]+opls_non_bonded[-1]+gbsa[-1]
        #             +mumu[-1]
        #             #+backbone_dbn[-1]
        #             +E_cam[-1]#+basilisk[-1]
        #             )
def save_cpickle(output_filename, data):
    f = open(output_filename,"wb")
    cPickle.dump(data, f, protocol=2)
    f.close()

cpickle_data = {}
cpickle_data["E_native"] = E_native
cpickle_data["E_non_native"] = E_non_native
cpickle_data["rmsd_native"] = rmsd_native
cpickle_data["rmsd_non_native"] = rmsd_non_native
cpickle_data["E_cam"] = E_cam
cpickle_data["basilisk"] = basilisk
cpickle_data["backbone_dbn"] = backbone_dbn
cpickle_data["eh"] = eh
cpickle_data["mumu"] = mumu
cpickle_data["rmsds"] = rmsds
cpickle_data["opls"] = opls
cpickle_data["profasi"] = profasi
cpickle_data["custom"] = custom

save_cpickle(output_filename, cpickle_data)

#print "calculating rmsds"
#lowest_energies = [9999999 for _ in range(255)]
#low_E_rmsds = [99999 for _ in range(255)]
#low_E_rmsd_index = [99999 for _ in range(255)]
#
#for i, profasi_i in enumerate(profasi):
#    energies = []
#    names = ["custom ","cam ", "opls ", "basilisk ", "dbn ", "eh ", "mumu ", "profasi "]
#    combinations = [custom[i], E_cam[i], opls[i], basilisk[i], backbone_dbn[i], eh[i], mumu[i], profasi_i]
#    combination_names = []
#    for ja in range(8):
#        energies.append(combinations[ja])
#        combination_names.append(names[ja])
#        for jb in range(8):
#            if jb > ja:
#                energies.append(combinations[ja]+combinations[jb])
#                combination_names.append(names[ja]+names[jb])
#                for jc in range(8):
#                    if jc > jb:
#                        energies.append(combinations[ja]+combinations[jb]+combinations[jc])
#                        combination_names.append(names[ja]+names[jb]+names[jc])
#                        for jd in range(8):
#                            if jd > jc:
#                                energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd])
#                                combination_names.append(names[ja]+names[jb]+names[jc]+names[jd])
#                                for je in range(8):
#                                    if je > jd:
#                                        energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je])
#                                        combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je])
#                                        for jf in range(8):
#                                            if jf > je:
#                                                energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf])
#                                                combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf])
#                                                for jg in range(8):
#                                                    if jg > jf:
#                                                        energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf]+combinations[jg])
#                                                        combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf]+names[jg])
#                                                        for jh in range(8):
#                                                            if jh > jg:
#                                                                energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf]+combinations[jg]+combinations[jh])
#                                                                combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf]+names[jg]+names[jh])
#    for j, E in enumerate(energies):
#        if E < lowest_energies[j]:
#            lowest_energies[j] = E
#            low_E_rmsds[j] = rmsds[i]
#            low_E_rmsd_index[j] = i
#   
#for j, J in enumerate(lowest_energies):
#    print j, low_E_rmsd_index[j], low_E_rmsds[j], combination_names[j]
#
##print dict((i,low_E_rmsd_index.count(i)) for i in low_E_rmsd_index)
#    
# 
#
#pylab.plot(rmsd_native,E_native,"r.")
#pylab.plot(rmsd_non_native,E_non_native,"k.")
#pylab.savefig("total_energy.png")
#pylab.clf()
##
#pylab.plot(rmsd_native,E_native,"r.")
#pylab.plot(rmsd_non_native,E_non_native,"k.")
#pylab.xlim([0.2,4.1])
#pylab.savefig("total_low_energy.png")
#pylab.clf()
#
#pylab.plot(rmsds,custom,"k.")
#pylab.savefig("custom.png")
#pylab.clf()
#
#pylab.plot(rmsds,E_cam,"k.")
##pylab.xlim([0.0,5.0])
#pylab.savefig("cam.png")
#pylab.clf()
#
##pylab.plot(rmsds,kbp_profasi_sidechain_charge_improved,"k.")
##pylab.savefig("kbp_profasi_sidechain_charge_improved.png")
##pylab.clf()
##
##pylab.plot(rmsds,kbp_profasi_hydrophobicity_improved,"k.")
##pylab.savefig("kbp_profasi_hydrophobicity_improved.png")
##pylab.clf()
##
#pylab.plot(rmsds,mumu,"k.")
#pylab.savefig("mumu.png")
#pylab.clf()
#
##pylab.plot(rmsds,E_all,"k.")
##pylab.savefig("all.png")
##pylab.clf()
##
#pylab.plot(rmsds,profasi,"k.")
#pylab.savefig("profasi.png")
#pylab.clf()
#
#pylab.plot(rmsds,opls,"k.")
#pylab.savefig("opls.png")
#pylab.clf()
##
##pylab.plot(rmsds,opls_charge,"k.")
##pylab.savefig("opls_charge.png")
##pylab.clf()
##
##pylab.plot(rmsds,opls_vdw,"k.")
##pylab.savefig("opls_vdw.png")
##pylab.clf()
##
##pylab.plot(rmsds,opls_angle_bend,"k.")
##pylab.savefig("opls_angle_bend.png")
##pylab.clf()
##
##pylab.plot(rmsds,opls_torsion,"k.")
##pylab.savefig("opls_torsion.png")
##pylab.clf()
##
##pylab.plot(rmsds,opls_improper_torsion,"k.")
##pylab.savefig("opls_improper_torsion.png")
##pylab.clf()
##
##pylab.plot(rmsds,opls_bond_stretch,"k.")
##pylab.savefig("opls_bond_stretch.png")
##pylab.clf()
##
##pylab.plot(rmsds,opls_non_bonded,"k.")
##pylab.savefig("opls_non_bonded.png")
##pylab.clf()
##
##pylab.plot(rmsds,gbsa,"k.")
##pylab.savefig("gbsa.png")
##pylab.clf()
##
##pylab.plot(rmsds,profasi_local,"k.")
##pylab.savefig("profasi_local.png")
##pylab.clf()
##
##pylab.plot(rmsds,profasi_local_sidechain,"k.")
##pylab.savefig("profasi_local_sidechain.png")
##pylab.clf()
##
##pylab.plot(rmsds,profasi_excluded_volume,"k.")
##pylab.savefig("profasi_excluded_volume.png")
##pylab.clf()
##
##pylab.plot(rmsds,profasi_excluded_volume_local,"k.")
##pylab.savefig("profasi_excluded_volume_local.png")
##pylab.clf()
##
##pylab.plot(rmsds,profasi_hydrogen_bond,"k.")
##pylab.savefig("profasi_hydrogen_bond.png")
##pylab.clf()
##
##pylab.plot(rmsds,profasi_hydrophobicity,"k.")
##pylab.savefig("profasi_hydrophobicity.png")
##pylab.clf()
##
##pylab.plot(rmsds,profasi_sidechain_charge,"k.")
##pylab.savefig("profasi_sidechain_charge.png")
##pylab.clf()
##
##pylab.plot(rmsds,profasi_proline_phi_torsion,"k.")
##pylab.savefig("profasi_proline_phi_torsion.png")
##pylab.clf()
##
#pylab.plot(rmsds,basilisk,"k.")
#pylab.savefig("basilisk.png")
#pylab.clf()
##
#pylab.plot(rmsds,backbone_dbn,"k.")
#pylab.savefig("backbone_dbn.png")
#pylab.clf()
##
#pylab.plot(rmsds,eh,"k.")
##pylab.ylim(-200,-700)
#pylab.savefig("eh.png")
#pylab.clf()
#
