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

#
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

#for i, I in enumerate(cpickle_data["custom"][0]):
#    cpickle_data["custom_%d" %i] = [float(x[i]) for x in cpickle_data["custom"]]
#    pylab.plot(cpickle_data["rmsds"],cpickle_data["custom_%d" %i],"k.")
#    pylab.savefig("custom_%d.png" %i)
#    pylab.clf()
#
pylab.plot(cpickle_data["rmsds"],cpickle_data["E_cam"],"k.")
#pylab.xlim([0.0,5.0])
pylab.savefig("cam.png")
pylab.clf()

pylab.plot(cpickle_data["rmsds"],cpickle_data["mumu"],"k.")
pylab.savefig("mumu.png")
pylab.clf()

pylab.plot(cpickle_data["rmsds"],cpickle_data["profasi"],"k.")
pylab.savefig("profasi.png")
pylab.clf()

#pylab.plot(cpickle_data["rmsds"],cpickle_data["opls"],"k.")
#pylab.savefig("opls.png")
#pylab.clf()
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
lowest_energies =  [9999999 for _ in range(219780)]
low_E_rmsds =      [9999999 for _ in range(219780)]
low_E_rmsd_index = [9999999 for _ in range(219780)]
print min(cpickle_data["rmsds"])
for i, dbn_i in enumerate(cpickle_data["backbone_dbn"]):
    energies = []
    #names = ["custom_0","custom_1","custom_2","custom_3","custom_4", "opls", "basilisk", "backbone_dbn", "eh", "mumu", "profasi","E_cam"]
    names = ["backbone_dbn","profasi","E_cam","mumu","eh"] #eh,isd
    combinations = [cpickle_data[x][i] for x in names]
    combination_names = []
    for ja in range(len(names)):
        energies.append(combinations[ja])
        combination_names.append(names[ja])
        for jb in range(len(names)):
            if jb > ja:
                energies.append(combinations[ja]+combinations[jb])
                combination_names.append(names[ja]+names[jb])
                for jc in range(len(names)):
                    if jc > jb:
                        energies.append(combinations[ja]+combinations[jb]+combinations[jc])
                        combination_names.append(names[ja]+names[jb]+names[jc])
                        for jd in range(len(names)):
                            if jd > jc:
                                energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd])
                                combination_names.append(names[ja]+names[jb]+names[jc]+names[jd])
                                for je in range(len(names)):
                                    if je > jd:
                                        energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je])
                                        combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je])
                                        for jf in range(len(names)):
                                            if jf > je:
                                                energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf])
                                                combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf])
                                                for jg in range(len(names)):
                                                    if jg > jf:
                                                        energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf]+combinations[jg])
                                                        combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf]+names[jg])
                                                        for jh in range(len(names)):
                                                            if jh > jg:
                                                                energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf]+combinations[jg]+combinations[jh])
                                                                combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf]+names[jg]+names[jh])
                                                            for ji in range(len(names)):
                                                                if ji > jh:
                                                                    energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf]+combinations[jg]+combinations[jh]+combinations[ji])
                                                                    combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf]+names[jg]+names[jh]+names[ji])
                                                                for jj in range(len(names)):
                                                                    if jj > ji:
                                                                        energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf]+combinations[jg]+combinations[jh]+combinations[ji]+combinations[jj])
                                                                        combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf]+names[jg]+names[jh]+names[ji]+names[jj])
                                                                    for jk in range(len(names)):
                                                                        if jk > jj:
                                                                            energies.append(combinations[ja]+combinations[jb]+combinations[jc]+combinations[jd]+combinations[je]+combinations[jf]+combinations[jg]+combinations[jh]+combinations[ji]+combinations[jj]+combinations[jk])
                                                                            combination_names.append(names[ja]+names[jb]+names[jc]+names[jd]+names[je]+names[jf]+names[jg]+names[jh]+names[ji]+names[jj]+names[jk])
    for j, E in enumerate(energies):
        if E < lowest_energies[j]:
            lowest_energies[j] = E
            low_E_rmsds[j] = cpickle_data["rmsds"][i]
            low_E_rmsd_index[j] = i
   
for j, J in enumerate(lowest_energies):
    print j, low_E_rmsd_index[j], low_E_rmsds[j], combination_names[j]
