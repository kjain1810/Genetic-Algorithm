import numpy as np
import random


def crossover(vec1, vec2):
    return (vec1 + vec2)


def point_crossover(vec1, vec2, crossoverpoint, VECTOR_SIZE=11):
    # KEEP CROSSOVER POINT >8 COZ PEHLE 5 USELESS VECTORS HAI RIGHT NOW LOL
    # DECENT
    ret1 = np.copy(vec1)
    ret2 = np.copy(vec2)
    for i in range(int(crossoverpoint), VECTOR_SIZE):
        ret1[i] = vec2[i]
        ret2[i] = vec1[i]
    return ret1, ret2


def K_point_crossover(vec1, vec2, crossoverprob, VECTOR_SIZE=11):
    # BEKAAR
    # print(vec1, vec2)
    ret1 = np.copy(vec1)
    ret2 = np.copy(vec2)
    for i in range(VECTOR_SIZE):
        x = random.random()
        if x <= crossoverprob:
            ret1[i] = vec2[i]
            ret2[i] = vec1[i]
    return ret1, ret2


def average_crossover(vec1, vec2):
    # BAD, ALREADY TRIED, WRITING FOR LULZ
    return (vec1 + vec2) / 2


def BSC(vec1, vec2, N=3, VECTOR_SIZE=11):
    ret1 = np.zeros(11)
    ret2 = np.zeros(11)
    x = random.random()
    if x < 0.5:
        b = (2 * x) ** ((N + 1) ** -1)
    else:
        b = ((2 * (1 - x)) ** -1) ** ((N + 1) ** -1)
    ret1 = ((1 + b) * vec1 + (1 - b) * vec2) / 2
    ret2 = ((1 - b) * vec1 + (1 + b) * vec2) / 2
    return ret1, ret2
