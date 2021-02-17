import numpy as np
from numpy import random

given_data = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
              1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]
given_data = np.array(given_data)
mean = np.mean(given_data)
# print(mean)
# using mean and variance for the given data is useless


# def get_initial_value(POPULATION_SIZE, VECTOR_SIZE=11):
#     initial_values = []
#     for i in range(POPULATION_SIZE):
#         temp = []
#         for j in range(VECTOR_SIZE):
#             random_power = np.random.randint(-12, -3)
#             random_number = np.random.random()*2 - 1
#             temp.append(random_number*(10**random_power))
#         initial_values.append(temp)

#     return initial_values

def get_initial_value(POPULATION_SIZE, VECTOR_SIZE = 11):
    initial_value = []
    for i in range(POPULATION_SIZE):
        temp = []
        for j in range(VECTOR_SIZE):
            trial = given_data[j]
            power = np.floor(np.log10(np.abs(trial)))
            randomNumber = ((np.random.random()*2) - 1)* 10
            temp.append(trial*(np.random.random()*2 - 1) + (randomNumber)*(10**power))
        initial_value.append(temp)
    return initial_value

