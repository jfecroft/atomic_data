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
from myconstants import MolMol


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
