import random
import csv
import matplotlib
import seaborn

def MCSUC_vs_ALLD():
    payoff_matrix_MCSUC_vs_ALLD = [[[5.946532, 2.760259],
                                     [2.761214, 2.760471]]]
    payoff_matrix_MCSUC_vs_HardMajority = [[[5.946532, 5.960563],
                                             [5.959303, 2.919953]]]
    payoff_matrix_MCSUC_vs_TFT = [[[5.946532, 4.975173],
                                    [4.975183, 4.999251]]]
    payoff_matrix_MCSUC_vs_GTFT0_3 = [[[5.946532, 5.798873],
                                        [5.798881, 5.805851]]]
    payoff_matrix_MCSUC_vs_WSLS = [[[5.946532,5.005695],
                      [5.005706,5.384411]]]
    payoff_matrix_MCSUC_vs_ALLC = [[[5.946532,5.960639],
                      [5.959277,5.959938]]]
    payoff_matrix_MCSUC_vs_CIC = [[[5.946532,4.236282],
                      [4.236297,4.912123]]]
    payoff_matrix_MCSUC_vs_CURE2 = [[[5.946532,5.939707],
                      [5.939704,5.946035]]]
    payoff_matrix_MCSUC_vs_Generous_independent = [[[5.739778, 5.467655],
                      [5.467662, 5.353776]]]
    payoff_matrix_MCSUC_vs_Extort2_independent = [[[5.739778, 3.715398],
                      [3.715414, 3.640329]]]

    stra = 8

    if stra == 0:
        payoff_matrix = payoff_matrix_MCSUC_vs_ALLD
        f = open("./data/SD_MCSUC_vs_ALLD_error=0.1.csv", 'a', newline='')
    elif stra == 1:
        f = open("./data/SD_MCSUC_vs_HardMajority_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_HardMajority
    elif stra == 2:
        f = open("./data/SD_MCSUC_vs_TFT_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_TFT
    elif stra == 3:
        f = open("data/SD_MCSUC_vs_GTFT_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_GTFT0_3
    elif stra == 4:
        f = open("data/SD_MCSUC_vs_WSLS_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_WSLS
    elif stra == 5:
        f = open("data/SD_MCSUC_vs_ALLC_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_ALLC
    elif stra == 6:
        f = open("data/SD_MCSUC_vs_CIC_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_CIC
    elif stra == 7:
        f = open("data/SD_MCSUC_vs_CURE2_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_CURE2
    elif stra == 8:
        f = open("data/SD_MCSUC_vs_Generous_independent_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_Generous_independent
    elif stra == 9:
        f = open("data/SD_MCSUC_vs_Extort2_independent_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_Extort2_independent
    j = 0



    step = 1000000

    writer = csv.writer(f)
    rate = 0.001
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