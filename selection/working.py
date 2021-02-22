import random

from fitness_func.working import fitness


def select(vecs, POPULATION_SIZE):
    vecs = sorted(vecs, key=lambda i: fitness(i["results"]))
    ret = []
    for i in range(len(vecs)):
        x = random.random()
        if x <= 0.8:
            ret.append(vecs[i])
            if len(ret) == POPULATION_SIZE:
                break
    return ret
