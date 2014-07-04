import sys
import string

filenames = sys.argv[1:]

min_energy = 99999999999999999
min_rmsd = 99999999

min_energy_line = "l"
min_rmsd_line = "l"
for filename in filenames[:]:
    data = open(filename, "r").readlines()
    for line in data[1:30000]:
        l = string.split(line,"\t")
        energy, rmsd = float(l[1]), float(l[-4])
        if energy < min_energy:
            min_energy = energy
            min_energy_line = line
        if rmsd < min_rmsd:
            min_rmsd = rmsd
            min_rmsd_line = line

print min_energy, min_rmsd
            
