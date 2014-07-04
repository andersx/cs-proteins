import sys

file_ = open(sys.argv[1],"r").readlines()
cut_off = float(sys.argv[2])

prediction = ""
for line_ in file_:
    if line_[0] != "#":
        line_ = line_.split()
        H = float(line_[-3])
        E = float(line_[-2])
        T = float(line_[-1])
        if cut_off < 0.5:
            if H > E and H > T:
                prediction+="H"
            elif E > H and E > T:
                prediction+="E"
            elif T > H and T > E:
                prediction+="T"
        elif H > cut_off:
            prediction+="H"
        elif E > cut_off:
            prediction+="E"
        elif T > cut_off:
            prediction+="T"
        else:
            prediction+="-"
print prediction

