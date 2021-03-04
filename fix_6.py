import json

with open("new_new_gen_8.json") as lmao:
    res = json.load(lmao)

final = {"generations": []}

for gen in res["generations"]:
    # here = {"vectors": []}
    here = []
    for vec in gen["vectors"]:
        topush = {
            # "vector": {
            "child": vec["vector"]["child"]["vector"],
            "parents": vec["vector"]["parents"]
            # }
        }
        here.append(
            {"vector": topush, "results": vec["vector"]["child"]["results"]})
    final["generations"].append(
        {"generation": gen["generation"], "vectors": here})

with open("fixed_8.json", "w+") as lmao:
    json.dump(final, lmao)
