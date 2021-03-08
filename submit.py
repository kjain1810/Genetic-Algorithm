from client import submit
from initial_population.working_kunal import load_to_submit

TEAM_KEY = "prTwq7vUkLegXASklNtVBIA7O8YxRRbYQE8LAnsDrmrx6A0fH1"


def submit_vector():
    # best_vec = []
    # GET THE VALUE HERE
    best_vecs = [{'vector': [-1.5900117634696895e-18, -1.1089152508024613e-12, -2.5448264472393646e-13, 5.156495819895334e-11, -1.4685999507818116e-10, -1.7336464013051853e-15, 7.588385881788844e-16, 2.7525165125385616e-05, -1.8852756204130466e-06, -1.5953841373151045e-08, 8.741325830954951e-10], 'results': [116101460426.6661, 87860031424.50586], 'generation': 32}
                 ]
    i = 0
    f = open("last_vector_8th.txt", "a")
    for best_vec in best_vecs:
        # break
        x = submit(TEAM_KEY, best_vec["vector"])
        print(x)
        rank = input()
        # SAVING THE VECTOR IN LAST VECTOR
        f.write(str(best_vec))
        f.write("\n")
        f.write(rank)
        f.write("\n")
    # IF THIS VECTOR GETS THE BEST RANK YET, DO:
    # bash save_this_vector.sh
    f.close()


if __name__ == "__main__":
    submit_vector()
