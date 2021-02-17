import json
import numpy as np

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


with open("./init_vecs.json") as f:
    results = json.load(f)

results = results["vectors"]
results = sorted(results, key=lambda i: i["val_error"])

for res in results:
    x = np.array(res["vector"])
    dist = np.linalg.norm(x-init)
    print(res["val_error"], dist)
