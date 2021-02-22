import numpy as np
import random
import time
import json

# from ..fitness_func.working import fitness


def fitness(res, FACTOR=0.7):
    return res[0] * FACTOR + res[1]


# from .working import get_initial_value

given_data = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
              1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]

big_change = [0, 1, 2, 3, 4, 6]


def init_values(POPULATION_SIZE, VECTOR_SIZE=11):
    initial_values = []
    for i in range(POPULATION_SIZE):
        here = []
        for j in range(len(given_data)):
            here.append(given_data[j])
        initial_values.append(here)
    random.seed(time.time())
    for i in range(POPULATION_SIZE):
        for j in range(VECTOR_SIZE):
            if j in big_change:
                initial_values[i][j] = random.uniform(-1, 1)
            else:
                initial_values[i][j] = initial_values[i][j] * \
                    random.uniform(0.9999, 1.0001) + \
                    random.uniform(-1e-18, 1e-18)
            # x = random.random()
            # if x < 0.5:  # TUNE
            #     y = random.uniform(-1e-18, 1e-18)
            #     if abs(initial_values[i][j] + y) <= 10:
            #         initial_values[i][j] += y
            #     factor = random.random() * 0.2 + 0.9
            #     if abs(initial_values[i][j] * factor) <= 10:
            #         initial_values[i][j] *= factor
    return initial_values


def load_inits(POPULATION_SIZE, VECTOR_SIZE=11):
    inits = []
    with open("./generations.json") as f:
        res = json.load(f)
    res = res["results"]
    vecs = []
    for x in res:
        y = x["vectors"]
        for z in y:
            vecs.append(z)
    vecs = sorted(vecs, key=lambda i: fitness(i["results"]))
    for i in range(POPULATION_SIZE):
        inits.append(vecs[i])
    # for i in range(len(vecs)):
    #     x = random.random()
    #     if x <= 0.9:
    #         inits.append(np.array(vecs[i]["vector"]))
    #     if len(inits) == POPULATION_SIZE:
    #         return inits
    return inits


if __name__ == "__main__":
    print(init_values(20))
    # init_values(20)
