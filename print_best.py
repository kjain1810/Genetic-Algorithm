import json
import numpy as np


def fitness(res, FACTOR=0.7):
    return res[0] * FACTOR + res[1]


def fitness_2(res):
    return 1 / ((res[0] + res[1]) - 2 * abs(res[0] - res[1]))


init = np.array([
    0.0,
    -1.45799022e-12,
    -2.28980078e-13,
    4.62010753e-11,
    -1.75214813e-10,
    -1.83669770e-15,
    8.52944060e-16,
    2.29423303e-05,
    -2.04721003e-06,
    -1.59792834e-08,
    9.98214034e-10
])


with open("./generations.json") as f:
    results = json.load(f)

results = results["results"]

here = []

for x in results:
    # if x["generation"] != 2:
    #     continue
    y = x["vectors"]
    for z in y:
        here.append(z)

here = sorted(here, key=lambda i: fitness(i["results"]))

bests = []

for i in range(60):
    res = here[i]
    bests.append(res)
    x = np.array(res['vector'])
    dist = np.linalg.norm(x-init)
    print(res["results"][0]/1e11, res["results"][1]/1e11, dist)

with open("new_vectors.json", "w") as f:
    json.dump({"vectors": bests}, f)
