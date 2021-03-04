def fitness(res, FACTOR=1.0):
    return abs(res[0] ** 2 - res[1] ** 2) + res[0] * res[1]


def fitness_orig(res):
    return res[0] + res[1]
