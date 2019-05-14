import numpy as np
from Converter import convertline
from Converter import create_conversions

def PDBwrite(self,newname):
    # This function takes a LAMMPS .data file and returns a PDB file of the name 'newname' do not add .pdb to 'newname' it is ammended automatically
    # The PDB file returned is missing a significant amount of information which PDB's can contain, however it contains all of th ecoordinate information
    # as well as the atomic symbols and weights. The returned file should be fully compatible with VMD and other visualization softwares
    conversion_table = create_conversions(self)
    header_keywords = [
                  "atoms", "bonds", "angles", "dihedrals", "impropers",
                  "atom types", "bond types", "angle types",
                  "dihedral types", "improper types",
                  "xlo xhi", "ylo yhi", "zlo zhi"]

    connections = dict([
                      ["Bonds", ("bonds", 3)],
                      ["Angles", ("angles", 3)],
                      ["Dihedrals", ("dihedrals", 4)],
                      ["Impropers", ("impropers", 2)]])

    coeff = dict([
                 ["Masses", ("atom types", 1)],
                 ["Velocities", ("atoms", 3)],
                 ["Pair Coeffs", ("atom types", 4)],
                 ["Bond Coeffs", ("bond types", 2)],
                 ["Angle Coeffs", ("angle types", 4)],
                 ["Dihedral Coeffs", ("dihedral types", 3)],
                 ["Improper Coeffs", ("improper types", 2)]])
    newfile="%s.pdb" % newname
    with open(self,'r') as f, open(newfile, 'w+') as g:
        for line2 in f:
            if 'Atoms' in line2:
                atoms=True
                valocities=False
                for line2 in f:
                    if line2.strip():
                            if 'Velocities' in line2:
                                break
                            if 'Bonds' in line2:
                                break
                            atominfo = line2.split()
                            index=atominfo[0]
                            q=atominfo[3]
                            x=float(atominfo[4])
                            y=float(atominfo[5])
                            z=float(atominfo[6])
                            if len(atominfo)<10:
                                nx = 1
                                ny = 1
                                nz = 1
                            else:
                                nx=float(atominfo[7])
                                ny=float(atominfo[8])
                                nz=float(atominfo[9])
                            convertline(atominfo, conversion_table)
                            number = atominfo[2]
                            if x<0:
                                x='{:.7s}'.format('{:0.4f}'.format(x))
                            else:
                                x='{:.6s}'.format('{:0.4f}'.format(x))
                            if y<0:
                                y='{:.7s}'.format('{:0.4f}'.format(y))
                            else:
                                y='{:.6s}'.format('{:0.4f}'.format(y))
                            if z<0:
                                z='{:.7s}'.format('{:0.4f}'.format(z))
                            else:
                                z='{:.6s}'.format('{:0.4f}'.format(z))
                            #print(x)
                            PDBline = ["ATOM".ljust(6),index.rjust(5)," ",number.ljust(4),"L","/RN"," ","C","/RSN","/","   ",x.rjust(8),y.rjust(8),z.rjust(8),"VAL".rjust(5),"Tfac".rjust(6),"       ","SEGI",number.rjust(2)]
                            g.write("".join(PDBline)+'\n')
                            #print(g)
                                       ##if 'Velocities' in line:
