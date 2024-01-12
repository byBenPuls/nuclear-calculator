from data import elements_dict, electron_mass, elements_particle, const, radius_const
from functions import reaction_energy, threshold_energy


print('Reaction like this: A + B => C + D\n')
a = input(f"Enter your element (A): ").upper()
b = input(f"Enter your element (B): ").upper()
c = input(f"Enter your element (C): ").upper()
d = input(f"Enter your element (D): ").upper()

if {a, b, c, d} <= set(elements_particle.keys()) | set(elements_dict.keys()):
    if a in set(elements_particle.keys()):
        r1 = elements_particle[a]
    else:
        element1 = elements_dict[a]
        r1 = element1[1] - element1[0] * electron_mass
    if b in set(elements_particle.keys()):
        r2 = elements_particle[b]
    else:
        element2 = elements_dict[b]
        r2 = element2[1] - element2[0] * electron_mass
    if c in set(elements_particle.keys()):
        r3 = elements_particle[c]
    else:
        element3 = elements_dict[c]
        r3 = element3[1] - element3[0] * electron_mass
    if d in set(elements_particle.keys()):
        r4 = elements_particle[d]
    else:
        element4 = elements_dict[d]
        r4 = element4[1] - element4[0] * electron_mass
    e = reaction_energy(r1, r2, r3, r4, const)
    t = threshold_energy(e, r1, r2)
    if e < 0:
        input(f'\nReaction {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} '
              f'is endoenergetic.\n\n'
              f'Energy yield reaction: {e:.5f} MeV\n'
              f'Threshold energy of bombarding particle ({a.lower()}): {t:.5f} MeV.'
              f'\n\n\nPress any key to continue...')
    if e > 0:
        input(f'\nReaction {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} '
              f'is exoenergetic.\n\n'
              f'Energy yield reaction: {e:.5f} MeV.'
              f'\n\n\nPress any key to continue...')
else:
    input('Element not found...')
