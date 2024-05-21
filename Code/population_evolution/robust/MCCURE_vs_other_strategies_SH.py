import random
import csv
import matplotlib
import seaborn

def MCSUC_vs_ALLD():
    payoff_matrix_MCSUC_vs_ALLD = [[[5.119515, 2.039550],
                                     [2.040705, 2.040058]]]
    payoff_matrix_MCSUC_vs_HardMajority = [[[5.119515, 5.239677],
                                             [5.238192, 2.039942]]]
    payoff_matrix_MCSUC_vs_TFT = [[[5.119515, 3.022686],
                                    [3.022697, 2.999324]]]
    payoff_matrix_MCSUC_vs_GTFT0_3 = [[[5.119515, 4.433616],
                                        [4.433623, 4.43036]]]
    payoff_matrix_MCSUC_vs_WSLS = [[[5.119515,3.025657],
                      [3.025665,4.663821]]]
    payoff_matrix_MCSUC_vs_ALLC = [[[5.119515,5.239147],
                      [5.237875,5.239751]]]
    payoff_matrix_MCSUC_vs_CIC = [[[5.119515,2.312968],
                      [2.312983,4.191117]]]
    payoff_matrix_MCSUC_vs_CURE2 = [[[5.119515,5.069888],
                      [5.069889,5.116313]]]
    payoff_matrix_MCSUC_vs_Generous_independent = [[[5.739778, 3.873257],
                      [3.873267, 4.046682]]]
    payoff_matrix_MCSUC_vs_Extort2_independent = [[[5.739778, 2.316991],
                      [2.317007, 2.432526]]]

    stra = 1

    if stra == 0:
        payoff_matrix = payoff_matrix_MCSUC_vs_ALLD
        f = open("./data/SH_MCSUC_vs_ALLD_error=0.1.csv", 'a', newline='')
    elif stra == 1:
        f = open("./data/SH_MCSUC_vs_HardMajority_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_HardMajority
    elif stra == 2:
        f = open("./data/SH_MCSUC_vs_TFT_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_TFT
    elif stra == 3:
        f = open("data/SH_MCSUC_vs_GTFT_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_GTFT0_3
    elif stra == 4:
        f = open("data/SH_MCSUC_vs_WSLS_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_WSLS
    elif stra == 5:
        f = open("data/SH_MCSUC_vs_ALLC_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_ALLC
    elif stra == 6:
        f = open("data/SH_MCSUC_vs_CIC_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_CIC
    elif stra == 7:
        f = open("data/SH_MCSUC_vs_CURE2_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_CURE2
    elif stra == 8:
        f = open("data/SH_MCSUC_vs_Generous_independent_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_Generous_independent
    elif stra == 9:
        f = open("data/SH_MCSUC_vs_Extort2_independent_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_Extort2_independent

    j = 1
    step = 1000000

    writer = csv.writer(f)

    rate = 0.032
    frequency = [rate, 1-rate]
    for i in range(step):

        fitness_MCSUC = 0
        fitness_MCSUC += frequency[0] * payoff_matrix[j][0][0]
        fitness_MCSUC += frequency[1] * payoff_matrix[j][0][1]

        fitness_ALLD = 0
        fitness_ALLD += frequency[0] * payoff_matrix[j][1][0]
        fitness_ALLD += frequency[1] * payoff_matrix[j][1][1]

        overall_fitness = frequency[0] * fitness_MCSUC + frequency[1] * fitness_ALLD

        frequency[0] = frequency[0] * fitness_MCSUC / overall_fitness
        frequency[1] = frequency[1] * fitness_ALLD / overall_fitness


        if (random.random() < 0.1):
            mutation(frequency)


        writer.writerow(frequency)
        if (i % 1000 == 0):
            print('step:', i, frequency)


    f.close()


def mutation(frequency):
    if random.random() > 0.5:
        num = 0
    else:
        num = 1
    for i in range(len(frequency)):
        if i != num:
            frequency[num] = frequency[num] * 0.999
        else:
            frequency[num] = frequency[num] + 0.001


if __name__ == "__main__":
    MCSUC_vs_ALLD()