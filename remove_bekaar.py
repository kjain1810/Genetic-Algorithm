import json

with open("new_gen_1.json") as f:
    res = json.load(f)

gens_to_save = []

for generation in res["generations"]:
    x = generation["vectors"][0]["results"]
    if x != [0, 0]:
        gens_to_save.append(generation)

for gen in gens_to_save:
    print(gen["generation"])

to_save = {"generations": gens_to_save}

with open("new_gen_1_.json", "w") as f:
    json.dump(to_save, f)
