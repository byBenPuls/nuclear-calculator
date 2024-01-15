from data import elements_dict, electron_mass, elements_particle, const, radius_const
from functions import reaction_energy, threshold_energy, atom_info, u_to_mev, reaction_energy4

empty = ['', ' ']

main = int(input('1 - Calculate energy yield reaction\n'
                 '2 - Give info about a definite atom\n'
                 '3 - Mass conversion in u to MeV\n'
                 'Select a number: '))

if main == 1:
    print('Reaction like this:\n'
          'A + B => C + D\n'
          'A + B => C + D + E\n')
    a = input(f"Enter your element (A): ").upper()
    b = input(f"Enter your element (B): ").upper()
    c = input(f"Enter your element (C): ").upper()
    d = input(f"Enter your element (D): ").upper()
    e = input(f"Enter your element (E) optional. Skip if you don't need element E: ").upper()

    if e in empty:
        if {a, b, c, d} <= set(elements_particle.keys()) | set(elements_dict.keys()):
            if a in set(elements_particle.keys()):
                r1 = elements_particle[a]
            else:
                element1 = elements_dict[a]
                r1 = element1[2] - element1[1] * electron_mass
            if b in set(elements_particle.keys()):
                r2 = elements_particle[b]
            else:
                element2 = elements_dict[b]
                r2 = element2[2] - element2[1] * electron_mass
            if c in set(elements_particle.keys()):
                r3 = elements_particle[c]
            else:
                element3 = elements_dict[c]
                r3 = element3[2] - element3[1] * electron_mass
            if d in set(elements_particle.keys()):
                r4 = elements_particle[d]
            else:
                element4 = elements_dict[d]
                r4 = element4[2] - element4[1] * electron_mass
            e = reaction_energy(r1, r2, r3, r4, const)
            t = threshold_energy(e, r1, r2)
            if e < 0:
                input(f'\nReaction {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} '
                      f'is endoenergetic.\n\n'
                      f'Energy yield reaction: {e:.5f} MeV\n'
                      f'Minimum threshold energy of bombarding particle ({a.lower()}): {t:.5f} MeV.'
                      f'\n\n\nPress any key to continue...')
            if e > 0:
                input(f'\nReaction {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} '
                      f'is exoenergetic.\n\n'
                      f'Energy yield reaction: {e:.5f} MeV.'
                      f'\n\n\nPress any key to continue...')
        else:
            input('Element not found...')
    else:
        if {a, b, c, d, e} <= set(elements_particle.keys()) | set(elements_dict.keys()):
            if a in set(elements_particle.keys()):
                r1 = elements_particle[a]
            else:
                element1 = elements_dict[a]
                r1 = element1[2] - element1[1] * electron_mass
            if b in set(elements_particle.keys()):
                r2 = elements_particle[b]
            else:
                element2 = elements_dict[b]
                r2 = element2[2] - element2[1] * electron_mass
            if c in set(elements_particle.keys()):
                r3 = elements_particle[c]
            else:
                element3 = elements_dict[c]
                r3 = element3[2] - element3[1] * electron_mass
            if d in set(elements_particle.keys()):
                r4 = elements_particle[d]
            else:
                element4 = elements_dict[d]
                r4 = element4[2] - element4[1] * electron_mass
            if e in set(elements_particle.keys()):
                r5 = elements_particle[e]
            else:
                element5 = elements_dict[e]
                r5 = element5[2] - element5[1] * electron_mass
            energy_yield = reaction_energy4(r1, r2, r3, r4, r5, const)
            t = threshold_energy(energy_yield, r1, r2)
            if energy_yield < 0:
                input(f'\nReaction {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} + {e.lower()} '
                      f'is endoenergetic.\n\n'
                      f'Energy yield reaction: {energy_yield:.5f} MeV\n'
                      f'Minimum threshold energy of bombarding particle ({a.lower()}): {t:.5f} MeV.'
                      f'\n\n\nPress any key to continue...')
            if energy_yield > 0:
                input(f'\nReaction {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} + {e.lower()} '
                      f'is exoenergetic.\n\n'
                      f'Energy yield reaction: {energy_yield:.5f} MeV.'
                      f'\n\n\nPress any key to continue...')
        else:
            input('Element not found...')
if main == 2:
    isotope = input('\nChoose an isotope (like this: O-17): ')
    isotope_check = elements_dict[isotope.upper()]
    if isotope.upper() in elements_dict:
        try:
            atom_info(isotope_check[1], isotope_check[2], radius_const,
                      isotope, isotope_check[3], isotope_check[0])
        except IndexError:
            input('No such isotope...')
    if isotope.upper() not in elements_dict:
        input('Isotope not found...')
if main == 3:
    u = int(input('Enter a mass in u for conversation to MeV: '))
    input(f'{u} u - {u_to_mev(u, const)} MeV\n'
          f'Press any key to continue...')
else:
    input('Your selected number does not exist\n'
          'Press any key to continue... ')
