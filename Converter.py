import numpy as np
import math

con4=[[str(1), 12.011],
 [str(2), 12.011],
 ['3', 12.011],
 ['4', 12.011],
 ['5', 1.008],
 ['6', 32.066],
 ['7', 15.999],
 ['8', 12.011],
 ['9', 12.011],
 ['10', 1.008],
 [str(11), 18.998],
 ['12', 12.011],
 ['13', 15.999]]
# unneccessary, but this is the format for the converter to be passed:


def create_conversions(self):
    # this function reads a LAMMPS .data file and returns a converter of the format above which assigns
    # molecule numbers to their respective masses 
    con = []
    with open(self, 'r') as f:
        for line in f:
            if 'Masses' in line:
                for line in f:
                    if line.strip():
                        if 'Pair Coeffs'in line:
                            break
                        con.append(line.split())
    return con

con2=[[12.011,"C"],
      [1.008,"H"],
      [18.998,"F"],
      [15.999,"O"],
      [14.027,"N"],
      [15.035,"NH"],
      [13.019,"CH"],
      [32.06,"S"],
      [35.453,"Cl"],
      [83.798,"Kr"],
      [4.003,"He"],
      [20.179,"Ne"],
      [32.066,"S"]]
## It is necessary to add the atomic masses and symbols of any atoms or molecules to be used here 
## Make sure to follow the same format

def convertwhole(filer):
    ## This is not fully fleshed out yet. It is best to use converline in a loop.
    newfile='newfile.pdb'
    with open(filer,'r') as f, open(newfile, 'w+') as g:
              for line in f:
                  f2=line.split()
                  print(f2)
                  for i in range(len(con1)):
                      if con1[i][0] == f2[10]:
                          f2[2] = con1[i][1]
                  for i in range(len(con2)):
                      if con2[i][0] == f2[2]:
                          f2[2] = con2[i][1]
                  g.write(" ".join(f2)+"\n")

def convertline(line, con1):
    # This function takes in a line as read by readlines() and the conversion table created by convert_line()
    # It returns the line in the same format but with the atomic symbol in place of the atomic weight ID
    for i in range(len(con1)):
        if line[2] == con1[i][0]:
            line[2] = con1[i][1]
    for i in range(len(con2)):
        if math.isclose(float(line[2]), float(con2[i][0]), abs_tol = 1e-2):
            line[2] = con2[i][1]
            return

