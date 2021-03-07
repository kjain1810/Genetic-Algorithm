from client import submit
from initial_population.working_kunal import load_to_submit

TEAM_KEY = "prTwq7vUkLegXASklNtVBIA7O8YxRRbYQE8LAnsDrmrx6A0fH1"


def submit_vector():
    # best_vec = []
    # GET THE VALUE HERE
    best_vecs = load_to_submit()
    i = 0
    f = open("last_vector_7th.txt", "a")
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
        i += 1
    # IF THIS VECTOR GETS THE BEST RANK YET, DO:
    # bash save_this_vector.sh
    f.close()


if __name__ == "__main__":
    submit_vector()
