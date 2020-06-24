"""
for useful constants such as masses etc
"""
from scipy.constants import hbar, physical_constants, angstrom
from math import sqrt,  pi, gamma
import yaml

TOL = 1.0e-5

bohrradius2angstrom = physical_constants["Bohr radius"][0]/angstrom
angstrom2bohr = 1/bohrradius2angstrom
kelvin2wavenumbers = physical_constants["kelvin-inverse meter relationship"][0]/100.0
kelvin2hartree = physical_constants["kelvin-hartree relationship"][0]
au2wavenumbers = physical_constants["hartree-inverse meter relationship"][0]/100.0
au2angstrom = physical_constants["Bohr radius"][0]/angstrom
au2kelvin = physical_constants["hartree-kelvin relationship"][0]

with open('data.yml') as f:
    DATA = yaml.load(f, Loader=yaml.FullLoader)


# convert C6 to KAng^6
for i in DATA["Molecules"]:
    DATA["Molecules"][i]["C6"] *= au2kelvin
    DATA["Molecules"][i]["C6"] *= au2angstrom**6

# convert C6 to KAng^6
for i in DATA["MoleculeMolecule"]:
    DATA["MoleculeMolecule"][i]["C6"] *= au2kelvin
    DATA["MoleculeMolecule"][i]["C6"] *= au2angstrom**6


def get_bfct():
    """
    return bfct = hbar**2/2 in units of K*AMU*Ang**2

    similar to bfct in molscat but in kelvin not wavenumbers

    returns a value 24.25437532030504
    """
    bfct = hbar**2/2.0
    bfct *= physical_constants["joule-kelvin relationship"][0]
    # bfct *= physical_constants["joule-inverse meter relationship"][0]/100.0
    bfct *= physical_constants["kilogram-atomic mass unit relationship"][0]
    bfct /= angstrom**2
    return bfct


BFCT = get_bfct()

# for defintions see
# Feshbach resonances in ultracold gases

# Cheng Chin, Rudolf Grimm, Paul Julienne, and Eite Tiesinga
# Rev. Mod. Phys. 82, 1225 - Published 29 April 2010
# https://doi.org/10.1103/RevModPhys.82.1225


def vdw_length(C6, mu):
    """
    note some people define this without the 0.5
    but you need the extra factor of a half to get the correct value for
    the mean scattering length
    """
    return 0.5*pow(mu*C6/BFCT, 1.0/4)


def vdw_energy(C6, mu):
    beta = vdw_length(C6, mu)
    return BFCT/(mu*beta**2)


def get_abar(C6, mu):
    abar = vdw_length(C6, mu)
    abar *= 4.0*pi/gamma(1/4.0)**2
    return abar


def red_mass(m1, m2):
    return m1*m2/(m1 + m2)


class MolMol:
    """
    Interface to get the data for a AB + AB system
    """
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



if __name__ == "__main__":
    import pdb
    pdb.set_trace()
