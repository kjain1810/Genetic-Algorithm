import json

with open("./init_vecs.json") as f:
    results = json.load(f)

results = results["vectors"]
results = sorted(results, key=lambda i: i["val_error"])

for res in results:
    print(res["val_error"], res["vector"])
