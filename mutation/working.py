import random


def mutate(vec, VECTOR_SIZE=11):
    vec[0] += random.random() * 2 - 1
    for i in range(1, VECTOR_SIZE):
        vec[i] = vec[i] * \
            (random.uniform(-0.1, 0.1) + 1) + random.uniform(-1e-18, 1e-18)
    return vec
