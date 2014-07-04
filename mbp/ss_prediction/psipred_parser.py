import sys

file_ = open(sys.argv[1],"r")
cut_off = int(sys.argv[2])

confidence = []
prediction = []
prediction_string = ""

for line_ in file_:
    for i in line_:
        if i != "\n":
            try:
                confidence.append(int(i))
            except:
                prediction.append(i)


for i, conf in enumerate(confidence):
    if conf < cut_off:
        prediction_string += "-"
    else:
        prediction_string += prediction[i]
print prediction_string
