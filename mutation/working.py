import random


def mutate_single(val, mul_range, add_range):
    return val * (random.uniform(-mul_range, mul_range) + 1) + random.uniform(-add_range, add_range)


def mutate(vec, generation, VECTOR_SIZE=11):
    for i in range(0, VECTOR_SIZE):
        x = random.random()
        if x <= max(0.2, 0.4 - (generation/100)):
            if i >= 7 or i == 5 or i == 4:
                vec[i] = mutate_single(vec[i], 0.1, 1e-18)
            elif i == 0:
                vec[i] = mutate_single(vec[i], 0.1, 1e-4)
            elif i == 1:
                vec[i] = mutate_single(vec[i], 0.1, 1e-2)
            elif i == 2:
                vec[i] = mutate_single(vec[i], 0.1, 1e-4)
            elif i == 3:
                vec[i] = mutate_single(vec[i], 0.1, 1e-2)
    return vec
