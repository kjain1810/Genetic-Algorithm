from fitness_func.working import fitness
import numpy as np
import random
import time
import json


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


def load_prev_gens(file, generation):
    with open(file) as f:
        res = json.load(f)

    inits = []
    for gen in res["generations"]:
        if(gen["generation"] == generation):
            inits.append(gen["vectors"])
    return inits


def get_best_from_all_gens(POPULATION_SIZE):
    # files = ["new_gen_1.json", "new_gen_2.json", "new_gen_3.json",
    #  "new_gen_4.json", "new_new_gen_5.json", "fixed_6.json", "fixed_7.json", "fixed_8.json"]
    files = ["fixed_8.json"]
    inits = []
    for file in files:
        with open(file) as f:
            res = json.load(f)
        res = res["generations"]
        for gen in res:
            for vec in gen["vectors"]:
                if vec["results"] == [0, 0]:
                    continue
                inits.append(
                    {"vector": vec["vector"]["child"], "results": vec["results"], "generation": gen["generation"]})
    # with open("./generations.json") as f:
    #     res = json.load(f)
    # res = res["results"]
    # for x in res:
    #     y = x["vectors"]
    #     for z in y:
    #         inits.append(z)
    inits = sorted(inits, key=lambda i: fitness(i["results"]))
    final_inits = []
    for i in range(POPULATION_SIZE):
        final_inits.append(inits[i])

    return final_inits


def hand_picked():
    picked_generations = [
        0,
        1,
        3,
        4,
        5,
        6,
        7,
        9,
        10,
        11,
        12,
        13,
        20,
        25,
        28,
        30
    ]
    here = get_best_from_all_gens(200)
    ret = []
    for i in range(len(picked_generations)):
        ret.append(here[picked_generations[i]])
    return ret


if __name__ == "__main__":
    print(init_values(20))
    # init_values(20)
