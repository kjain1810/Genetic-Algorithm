import random


def mutate_single(val, mul_range, add_range):
    return val * (random.uniform(-mul_range, mul_range) + 1) + random.uniform(-add_range, add_range)


def mutate(vec, generation, VECTOR_SIZE=11):
    for i in range(0, VECTOR_SIZE):
        x = random.random()
        if x <= max(0.2, 0.4 - (generation/100)):
            vec[i] = mutate_single(vec[i], 0.1, 1e-18)
    return vec
