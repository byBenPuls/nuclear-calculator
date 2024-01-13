const isotopes = require('./data/isotopes.json')


exports.getRadius = (name) => {
    const isotope = name.toUpperCase ()
    const path = isotopes.elements_dict
    if (isotope in path) {
        const mass_number = path[isotope][2]
        return (1.12 * ((mass_number) ** 1 / 3))
    } else {
        return 'not found'
    }
}

exports.getInfo = (name) => {
    const isotope = name.toUpperCase ()
    const path = isotopes.elements_dict
    const mass = path[isotope]
    if (isotope in path) {
        if (mass[3] !== undefined)  {
            const name_element = mass[0]
            const atomic_number = mass[1]
            const mass_number = mass[2]
            const count_neutrons = Math.round(mass_number) - atomic_number
            const count_electrons = atomic_number
            const count_protons = atomic_number
            const stable = mass[3]
            const radius = (1.12 * ((mass_number) ** 1 / 3))
            return [name_element, atomic_number, mass_number, count_neutrons, count_protons, count_electrons, stable, radius]
        } else {
            console.log('Сould not find isotope parameter \'stability\'')
            return 'Oops. Not found'
        }
    } else {
        return 'not found'
    }
}