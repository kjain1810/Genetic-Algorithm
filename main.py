import json
import numpy as np
import matplotlib.pyplot as plt
import random
import time
from operator import itemgetter


from client import get_errors, submit
from initial_population.working_kunal import load_inits, init_values, load_prev_gens, get_best_from_all_gens, hand_picked
from crossover.working import K_point_crossover, BSC
from mutation.working import mutate
from fitness_func.working import fitness
from selection.working import select, get_mating_pool, select_from_children

TEAM_KEY = "prTwq7vUkLegXASklNtVBIA7O8YxRRbYQE8LAnsDrmrx6A0fH1"

VECTOR_SIZE = 11
POPULATION_SIZE = 5
overfit_vector = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
                  1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]


random.seed(time.time())


def explore():
    INDEX_EXPLORING = 10
    here = get_best_from_all_gens(1)[0]
    best_vec = here["vector"]
    orig_res = here["results"]
    print(orig_res[0]/1e11, orig_res[1]/1e11)
    values = []
    for i in range(-5, 5):
        if i == 0:
            continue
        copied = [j for j in best_vec]
        toadd = i * 1e-15
        copied[INDEX_EXPLORING] += toadd
        # res = [0, 0]
        res = get_errors(TEAM_KEY, copied)
        print(i, res[0]/1e11, res[1]/1e11,
              (fitness(res) - fitness(orig_res))/1e11)
        values.append({"index": INDEX_EXPLORING,
                       "difference": toadd, "results": res})
    with open("exploring.json") as f:
        oldvals = json.load(f)
    for val in values:
        oldvals["explorations"].append(val)
    with open("exploring.json", "w") as f:
        json.dump(oldvals, f)


def main():
    POPULATION_SIZE = 16
    CHILDREN_SIZE = 20

    # CREATE MATING POOL ON ITS OWN
    mating_pool = hand_picked()

    for generation in range(1, 36):
        print("Generation", generation)

        # SELECT PARENTS
        parents = get_mating_pool(POPULATION_SIZE, CHILDREN_SIZE)

        # DO CROSSOVER OF PARENTS
        children = []
        for i in range(len(parents)):
            child1, child2 = BSC(
                np.array(mating_pool[parents[i][0]]["vector"]), np.array(mating_pool[parents[i][1]]["vector"]), N=min(6, 3+generation/10))
            children.append({"child": child1, "parents": [
                            mating_pool[parents[i][0]], mating_pool[parents[i][1]]]})
            children.append({"child": child2, "parents": [
                            mating_pool[parents[i][0]], mating_pool[parents[i][1]]]})
        #     print(np.linalg.norm(child1 - np.array(
        #         mating_pool[parents[i][0]]["vector"])), np.linalg.norm(child1 - np.array(mating_pool[parents[i][1]]["vector"])))
        #     print(np.linalg.norm(child2 - np.array(
        #         mating_pool[parents[i][0]]["vector"])), np.linalg.norm(child2 - np.array(mating_pool[parents[i][1]]["vector"])))
        #     print("")
        # # DO MUTATIONS ON CHILDREN
        for i in range(len(children)):
            children[i]["child"] = mutate(children[i]["child"], generation)

        # GET ERRORS
        errors = []
        for child in children:
            res = [0, 0]
            # res = get_errors(TEAM_KEY, child["child"].tolist())
            print(res[0]/1e11, res[1]/1e11, fitness(res))
            child["child"] = {
                "vector": child["child"].tolist(), "results": res}
            errors.append({"vector": child, "results": res})

        # ADD CHILDREN TO LIST
        with open("new_new_gen_9.json") as f:
            oldres = json.load(f)
        oldres = oldres["generations"]
        oldres.append({"generation": generation, "vectors": errors})
        oldres = {"generations": oldres}
        with open("new_new_gen_9.json", "w") as f:
            json.dump(oldres, f)

        # SELECT BEST CHILDREN
        mating_pool = select_from_children(
            children, POPULATION_SIZE, CHILDREN_SIZE)


def get_best():
    here = get_best_from_all_gens(200)
    here = sorted(here, key=lambda i: fitness(i["results"]))
    for i in range(200):
        if(i==2):
            get_vector_history(here[i]["vector"], here[i]["file"])
            break
        # print(i, here[i]["results"][0]/1e11, here[i]
        #       ["results"][1]/1e11, here[i]["generation"], here[i]["file"])

    # print(here[48])
    # for i in to_select:
    #     print(here[i])

def get_vector_history(vector, file):
    with open(file) as f:
        res = json.load(f)
    res = res["generations"]
    res = sorted(res, key = lambda i: -i["generation"])
    family_vectors = []
    family_vectors.append({"generation": res[0]["generation"], "vector": vector})
    # print(res[0])
    for gen in res:
        for vec in gen["vectors"]:
            if(vec["vector"]["child"] in list(map(itemgetter("vector"), family_vectors))):
                family_vectors.append({"generation": gen["generation"]-1, "vector": vec["vector"]["parents"][0]["vector"]})
                family_vectors.append({"generation": gen["generation"]-1, "vector": vec["vector"]["parents"][1]["vector"]})
    for j in family_vectors:
        print(j["generation"])
if __name__ == '__main__':
    # main()
    # experiment()
    # explore()
    get_best()
