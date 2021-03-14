import json
import random
import time
import numpy as np

from client import get_errors

random.seed(time.time())

TEAM_KEY = "prTwq7vUkLegXASklNtVBIA7O8YxRRbYQE8LAnsDrmrx6A0fH1"

VECTOR_SIZE = 11
POPULATION_SIZE = 5
overfit_vector = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
                  1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]

F_INIT_POPULATION = "mating_pool.json"
F_DUMP_FILE = "dump.json"
NUM_GENERATIONS = 35

# FITNESS FUNCTION


def fitness(res, FACTOR=1.0):
    return FACTOR * res[0] + res[1]

# MATING POOL FUNCTION


def get_mating_pool(POPULATION_SIZE, CHILDREN_SIZE):
    ret = []
    parent_1 = []
    # ENSURES ALL PARENTS GET INVOLVED IN ATLEAST 1 CHILD
    for i in range(POPULATION_SIZE // 2):
        parent_1.append(i)
    # FILL THE REMAINING FIRST PARENTS RANDOMLY
    for i in range((CHILDREN_SIZE - POPULATION_SIZE) // 2):
        parent_1.append(random.randint(0, POPULATION_SIZE - 1))
    # FILL SECOND PARENT RANDOMLY
    for i in range(CHILDREN_SIZE//2):
        par2 = random.randint(0, POPULATION_SIZE - 1)
        # ENSURE NO PAIR GETS SELECTED TWICE
        while ((parent_1[i], par2) in ret or (par2, parent_1[i]) in ret or parent_1[i] == par2):
            par2 = random.randint(0, POPULATION_SIZE - 1)
        ret.append((parent_1[i], par2))
    return ret

# CROSSOVER FUNCTION


def K_point_crossover(vec1, vec2, crossoverprob, VECTOR_SIZE=11):
    # MAKE A COPY OF BOTH THE VECTORS
    ret1 = np.copy(vec1)
    ret2 = np.copy(vec2)
    for i in range(VECTOR_SIZE):
        x = random.random()
        # EXHANGE A PARTICULAR INDEX WITH GIVEN PROBABILITY
        if x <= crossoverprob:
            ret1[i] = vec2[i]
            ret2[i] = vec1[i]
    return ret1, ret2


def mutate_single(val, mul_range, add_range):
    return val * (random.uniform(-mul_range, mul_range) + 1) + random.uniform(-add_range, add_range)

# MUTATION FUNCTION


def mutate(vec, generation, VECTOR_SIZE=11):
    for i in range(0, VECTOR_SIZE):
        x = random.random()
        # MUTATE A PARTICULAR INDEX WITH A GIVEN PROBABILITY
        if x <= max(0.2, 0.4 - (generation/100)):
            vec[i] = mutate_single(vec[i], 0.1, 1e-18)
    return vec

# SELECTION FUNCTION


def select(children, POPULATION_SIZE, CHILDREN_SIZE):
    values = []
    for i in range(CHILDREN_SIZE):
        values.append(children[i]["child"])
    # SORT BY FITNESS
    values = sorted(values, key=lambda i: fitness(i["results"]))
    ret = []
    for i in range(POPULATION_SIZE):
        ret.append(values[i])
    return ret


def main():
    POPULATION_SIZE = 16
    CHILDREN_SIZE = 20

    mating_pool = []
    overalls = []

    ##################### SELECT INITIAL POPULATION #####################
    with open(F_INIT_POPULATION) as f:
        here = json.load(f)
        mating_pool = here["mating_pool"]
    #####################################################################

    for generation in range(1, NUM_GENERATIONS + 1):
        print(generation)
        ################## GET PARENTS FROM MATING POOL #################
        parents = get_mating_pool(POPULATION_SIZE, CHILDREN_SIZE)
        #################################################################

        ################## GET CHILDREN FROM CROSSOVER ##################
        children = []
        for i in range(len(parents)):
            child1, child2 = K_point_crossover(
                np.array(mating_pool[parents[i][0]]["vector"]), np.array(mating_pool[parents[i][1]]["vector"]), crossoverprob=min(0.8, 0.5 + generation/100))
            children.append({"child": child1, "parents": [
                            mating_pool[parents[i][0]], mating_pool[parents[i][1]]]})
            children.append({"child": child2, "parents": [
                            mating_pool[parents[i][0]], mating_pool[parents[i][1]]]}
                            )
        #################################################################

        ############################ DO MUTATIONS #######################
        for i in range(len(children)):
            children[i]["child"] = mutate(children[i]["child"], generation)
        #################################################################

        ############################ GET ERRORS #########################
        errors = []
        for child in children:
            res = [random.rand(), random.rand()]
            # UNCOMMENT TO MAKE QUERIES!!
            # res = get_errors(TEAM_KEY, child["child"].tolist())
            child["child"] = {
                "vector": child["child"].tolist(), "results": res}
            errors.append({"vector": child, "results": res})
            overalls.append(
                {"vector": child["child"]["vector"], "result": res})
        ##################################################################

        ########################### DUMP CHILDREN ########################
        with open(F_DUMP_FILE) as f:
            oldres = json.load(f)
            oldres = oldres["generations"]
            oldres.append({"generation": generation, "vectors": errors})
            oldres = {"generations": oldres}
            with open(F_DUMP_FILE, "w") as f:
                json.dump(oldres, f)
        ###################################################################

        ################################ SELECTION ########################
        mating_pool = select(children, POPULATION_SIZE, CHILDREN_SIZE)
        ###################################################################


if __name__ == '__main__':
    main()
    overalls = [[-1.5255075089406534e-19, -1.4130890469184774e-12, -2.417466014489163e-13, 5.3195661061779506e-11, -1.4657972126516002e-10, -1.823887947537584e-15, 9.789206723171945e-16, 2.30807526576702e-05, -1.8018325565881513e-06, -1.3465706038939896e-08, 8.289022217323264e-10], [-7.966187402840873e-19, -0.013204533000542, -2.0710898066648007e-13, 5.260402701064849e-11, -1.2872142124720997e-10, -1.7107248211502951e-15, 8.840773765420747e-16, 2.720562981886773e-05, -1.916896672295187e-06, -1.481786495663743e-08, 8.70219246690817e-10], [2.500142901185707e-18, -1.446045689005307e-12, -2.1262310489704696e-13, 6.028821130082867e-11, -1.5634210864666434e-10, -2.0432227066643857e-15, 9.2699028899782e-16, 2.507909059926704e-05, -2.049523772151163e-06, -1.4651921077177198e-08, 9.451988173508219e-10], [-4.334178830109263e-19, -1.2814583750333733e-12, -2.4132802300937104e-13, 5.413785967254893e-11, -1.5428068830322833e-10, -2.24612271927916e-15, 7.915960478954897e-16, 2.607754777276336e-05, -1.979331949163259e-06, -1.4518488021389094e-08, 9.112082074257866e-10], [-0.01896975566136764, 0.00020270045476877518, -5.968574489236788e-06, 0.0012136671735861085, -1.159754878408517e-10, -1.4711162119525787e-15, 8.718987625041863e-16, 2.9377838253333205e-05, -1.90115107652098e-06, -1.5981658021862748e-08, 8.627817340129648e-10],
                [1.79694767322469e-17, -1.3463149567488761e-12, -2.622698735405157e-13, 3.464463692369948e-11, -1.8495942031979397e-10, -1.4758817178417392e-15, 6.2921260119272845e-16, 2.6808586201629767e-05, -1.9041082629353541e-06, -1.480195471840355e-08, 8.578343062690086e-10], [-0.029358403093566153, 0.0002132398575926024, -6.7173028965879454e-06, 0.0015361479168859952, -1.1860485090045173e-10, -1.3979262689719637e-15, 8.144070593983925e-16, 2.893164767297081e-05, -1.9572851229169965e-06, -1.6152834837410027e-08, 8.913139187587098e-10], [-0.02334370692683367, 0.0001957364304301047, -5.592128139111349e-06, 0.0013277055314681828, -1.21365430050191e-10, -1.4668524700318145e-15, 8.005406501025325e-16, 2.70687896111528e-05, -2.0860007097411178e-06, -1.5984974247845284e-08, 9.537192854189212e-10], [-0.027407942810694065, 0.0002468603264184149, -7.018749143216041e-06, 0.0014839035163197508, -1.4200398662243262e-10, -1.3954008654781276e-15, 8.216245708004078e-16, 2.914224065669245e-05, -1.9525148076357393e-06, -1.652014834325622e-08, 8.939559961813824e-10], [-0.020542303240645703, 0.0001387178887213967, -4.366734776798681e-06, 0.0009981495686919692, -9.480258785509228e-11, -1.956737847068162e-15, 8.541549307654014e-16, 2.8789057215401574e-05, -2.0281469154063015e-06, -1.6124224019498098e-08, 9.325854035703712e-10]]
    with open("output.txt", "w") as f:
        f.write("[\n")
        for i in range(10):
            f.write("\t")
            f.write(str(overalls[i]))
            if i < 9:
                f.write(" ,")
            f.write("\n")
        f.write("]")
        f.close()
