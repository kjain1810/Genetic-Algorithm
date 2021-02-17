import json

with open("./init_vecs.json") as f:
    results = json.load(f)

results = results["vectors"]

results = [result for result in results if result["val_error"] <= 1e15]

results = {"vectors": results}

with open("./init_vecs.json", "w") as f:
    json.dump(results, f)
