import json

import numpy as np

from client import get_errors
from initial_population.working_kunal import load_inits, init_values
from crossover.working import point_crossover
from mutation.working import mutate

TEAM_KEY = "prTwq7vUkLegXASklNtVBIA7O8YxRRbYQE8LAnsDrmrx6A0fH1"

VECTOR_SIZE = 11
POPULATION_SIZE = 5
overfit_vector = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
                  1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]


def main():
    vecs = load_inits(3)
    with open("./generations.json") as f:
        otp = json.load(f)
        otp = otp["results"]

    # DO GENETIC ALGO
    results = []
    for i in range(3):
        for j in range(i+1, 3):
            # x1, x2 = BSC(vecs[i], vecs[j])
            x1, x2 = point_crossover(vecs[i], vecs[j], 0.5, 8)
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
