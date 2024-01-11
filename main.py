import math
from data import elements_dict, electron_mass, elem_part, const
from functions import reaction_energy, threshold_energy

a = input("Enter your element: ").upper()
b = input("Enter your element: ").upper()
c = input("Enter your element: ").upper()
d = input("Enter your element: ").upper()

if (a and b and c and d) in elements_dict or elem_part:
    if {a, b, c, d} <= set(elem_part.keys()) | set(elements_dict.keys()):
        if a in set(elem_part.keys()):
            r1 = elem_part[a]
        else:
            element1 = elements_dict[a]
            r1 = element1[1] - element1[0] * electron_mass
    if b in set(elem_part.keys()):
        r2 = elem_part[b]
    else:
        element2 = elements_dict[b]
        r2 = element2[1] - element2[0] * electron_mass
    if c in set(elem_part.keys()):
        r3 = elem_part[c]
    else:
        element3 = elements_dict[c]
        r3 = element3[1] - element3[0] * electron_mass
    if d in set(elem_part.keys()):
        r4 = elem_part[d]
    else:
        element4 = elements_dict[d]
        r4 = element4[1] - element4[0] * electron_mass
    e = reaction_energy(math.fsum([r1, r2]), math.fsum([r3, r4]), const)
    t = threshold_energy(e, r1, r2)
    if e < 0:
        input(f'Реакция {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} является эндотермической.\n'
              f'Энергетический выход реакции: {e:.5f} МэВ.\n'
              f'Пороговая энергия бомбардирующей частицы ({a.lower()}): {t:.5f} МэВ.')
    if e > 0:
        input(f'Реакция {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} является экзотермической.\n'
              f'Энергетический выход реакции: {e:.5f} МэВ.\n'
              f'Пороговая энергия бомбардирующей частицы ({a.lower()}): {t:.5f} МэВ.')
else:
    input('Element not found.')
