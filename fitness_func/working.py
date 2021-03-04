def fitness_lol(res, FACTOR=1.0):
    return abs(res[0] ** 2 - res[1] ** 2) + res[0] * res[1]


def fitness(res, FACTOR=1.0):
    return res[0] * FACTOR + res[1]
