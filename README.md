# Lammps-to-PDB-writer
This code converts LAMMPS data files to PDB files. Much of the information in the files is mostly filler, but they contain coordinate information as well as atomic symbols and weights.
To use it you simply pass the writer the .data file and a the name you would like the PDB to be under
Example: in a python terminal in the repository where the converter and your data files are stored, type:

from PDBwriter import PDBwrite
PDBwrite('expamplefile.data', 'newexamplefile')

this will write and return a PDB file under the name newexamplefile.pdb
The original LAMMPS file will not be altered

In order for the program to work the LAMMPS file must follow the traditional .data file format
Read the comments in the files if something isn't working properly. The code may need supplementary input from the user, but it should only require minor additions.
