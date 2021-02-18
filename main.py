import json

import numpy as np

from client import get_errors
from initial_population.working_kunal import load_inits
from crossover.working import crossover

TEAM_KEY = "prTwq7vUkLegXASklNtVBIA7O8YxRRbYQE8LAnsDrmrx6A0fH1"

VECTOR_SIZE = 11
POPULATION_SIZE = 10
overfit_vector = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
                  1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]


def main():
    vecs = load_inits(5)
    vec = np.copy(vecs[0])
    for i in range(1, 5):
        vec += vecs[i]
    vec /= 5
    with open("./new_vecs.json") as f:
        results = json.load(f)
        results = results["vectors"]
    res = get_errors(TEAM_KEY, vec.tolist())
    print(res)
    results.append(
        {"vector": vec.tolist(), "train_error": res[0], "val_error": res[1]})
    # reqs = []
    # for vec in vecs:
    #     print(vec)
    # for i in range(len(vecs)):
    #     for j in range(i + 1, len(vecs)):
    #         reqs.append(crossover(vecs[i], vecs[j]))
    # results = []
    # for vec in reqs:
    #     # print(vec)
    #     res = get_errors(TEAM_KEY, vec.tolist())
    #     print(res)
    #     results.append(
    #         {"vector": vec.tolist(), "train_error": res[0], "val_error": res[1]})
    results = {"vectors": results}
    with open("./new_vecs.json", "w") as f:
        json.dump(results, f)


def main2():
    # myvecs = [overfit_vector * 2]
    myvecs = get_initial_value(POPULATION_SIZE, VECTOR_SIZE)
    with open("./init_vecs.json") as f:
        results = json.load(f)
    # print(myvecs)
    for vec in myvecs:
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
