import random
import csv
import matplotlib
import seaborn

def MCSUC_vs_strategy():
    # tbe payoff matrix records the payoff obtained from codes in 'game_reward_coop_between_2_players'.
    payoff_matrix_MCSUC_vs_ALLD = [[[5.739778, 2.579176],
                                     [2.581511, 2.580071]]]
    payoff_matrix_MCSUC_vs_HardMajority = [[[5.739778, 5.780514],
                                             [5.778723, 2.580387]]]
    payoff_matrix_MCSUC_vs_TFT = [[[5.739778, 4.488947],
                                    [4.488966, 4.500408]]]
    payoff_matrix_MCSUC_vs_GTFT0_3 = [[[5.739778, 5.457340],
                                        [5.457349, 5.462084]]]
    payoff_matrix_MCSUC_vs_WSLS = [[[5.739778,4.511165],
                      [4.511184,5.203941]]]
    payoff_matrix_MCSUC_vs_ALLC = [[[5.739778,5.780989],
                      [5.778601,5.779964]]]
    payoff_matrix_MCSUC_vs_CIC = [[[5.739778,3.755501],
                      [3.755490,4.732227]]]
    payoff_matrix_MCSUC_vs_CURE2 = [[[5.739778,5.721948],
                      [5.721944,5.73866]]]
    payoff_matrix_MCSUC_vs_Generous_independent = [[[5.739778, 5.067884],
                      [5.067896, 5.027988]]]
    payoff_matrix_MCSUC_vs_Extort2_independent = [[[5.739778, 3.365560],
                      [3.365583, 3.338001]]]

    stra = 0

    # decide which one is opponent strategy
    if stra == 0:
        payoff_matrix = payoff_matrix_MCSUC_vs_ALLD
        f = open("./data/MCSUC_vs_ALLD_error=0.1.csv", 'a', newline='')
    elif stra == 1:
        f = open("./data/MCSUC_vs_HardMajority_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_HardMajority
    elif stra == 2:
        f = open("./data/MCSUC_vs_TFT_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_TFT
    elif stra == 3:
        f = open("data/MCSUC_vs_GTFT_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_GTFT0_3
    elif stra == 4:
        f = open("data/MCSUC_vs_WSLS_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_WSLS
    elif stra == 5:
        f = open("data/MCSUC_vs_ALLC_999_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_ALLC
    elif stra == 6:
        f = open("data/MCSUC_vs_CIC_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_CIC
    elif stra == 7:
        f = open("data/MCSUC_vs_CURE2XX_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_CURE2
    elif stra == 8:
        f = open("data/MCSUC_vs_Generous_independent_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_Generous_independent
    elif stra == 9:
        f = open("data/MCSUC_vs_Extort2_independent_error=0.1.csv", 'a', newline='')
        payoff_matrix = payoff_matrix_MCSUC_vs_Extort2_independent
    j = 0

    print(payoff_matrix)

    # simulation steps
    step = 1000000

    writer = csv.writer(f)
    # inital rate of MCSUC
    rate = 0.495
    frequency = [rate, 1-rate]
    for i in range(step):
        # Nowak and Sigmund’s approach to calculate fitness
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
    MCSUC_vs_strategy()