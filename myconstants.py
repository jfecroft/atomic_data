"""
for useful constants such as masses etc
"""
from scipy.constants import hbar, physical_constants, angstrom
from math import sqrt
import yaml

TOL = 1.0e-5

bohrradius2angstrom = physical_constants["Bohr radius"][0]/angstrom
kelvin2wavenumbers = physical_constants["kelvin-inverse meter relationship"][0]/100.0


with open('data.yml') as f:
    DATA = yaml.load(f, Loader=yaml.FullLoader)


def get_bfct():
    """
    return bfct = hbar**2/2 in units of K*AMU*Ang**2

    similar to bfct in molscat but in kelvin not wavenumbers

    returns a value 24.25437532030504
    """
    bfct = hbar**2
    bfct *= physical_constants["joule-kelvin relationship"][0]
    # bfct *= physical_constants["joule-inverse meter relationship"][0]/100.0
    bfct *= physical_constants["kilogram-atomic mass unit relationship"][0]
    bfct /= angstrom**2
    bfct /= 2
    return bfct


BFCT = get_bfct()


def vdw_length(C6, mu):
    return pow(mu*C6/BFCT, 1.0/4)


def vdw_energy(C6, mu):
    beta = vdw_length(C6, mu)
    return BFCT/(mu*beta**2)


def get_abar(C6, mu):
    abar = vdw_length(C6, mu)
    abar *= 4.0*pi/gamma(1/4.0)**2
    return abar


def red_mass(m1, m2):
    return m1*m2/(m1 + m2)


if __name__ == "__main__":
    import pdb
    pdb.set_trace()
