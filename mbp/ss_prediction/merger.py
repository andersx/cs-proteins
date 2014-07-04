import sys

d = {}

for i in sys.argv[1:]:
    file_ = open(i,"r").readlines()[0][:-1]
    for i, I in enumerate(file_):
        if I == "C":
            I = "T"
        if i not in d:
            d[i]=[I]
        else:
            d[i].append(I)
prediction = ""
for i in range(len(d)):
    T_count = 0
    H_count = 0
    E_count = 0
    nan_count = 0
    for j in d[i]:
        if j == "T":
            T_count +=1
        elif j == "H":
            H_count += 1
        elif j == "E":
            E_count += 1
        elif j == "-":
            nan_count += 1
    if H_count > T_count and H_count > E_count and H_count > nan_count:
        prediction += "H"
    elif E_count > T_count and E_count > H_count and E_count > nan_count:
        prediction += "E"
    elif T_count > E_count and T_count > H_count and T_count > nan_count:
        prediction += "T"
    elif T_count >= 2:
        prediction += "T"
    else:
        prediction += "-"
print prediction
