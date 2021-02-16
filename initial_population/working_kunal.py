import numpy as np
import random

from .working import get_initial_value


def init_values(POPULATION_SIZE, VECTOR_SIZE=11):
    initial_values = get_initial_value()
    for i in range(POPULATION_SIZE):
        for j in range(VECTOR_SIZE):
            x = random.randint(0, 9)
            if x < 5:  # TUNE
                initial_values[i][j] = 0.0
    return initial_values
