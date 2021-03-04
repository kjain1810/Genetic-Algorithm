from client import submit

TEAM_KEY = "prTwq7vUkLegXASklNtVBIA7O8YxRRbYQE8LAnsDrmrx6A0fH1"


def submit_vector():
    best_vec = []
    # GET THE VALUE HERE
    best_vec = [-2.2039910365639575e-19, -1.2947992095069348e-12, 1.0768417154689328e-07, -8.458011557930416e-05, -1.635282670676313e-10, -1.4191725413142035e-15, 9.179444207255541e-16, 2.4860215202029475e-05, -1.8225209312478627e-06, -1.6009993279441546e-08, 8.741325830954951e-10]

    x = submit(TEAM_KEY, best_vec)
    print(x)
    # SAVING THE VECTOR IN LAST VECTOR
    f = open("last_vector.txt", "w")
    f.write('[')
    for i in range(len(best_vec)):
        f.write(str(format(best_vec[i], '0.60g')))
        if i != 10:
            f.write(',')
    f.write(']')
    # IF THIS VECTOR GETS THE BEST RANK YET, DO:
    # bash save_this_vector.sh


if __name__ == "__main__":
    submit_vector()
