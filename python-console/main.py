from data.elements import *
from functions.functions import *
from data.special import *
from data.list import *
from functions.technical import *
import time
import configparser
from pathlib import Path
import os

aviable_language = ['en', 'ru']
empty = ['', ' ']
if os.path.exists('configuration/language.ini'):
    config = configparser.ConfigParser()
    config.read('configuration/language.ini')
    main_language = config.get('Language', 'MainLanguage')
else:
    print('Configuration file not found\n'
          'Creating the configuration file\n\n')
    time.sleep(2)


    def display_progress_bar(iteration, all_procent, bar_length=50):
        progress = (iteration / all_procent)
        arrow = '=' * int(round(progress * bar_length) - 1)
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write(f'\rProgress: [{arrow + spaces}] {int(progress * 100)}%')
        sys.stdout.flush()


    total = 100
    for i in range(total + 1):
        time.sleep(0.1)
        display_progress_bar(i, total)
    path = Path('configuration')
    path.mkdir(parents=True)
    open('configuration/language.ini', 'a').close()
    config = configparser.ConfigParser()
    config.add_section('Language')
    config.set('Language', 'mainlanguage', 'en')
    with open('configuration/language.ini', 'w') as config_file:
        config.write(config_file)
    restart('\nRestarting programm (after 3 seconds)...')

if main_language == 'en':
    from languages.en import *
elif main_language == 'ru':
    from languages.ru import *

print('_________________________________________')
for key, value in menu.items():
    print('{r:2s}| {w:5s} '.format(r=key, w=value))
print('-----------------------------------------\n')
main = int(input(menu_text))

if main == 1:
    print(help_reactions)
    a = input(particle[0]).upper().replace(' ', '')
    b = input(particle[1]).upper().replace(' ', '')
    c = input(particle[2]).upper().replace(' ', '')
    d = input(particle[3]).upper().replace(' ', '')
    e = input(particle[4]).upper().replace(' ', '')

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
                print(f'\n{reaction_endo[0]} {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} '
                      f'{reaction_endo[1]}.\n\n'
                      f'{reaction_endo[3]}{e:.5f} {reaction_endo[4]}\n'
                      f'{reaction_endo[5]} ({a.lower()}): {t:.5f} {reaction_endo[4]}.',
                      )
                input(after[0])
            if e > 0:
                print(f'\n{reaction_endo[0]} {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} '
                      f'{reaction_endo[2]}\n\n'
                      f'{reaction_endo[3]}{e:.5f} {reaction_endo[4]}.',
                      )
                input(after[0])
        else:
            input(f'{errors[0]}')
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
                print(f'\n{reaction_endo[0]} {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} + {e.lower()} '
                      f'{reaction_endo[1]}.\n\n'
                      f'{reaction_endo[3]}{energy_yield:.5f} {reaction_endo[5]}\n'
                      f'{reaction_endo[6]} ({a.lower()}): {t:.5f} {reaction_endo[5]}.'
                      )
                input(after[0])
            if energy_yield > 0:
                print(f'\n{reaction_endo[0]} {a.lower()} + {b.lower()} => {c.lower()} + {d.lower()} + {e.lower()} '
                      f'{reaction_endo[2]}.\n\n'
                      f'{reaction_endo[4]}{energy_yield:.5f} {reaction_endo[5]}.'
                      )
                input(after[0])
        else:
            input(errors[0])
elif main == 2:
    try:
        isotope = input(find[0]).replace(' ', '')
        text = isotope[: 1].upper() + isotope[1:]
        result = text.split('-', 3)
        if result[0] in elements:
            qwerty = var[elements[result[0]] - 1]
            number = 0
            while int(result[1]) != qwerty['isotopes'][number]['mass_number']:
                number += 1
            mass = qwerty['isotopes'][number]['mass']
            mass_number = qwerty['isotopes'][number]['mass_number']
            atomic_number = qwerty['atomic_number']
            electrons = atomic_number
            protons = atomic_number
            neutrons = int(mass_number) - int(atomic_number)
            radius = nucleus_radius(radius_const, mass_number)
            print(f'{find[1]} ({text}):\n'
                  f'{find[2]}{mass} u\n'
                  f'{find[3]}{mass_number}\n'
                  f'{find[4]}{atomic_number}\n'
                  f'{find[5]}{electrons}\n'
                  f'{find[6]}{protons}\n'
                  f'{find[7]}{neutrons}\n'
                  f'{find[8]}{round(radius, 5)} Fm'
                  )
            input(after[0])
        else:
            print(errors[1])
            input(after[0])
    except Exception as err:
        input(f'{errors[1]}\n\n{err}')
elif main == 3:
    u = int(input(convertation[0]))
    print(f'{u} u - {u_to_mev(u, const)} {reaction_endo[5]}\n'
          )
    input(after[0])
elif main == 4:
    print(help_menu)
    input(after[0])
elif main == 5:
    config = configparser.ConfigParser()
    languages = aviable_language
    print(f'{settings[0]} ({len(languages)}):')
    print(*languages, sep=', ')
    print(f'. {settings[1]}')
    select_language = input()
    if select_language in languages:
        if select_language == main_language:
            print(settings[2])
            input(after[0])
        else:
            if select_language == 'ru':
                config['Language'] = {
                    'mainlanguage': 'ru'
                }
                with open('configuration/language.ini', 'w') as configfile:
                    config.write(configfile)
                print(settings[3])
                restart(rest[0])
            elif select_language == 'en':
                config['Language'] = {
                    'mainlanguage': 'en'
                }
                with open('configuration/language.ini', 'w') as configfile:
                    config.write(configfile)
                print(settings[3])
                restart(rest[0])
            else:
                print(settings[4])
                restart(rest[0])
    else:
        print(errors[2])
        restart(rest[0])
