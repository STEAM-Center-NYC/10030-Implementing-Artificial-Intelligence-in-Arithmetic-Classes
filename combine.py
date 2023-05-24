import os

def openfile(file, start=True):
    if start == True:
        doc = open(file, 'a+')
        return doc
    else:
        doc = open(file, 'r')
        return doc

startingfile = openfile("number_theory.txt")

for files in os.listdir("/Users/ECU/Documents/GitHub/10030-Implementing-Artificial-Intelligence-in-Arithmetic-Classes/10030-Implementing-Artificial-Intelligence-in-Arithmetic-Classes/MATH/train/number_theory"):
    file = openfile("/Users/ECU/Documents/GitHub/10030-Implementing-Artificial-Intelligence-in-Arithmetic-Classes/10030-Implementing-Artificial-Intelligence-in-Arithmetic-Classes/MATH/train/number_theory/" + files, start=False)
    startingfile.write("," + file.read())
    file.close()
