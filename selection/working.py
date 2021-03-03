import random
import time

# from fitness_func.working import fitness
from fitness_func.working import fitness
from initial_population.working_kunal import get_best_from_all_gens

random.seed(time.time())


def select(vecs, POPULATION_SIZE):
    vecs = sorted(vecs, key=lambda i: fitness(i["results"]))
    ret = []
    # while len(ret) < POPULATION_SIZE:
    #     x = random.randint(0, POPULATION_SIZE - 1)
    #     while x not in ret:
    #         x = random.randint(0, POPULATION_SIZE - 1)
    #     ret.append(x)
    for i in range(len(vecs)):
        x = random.random()
        # if x <= 0.8:
        ret.append(vecs[i])
        if len(ret) == POPULATION_SIZE:
            break
    return ret


def get_mating_pool(POPULATION_SIZE, CHILDREN_SIZE):
    ret = []
    parent_1 = []
    for i in range(POPULATION_SIZE // 2):
        parent_1.append(i)
    for i in range((CHILDREN_SIZE - POPULATION_SIZE) // 2):
        parent_1.append(random.randint(0, POPULATION_SIZE - 1))
    for i in range(CHILDREN_SIZE//2):
        par2 = random.randint(0, POPULATION_SIZE - 1)
        while ((parent_1[i], par2) in ret or (par2, parent_1[i]) in ret or parent_1[i] == par2):
            par2 = random.randint(0, POPULATION_SIZE - 1)
        ret.append((parent_1[i], par2))
    return ret


'''

parent1: [1, 2, 3, ... 16, rand() x 4] -- 20 numbers
parent2: [rand() x 20] -- 20 numbers

'''


def select_from_children(children, POPULATION_SIZE, CHILDREN_SIZE):
    values = []
    for i in range(CHILDREN_SIZE):
        values.append(children[i]["child"])
    values = sorted(values, key=lambda i: fitness(i["results"]))
    ret = []
    for i in range(POPULATION_SIZE):
        ret.append(values[i])
    return ret
    # print(len(values))


if __name__ == "__main__":
    children = get_best_from_all_gens(20)
    select_from_children(children, 16, 20)
