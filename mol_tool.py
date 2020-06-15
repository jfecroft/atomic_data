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

if __name__ == '__main__':
    args = docopt(__doc__)

    a1 = args["<a1>"]
    i1 = int(args["<i1>"])

    a2 = args["<a2>"]
    i2 = int(args["<i2>"])

    mol = a1+a2

    mass = DATA["Atoms"][a1][i1]["mass"] + DATA["Atoms"][a2][i2]["mass"]

    C6 = DATA["MoleculeMolecule"][mol]["C6"]  # for now ony work for same spiecies

    mu = red_mass(mass, mass)
    l_vdw = vdw_length(C6, mu)
    e_vdw = vdw_energy(C6, mu)
    abar = get_abar(C6, mu)

    print "for collsions of {} with {}".format(mol, mol)
    print "the van de Waals length is {}".format(l_vdw)
    print "the van de Waals energy is {}".format(e_vdw)
    print "abar is {}".format(abar)
    import pdb
    pdb.set_trace()
