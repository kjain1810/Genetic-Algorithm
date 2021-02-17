import numpy as np
import random
import time

# from .working import get_initial_value

given_data = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
              1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]


def init_values(POPULATION_SIZE, VECTOR_SIZE=11):
    initial_values = []
    for i in range(POPULATION_SIZE):
        here = []
        for j in range(len(given_data)):
            here.append(given_data[j])
        initial_values.append(here)
    random.seed(time.time())
    for i in range(POPULATION_SIZE):
        for j in range(VECTOR_SIZE):
            # x = random.uniform(-1e-12, 1e-12)
            x = random.random()
            if x < 0.6:  # TUNE
                y = random.uniform(-1e-15, 1e-15)
                if abs(initial_values[i][j] + y) <= 10:
                    initial_values[i][j] += y
                #     initial_values[i][j] = 0.0
                # else:
                factor = random.random() * 0.002 + 0.999
                if abs(initial_values[i][j] * factor) <= 10:
                    initial_values[i][j] *= factor
    return initial_values


if __name__ == "__main__":
    print(init_values(20))
    # init_values(20)
