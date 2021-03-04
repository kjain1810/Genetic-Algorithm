from client import submit

TEAM_KEY = "prTwq7vUkLegXASklNtVBIA7O8YxRRbYQE8LAnsDrmrx6A0fH1"


def submit_vector():
    best_vec = []
    # GET THE VALUE HERE
    best_vec = [-1.5900117634696895e-18, -1.1089152508024613e-12, -2.5448264472393646e-13, 5.156495819895334e-11, -1.4685999507818116e-10, -
                1.7336464013051853e-15, 7.588385881788844e-16, 2.7525165125385616e-05, -1.8852756204130466e-06, -1.5953841373151045e-08, 8.741325830954951e-10]

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
