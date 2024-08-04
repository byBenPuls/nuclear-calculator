# English language

menu_text = 'Select a number: '

particle = [
    'Enter your element (A): ',
    'Enter your element (B): ',
    'Enter your element (C): ',
    'Enter your element (D): ',
    'Enter your element (E) optional. Skip if you don\'t need element E: ',

]

menu = {
    '1': 'Calculate energy yield reaction',
    '2': 'Give info about a definite atome',
    '3': 'Mass conversion in u to MeV',
    '4': 'Instructions and feedback',
    '5': 'Settings'
}

reaction_endo = [
    'Reaction',
    'is endoenergetic.\n\n',
    'is exoenergetic.\n\n',
    'Energy yield reaction: ',
    'MeV',
    'Minimum threshold energy of bombarding particle'
]

find = [
    'Enter an isotope (O-17): ',
    '\nСharacteristics',
    'Mass: ',
    'Mass number: ',
    'Atomic number: ',
    'Electrons: ',
    'Protons: ',
    'Neutrons: ',
    'Nucleus radius: '
]

convertation = [
    'Enter a mass in u for conversation to MeV: '
]

help_menu = ('Mode 1:'
             '\n\nYou can calculate energy rection yield. '
             'This program can calculate reaction like this:\n'
             'A + B => C + D\n'
             'A + B => C + D + E\n'
             'If your reaction have more coefficients, then do not try calculate in this program. '
             'The operation is not supported yet.\nProgram calculating energy reaction yield and if '
             'energy reaction is < 0, then program calculating minimum threshold bombarding particle.'
             '\n\nMode 2:'
             '\n\nProgram can give information about an isotope..'
             '\n\nMode 3:'
             '\n\nConversion from u to MeV'
             '\n\ndiscordben7@gmail.com')

help_reactions = ('\nReaction like this:\n'
                  'A + B => C + D\n'
                  'A + B => C + D + E\n')

after = ['\n\n\nPress any key to continue...']

errors = [
    'Element not found...',
    'Incorrect isotope',
    'Your selected number does not exist\n'
]

settings = [
    'You can change language. Aviable languages',
    'Enter "en" for English or "ru" for Russian\n"',
    'This language is already installed',
    'The new language has been successfully installed. \nRestart the program',
    'This language not found in files..'
]

rest = [
    '\nRestarting programm (after 3 seconds)...'
]
