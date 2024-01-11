def reaction_energy(e1, e2, convertationconst):
    return (e1 - e2) * convertationconst


def threshold_energy(q, e1, e2):
    return abs(q) * (1 + (e1 / e2))
