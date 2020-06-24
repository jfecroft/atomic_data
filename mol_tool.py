#!/usr/bin/env python
"""
Utility script for computing molecular constants

Usage:
  mol_tool <a1> <i1> <a2> <i2>

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt
from myconstants import DATA, red_mass, vdw_length, vdw_energy, get_abar

class MolMol:
    def __init__(self, a1, i1, a2, i2):
        self.a1 = a1
        self.a2 = a2
        self.i1 = int(i1)
        self.i2 = int(i2)
        self.mol = a1+a2
        self.mass1 = DATA["Atoms"][self.a1][self.i1]["mass"]
        self.mass2 = DATA["Atoms"][self.a2][self.i2]["mass"]
        self.mass = self.mass1 + self.mass2
        self.C6 = DATA["MoleculeMolecule"][self.mol]["C6"]
        self.mu = red_mass(self.mass, self.mass)
        self.l_vdw = vdw_length(self.C6, self.mu)
        self.e_vdw = vdw_energy(self.C6, self.mu)
        self.abar = get_abar(self.C6, self.mu)


if __name__ == '__main__':
    args = docopt(__doc__)

    a1 = args["<a1>"]
    i1 = args["<i1>"]

    a2 = args["<a2>"]
    i2 = args["<i2>"]

    Sys = MolMol(a1, i1, a2, i2)

    print "for collsions of {} with {}".format(Sys.mol, Sys.mol)
    print "the reduced mass is {}".format(Sys.mu)
    print "the van de Waals length is {}".format(Sys.l_vdw)
    print "the van de Waals energy is {}".format(Sys.e_vdw)
    print "abar is {}".format(Sys.abar)
