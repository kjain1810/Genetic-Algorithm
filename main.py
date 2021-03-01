import json

import numpy as np
import matplotlib.pyplot as plt

from client import get_errors
from initial_population.working_kunal import load_inits, init_values, load_prev_gens, get_best_from_all_gens
from crossover.working import K_point_crossover, BSC
from mutation.working import mutate
from fitness_func.working import fitness
from selection.working import select, get_mating_pool

TEAM_KEY = "prTwq7vUkLegXASklNtVBIA7O8YxRRbYQE8LAnsDrmrx6A0fH1"

VECTOR_SIZE = 11
POPULATION_SIZE = 5
overfit_vector = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
                  1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]


# TODO: cross BSC results with K-point
# TODO: cross K-point with BSC
# TODO: take best of k point and bsc, do k point with them

def main():
    inits = get_best_from_all_gens(100)
    for i in inits:
        print(i["results"][0]/1e11, i["results"][1]/1e11, np.linalg.norm(np.array(i["vector"]) - np.array(overfit_vector)))

# def main():
#     # init = load_inits(30)
#     temp_init = load_prev_gens("new_gen_2.json", 31)[0]
#     POPULATION_SIZE = 16
#     # print(len(init_temp))
#     init = []
#     for i in temp_init:
#         init.append({"vector": i["vector"]["child"]})
#     # mating_pool = select(init, POPULATION_SIZE)
#     mating_pool = init
#     init = [vec for vec in init if vec not in mating_pool]
#     dists = []
#     for generation in range(1, 16):
#         print(len(init))
#         # print(len(mating_pool))
#         print("Generation", generation)
#         # SELECT PARENTS
#         parents = get_mating_pool(POPULATION_SIZE)
#         # DO CROSSOVER OF PARENTS
#         children = []
#         for i in range(len(parents)):
#             child1, child2 = BSC(
#                 np.array(mating_pool[parents[i][0]]["vector"]), np.array(mating_pool[parents[i][1]]["vector"]), N=6+(31+generation)/20)
#             children.append({"child": child1, "parents": [
#                             mating_pool[parents[i][0]], mating_pool[parents[i][1]]]})
#             children.append({"child": child2, "parents": [
#                             mating_pool[parents[i][0]], mating_pool[parents[i][1]]]})
#         # DO MUTATIONS ON CHILDREN
#         for i in range(len(children)):
#             children[i]["child"] = mutate(children[i]["child"])
#         # GET ERRORS
#         errors = []
#         for child in children:
#             # res = [0, 0]
#             res = get_errors(TEAM_KEY, child["child"].tolist())
#             print(res[0]/1e11, res[1]/1e11,
#                   np.linalg.norm(child["child"] - np.array(overfit_vector)))
#             child["child"] = child["child"].tolist()
#             errors.append({"vector": child, "results": res})
#             init.append({"vector": child["child"], "results": res})
#         # ADD CHILDREN TO LIST
#         with open("new_gen_4.json") as f:
#             oldres = json.load(f)
#         oldres = oldres["generations"]
#         oldres.append({"generation": generation+31, "vectors": errors})
#         oldres = {"generations": oldres}
#         with open("new_gen_4.json", "w") as f:
#             json.dump(oldres, f)
#         mating_pool = select(init, POPULATION_SIZE)
#         init = [vec for vec in init if vec not in mating_pool]


def main1():
    vecs = load_inits(3)
    with open("./generations.json") as f:
        otp = json.load(f)
        otp = otp["results"]

    # DO GENETIC ALGO
    results = []
    for i in range(3):
        for j in range(i+1, 3):
            # x1, x2 = BSC(vecs[i], vecs[j])
            x1, x2 = K_point_crossover(vecs[i], vecs[j], 0.5, 8)
            x1 = mutate(x1)
            x2 = mutate(x2)
            # print(x1)
            # print(x2)
            # print("")
            res1 = get_errors(TEAM_KEY, x1.tolist())
            res2 = get_errors(TEAM_KEY, x2.tolist())
            results.append({"vector": x1.tolist(), "results": res1})
            results.append({"vector": x2.tolist(), "results": res2})
            print(res1[0]/1e11, res1[1]/1e11, x1)
            print(res2[0]/1e11, res2[1]/1e11, x2)
            print("")
    results = {"generation": 3, "vectors": results, "parents": []}
    for i in range(3):
        results["parents"].append(vecs[i].tolist())
    otp.append(results)
    otp = {"results": otp}
    with open("./generations.json", "w") as f:
        json.dump(otp, f)


def main2():
    # myvecs = [overfit_vector * 2]
    myvecs = init_values(POPULATION_SIZE, VECTOR_SIZE)
    with open("./init_vecs.json") as f:
        results = json.load(f)
    # print(myvecs)
    for vec in myvecs:
        # print(vec)
        res = get_errors(TEAM_KEY, vec)
        results["vectors"].append({
            "vector": vec,
            "train_error": res[0],
            "val_error": res[1]
        })
        print(res, vec)
    with open("./init_vecs.json", "w") as f:
        json.dump(results, f)


if __name__ == '__main__':
    main()
    # experiment()
