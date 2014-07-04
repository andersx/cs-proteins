import sys

file_ = open(sys.argv[1],"r")
cut_off = float(sys.argv[2])

score = []
prediction_string = ""

for line_ in file_:
    line_ = line_.split()
    score.append(float(line_[1]))


for i, value in enumerate(score):
    if value > cut_off:
        prediction_string += "H"
    elif value < -cut_off:
        prediction_string += "E"
    elif abs(value) < 0.2 and abs(value) > 0.000:
        prediction_string += "C"
    else:
        prediction_string += "-"
print prediction_string
