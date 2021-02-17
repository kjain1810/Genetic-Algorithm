import json
import matplotlib.pyplot as plt

with open("./init_vecs.json") as f:
    vectors = json.load(f)

vectors = vectors["vectors"]
overfit_vector = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
                  1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]


x = []
y = []
xx = 0
yy = 0
for vec in vectors:
    if vec["vector"] == overfit_vector:
        xx = vec["train_error"]
        yy = vec["val_error"]
    if vec["val_error"] < 1e12:
        x.append(vec["train_error"])
        y.append(vec["val_error"])

plt.plot(x, y, 'o')
plt.plot([xx], [yy], 'o', color="red")
plt.xlabel("Training error")
plt.ylabel("Validation error")
plt.show()
