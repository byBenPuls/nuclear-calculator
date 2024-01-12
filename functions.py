from math import pow, fsum


def reaction_energy(e1, e2, e3, e4, convertationconst):
    return (fsum([e1, e2]) - fsum([e3, e4])) * convertationconst
# Measured in MeV


def threshold_energy(q, e1, e2):
    return abs(q) * (1 + (e1 / e2))
# Measured in MeV


def nucleus_radius(const, mass_number):
    return const * pow(mass_number, 1 / 3)
# Measured in Fm
