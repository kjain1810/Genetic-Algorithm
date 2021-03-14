import json
import random
import time
import numpy as np

from client import get_errors

random.seed(time.time())

TEAM_KEY = "prTwq7vUkLegXASklNtVBIA7O8YxRRbYQE8LAnsDrmrx6A0fH1"

VECTOR_SIZE = 11
POPULATION_SIZE = 5
overfit_vector = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
                  1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]

F_INIT_POPULATION = ""
F_DUMP_FILE = ""
NUM_GENERATIONS = 35

# FITNESS FUNCTION


def fitness(res, FACTOR=1.0):
    return FACTOR * res[0] + res[1]

# MATING POOL FUNCTION


def get_mating_pool(POPULATION_SIZE, CHILDREN_SIZE):
    ret = []
    parent_1 = []
    # ENSURES ALL PARENTS GET INVOLVED IN ATLEAST 1 CHILD
    for i in range(POPULATION_SIZE // 2):
        parent_1.append(i)
    # FILL THE REMAINING FIRST PARENTS RANDOMLY
    for i in range((CHILDREN_SIZE - POPULATION_SIZE) // 2):
        parent_1.append(random.randint(0, POPULATION_SIZE - 1))
    # FILL SECOND PARENT RANDOMLY
    for i in range(CHILDREN_SIZE//2):
        par2 = random.randint(0, POPULATION_SIZE - 1)
        # ENSURE NO PAIR GETS SELECTED TWICE
        while ((parent_1[i], par2) in ret or (par2, parent_1[i]) in ret or parent_1[i] == par2):
            par2 = random.randint(0, POPULATION_SIZE - 1)
        ret.append((parent_1[i], par2))
    return ret

# CROSSOVER FUNCTION


def K_point_crossover(vec1, vec2, crossoverprob, VECTOR_SIZE=11):
    # MAKE A COPY OF BOTH THE VECTORS
    ret1 = np.copy(vec1)
    ret2 = np.copy(vec2)
    for i in range(VECTOR_SIZE):
        x = random.random()
        # EXHANGE A PARTICULAR INDEX WITH GIVEN PROBABILITY
        if x <= crossoverprob:
            ret1[i] = vec2[i]
            ret2[i] = vec1[i]
    return ret1, ret2


def mutate_single(val, mul_range, add_range):
    return val * (random.uniform(-mul_range, mul_range) + 1) + random.uniform(-add_range, add_range)

# MUTATION FUNCTION


def mutate(vec, generation, VECTOR_SIZE=11):
    for i in range(0, VECTOR_SIZE):
        x = random.random()
        # MUTATE A PARTICULAR INDEX WITH A GIVEN PROBABILITY
        if x <= max(0.2, 0.4 - (generation/100)):
            vec[i] = mutate_single(vec[i], 0.1, 1e-18)
    return vec

# SELECTION FUNCTION


def select(children, POPULATION_SIZE, CHILDREN_SIZE):
    values = []
    for i in range(CHILDREN_SIZE):
        values.append(children[i]["child"])
    # SORT BY FITNESS
    values = sorted(values, key=lambda i: fitness(i["results"]))
    ret = []
    for i in range(POPULATION_SIZE):
        ret.append(values[i])
    return ret


def main():
    POPULATION_SIZE = 16
    CHILDREN_SIZE = 20

    mating_pool = []

    ##################### SELECT INITIAL POPULATION #####################
    with open(F_INIT_POPULATION) as f:
        here = json.load(f)
        mating_pool = here["mating_pool"]
    #####################################################################

    for generation in range(1, NUM_GENERATIONS + 1):
        ################## GET PARENTS FROM MATING POOL #################
        parents = get_mating_pool(POPULATION_SIZE, CHILDREN_SIZE)
        #################################################################

        ################## GET CHILDREN FROM CROSSOVER ##################
        children = []
        for i in range(len(parents)):
            child1, child2 = K_point_crossover(
                np.array(mating_pool[parents[i][0]]["vector"]), np.array(mating_pool[parents[i][1]]["vector"]), N=min(6, 3+generation/10))
            children.append({"child": child1, "parents": [
                            mating_pool[parents[i][0]], mating_pool[parents[i][1]]]})
            children.append({"child": child2, "parents": [
                            mating_pool[parents[i][0]], mating_pool[parents[i][1]]]}
                            )
        #################################################################

        ############################ DO MUTATIONS #######################
        for i in range(len(children)):
            children[i]["child"] = mutate(children[i]["child"], generation)
        #################################################################

        ############################ GET ERRORS #########################
        errors = []
        for child in children:
            res = get_errors(TEAM_KEY, child["child"].tolist())
            child["child"] = {
                "vector": child["child"].tolist(), "results": res}
            errors.append({"vector": child, "results": res})
        ##################################################################

        ########################### DUMP CHILDREN ########################
        with open(F_DUMP_FILE) as f:
            oldres = json.load(f)
            oldres = oldres["generations"]
            oldres.append({"generation": generation, "vectors": errors})
            oldres = {"generations": oldres}
            with open(F_DUMP_FILE) as f:
                json.dump(oldres, f)
        ###################################################################

        ################################ SELECTION ########################
        mating_pool = select(children, POPULATION_SIZE, CHILDREN_SIZE)
        ###################################################################


if __name__ == '__main__':
    main()
