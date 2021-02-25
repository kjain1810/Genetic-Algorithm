import json
import numpy as np

with open("new_gen_1.json") as f:
    res = json.load(f)

original_given = np.array([
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
]
)

gens_to_save = []

for generation in res["generations"]:
    # print(generation)
    # break
    # x = generation["vectors"][0]["results"]
    for vector in generation["vectors"]:
        # print(vector)
        vec = vector["vector"]["child"]
        print(np.linalg.norm(np.array(vec) - original_given))
# for gen in gens_to_save:
#     print(gen["generation"])

# to_save = {"generations": gens_to_save}

# with open("new_gen_1_.json", "w") as f:
#     json.dump(to_save, f)
