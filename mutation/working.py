import random


def mutate(vec, VECTOR_SIZE=11):
    for i in range(0, VECTOR_SIZE):
        x = random.random()
        if x <= 0.1:
            vec[i] = vec[i] * \
                (random.uniform(-0.1, 0.1) + 1) + random.uniform(-1e-18, 1e-18)
    return vec
