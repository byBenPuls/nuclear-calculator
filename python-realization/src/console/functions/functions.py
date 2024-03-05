from math import pow, fsum
import os
import sys

def u_to_mev(u, const):
    return u * const


def reaction_energy(e1, e2, e3, e4, convertationconst):
    return (fsum([e1, e2]) - fsum([e3, e4])) * convertationconst


# Measured in MeV


def reaction_energy4(e1, e2, e3, e4, e5, convertationconst):
    return (fsum([e1, e2]) - fsum([e3, e4, e5])) * convertationconst


def threshold_energy(q, e1, e2):
    return abs(q) * (1 + (e1 / e2))


# Measured in MeV


def nucleus_radius(const, mass_number):
    return const * pow(mass_number, 1 / 3)


# Measured in Fm


def atom_info(nuclear_charge, mass_number, const, name, stable_check, isotope_name):
    stability = {True: 'stable', False: 'unstable'}
    a = round(mass_number)
    z = nuclear_charge
    count_neutrons = a - z
    count_protons = z
    count_electrons = z
    mass_u = u_to_mev(mass_number, const)
    radius = nucleus_radius(const, mass_number)
    input(f'{isotope_name} isotope ({name}) have {count_neutrons} neutrons, '
          f'{count_protons} protons and {count_electrons} electrons. A = {a}. Z = {z}.'
          f'\nIsotope has mass {mass_number} u or {mass_u} MeV.'
          f'\nNucleus radius is: {round(radius, 3)} Fm.'
          f'\nThis isotope is {stability[stable_check]}.'
          f'\n\nPress enter to continue...')


def after(text):
    input(text)
