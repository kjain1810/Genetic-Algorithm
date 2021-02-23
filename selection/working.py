import random
import time

from fitness_func.working import fitness

random.seed(time.time())


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


def get_mating_pool(POPULATION_SIZE):
    ret = []
    for i in range(int(POPULATION_SIZE/2)):
        x = random.randint(0, POPULATION_SIZE - 1)
        y = random.randint(0, POPULATION_SIZE - 1)
        while ((x, y) in ret and x != y and (y, x) not in ret):
            x = random.randint(0, POPULATION_SIZE - 1)
            y = random.randint(0, POPULATION_SIZE - 1)
        ret.append((x, y))
    return ret
