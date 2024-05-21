import random
import csv
import matplotlib
import seaborn
import sys
sys.path.append("..")
import os
import numpy as np

def evolution_population():
    # payoff_matrix=[
    #     [
    #         5.739778, 5.780989, 2.579345
    #     ],
    #     [
    #         5.778601, 5.780056, 0.820075
    #      ],
    #     [
    #         2.581763, 8.820590, 2.580071
    #     ]
    #
    # ]

    payoff_matrix=[

        [
            5.780056, 0.820075
         ],
        [
            8.820590, 2.580071
        ]

    ]
    print(payoff_matrix)


    f = open("./data/evolution_ALLC_ALLD_frequncey.csv", 'a', newline='')

    strategies_number = 2
    init_frequency = 1 / strategies_number
    frequency = [0.999,0.001]

    step = 1000000

    writer = csv.writer(f)
    writer.writerow(frequency)
    for i in range(step):
        fitness_strategies = [0 for i in range(strategies_number)]
        overall_fitness = 0
        for j in range(strategies_number):
            for k in range(strategies_number):
                fitness_strategies[j] += frequency[k] * payoff_matrix[j][k]
            overall_fitness += frequency[j] * fitness_strategies[j]
        for j in range(strategies_number):
            frequency[j] = frequency[j] * fitness_strategies[j] / overall_fitness


        if (random.random() < 0.1):
            mutation(frequency,strategies_number)

        writer.writerow(frequency)
        if (i % 1000 == 0):
            print('step:', i, frequency,fitness_strategies)
    f.close()



def mutation(frequency,strategies_number):
    random_number = random.randint(0, strategies_number - 1)

    for i in range(strategies_number):
        if i != random_number:
            frequency[i] = frequency[i] * 0.999
        else:
            frequency[i] = frequency[i] + 0.001


if __name__ == "__main__":
    evolution_population()