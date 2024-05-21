import random
import sys
sys.path.append("..")
from strategies import CIC
import matplotlib.pyplot as plt


def coo_rate(decision_player):
    "4*1 -> 2*2"
    if decision_player == 0:
        return [1,1]
    if decision_player == 1:
        return [1,0]
    if decision_player == 2:
        return [0,1]
    if decision_player == 3:
        return [0,0]

def game_CIC_vs_CIC():
    step = 1000000
    times = 1000
    epsilon = 0.1

    visit = {}

    sum_all_time_player1_reward1 = 0
    sum_all_time_player1_reward2 = 0
    sum_all_time_player2_reward1 = 0
    sum_all_time_player2_reward2 = 0
    sum_all_time_player1_coo1 = 0
    sum_all_time_player1_coo2 = 0
    sum_all_time_player2_coo1 = 0
    sum_all_time_player2_coo2 = 0
    for i in range(times):
        player1 = CIC.CIC()
        player2 = CIC.CIC()
        sum_player1_channel1_reward = 0
        sum_player1_channel2_reward = 0
        sum_player2_channel1_reward = 0
        sum_player2_channel2_reward = 0
        sum_one_time_player1_coo1 = 0
        sum_one_time_player1_coo2 = 0
        sum_one_time_player2_coo1 = 0
        sum_one_time_player2_coo2 = 0
        decision_player1_next = 0
        decision_player2_next = 0
        for j in range(step):

            decision_player1_current = decision_player1_next
            decision_player2_current = decision_player2_next

            if decision_player1_current == 0 or decision_player1_current == 3:
                random_nbr  = random.random()
                if random_nbr < 2*epsilon*(1-epsilon):
                    decision_player1_current = random.choice([1,2])
                elif 2*epsilon*(1-epsilon) < random_nbr < 2*epsilon*(1-epsilon)+epsilon*epsilon:
                    decision_player1_current = 0 if decision_player1_current == 3 else 3
                else:
                    decision_player1_current = decision_player1_current
            elif decision_player1_current == 1 or decision_player1_current == 2:
                random_nbr  = random.random()
                if random_nbr < 2*epsilon*(1-epsilon):
                    decision_player1_current = random.choice([0,3])
                elif 2*epsilon*(1-epsilon) < random_nbr < 2*epsilon*(1-epsilon)+epsilon*epsilon:
                    decision_player1_current = 1 if decision_player1_current == 2 else 2
                else:
                    decision_player1_current = decision_player1_current

            if decision_player2_current == 0 or decision_player2_current == 3:
                random_nbr  = random.random()
                if random_nbr < 2*epsilon*(1-epsilon):
                    decision_player2_current = random.choice([1,2])
                elif 2*epsilon*(1-epsilon) < random_nbr < 2*epsilon*(1-epsilon)+epsilon*epsilon:
                    decision_player2_current = 0 if decision_player2_current == 3 else 3
                else:
                    decision_player2_current = decision_player2_current
            elif decision_player2_current == 1 or decision_player2_current == 2:
                random_nbr  = random.random()
                if random_nbr < 2*epsilon*(1-epsilon):
                    decision_player2_current = random.choice([0,3])
                elif 2*epsilon*(1-epsilon) < random_nbr < 2*epsilon*(1-epsilon)+epsilon*epsilon:
                    decision_player2_current = 1 if decision_player2_current == 2 else 2
                else:
                    decision_player2_current = decision_player2_current
            if (decision_player1_current,decision_player2_current) not in visit:
                visit[(decision_player1_current,decision_player2_current)] = 1
            else:
                visit[(decision_player1_current, decision_player2_current)] += 1

            sum_one_time_player1_coo1 += coo_rate(decision_player1_current)[0]
            sum_one_time_player1_coo2 += coo_rate(decision_player1_current)[1]
            sum_one_time_player2_coo1 += coo_rate(decision_player2_current)[0]
            sum_one_time_player2_coo2 += coo_rate(decision_player2_current)[1]

            sum_player1_channel1_reward += player1.CIC_reward1(decision_player1_current, decision_player2_current)
            sum_player1_channel2_reward += player1.CIC_reward2(decision_player1_current, decision_player2_current)
            sum_player2_channel1_reward += player2.CIC_reward1(decision_player2_current, decision_player1_current)
            sum_player2_channel2_reward += player2.CIC_reward2(decision_player2_current, decision_player1_current)

            decision_player1_next = player1.CIC_desicion(decision_player1_current,decision_player2_current)
            decision_player2_next = player2.CIC_desicion(decision_player2_current,decision_player1_current)

        avg_each_time_player1_reward1 = sum_player1_channel1_reward / step
        avg_each_time_player1_reward2 = sum_player1_channel2_reward / step
        avg_each_time_player2_reward1 = sum_player2_channel1_reward / step
        avg_each_time_player2_reward2 = sum_player2_channel2_reward / step
        sum_all_time_player1_reward1 += avg_each_time_player1_reward1
        sum_all_time_player1_reward2 += avg_each_time_player1_reward2
        sum_all_time_player2_reward1 += avg_each_time_player2_reward1
        sum_all_time_player2_reward2 += avg_each_time_player2_reward2
        sum_all_time_player1_coo1 += sum_one_time_player1_coo1 / step
        sum_all_time_player1_coo2 += sum_one_time_player1_coo2 / step
        sum_all_time_player2_coo1 += sum_one_time_player2_coo1 / step
        sum_all_time_player2_coo2 += sum_one_time_player2_coo2 / step
    avg_all_time_player1_reward1 = sum_all_time_player1_reward1 / times
    avg_all_time_player1_reward2 = sum_all_time_player1_reward2 / times
    avg_all_time_player2_reward1 = sum_all_time_player2_reward1 / times
    avg_all_time_player2_reward2 = sum_all_time_player2_reward2 / times
    avg_all_time_player1_coo1 = sum_all_time_player1_coo1 / times
    avg_all_time_player1_coo2 = sum_all_time_player1_coo2 / times
    avg_all_time_player2_coo1 = sum_all_time_player2_coo1 / times
    avg_all_time_player2_coo2 = sum_all_time_player2_coo2 / times

    print('avg_all_time_player1_reward1: {0}\navg_all_time_player1_reward2: {1}\navg_all_time_player2_reward1: {2}\navg_all_time_player2_reward2: {3}\n'.format(avg_all_time_player1_reward1,avg_all_time_player1_reward2,avg_all_time_player2_reward1,avg_all_time_player2_reward2))
    print((avg_all_time_player1_reward1+avg_all_time_player1_reward2+avg_all_time_player2_reward1+avg_all_time_player2_reward2)/4)
    print(2*(avg_all_time_player1_reward1 + avg_all_time_player1_reward2 + avg_all_time_player2_reward1 + avg_all_time_player2_reward2) / 4)

    print(
        'avg_all_time_player1_coo1: {0}\navg_all_time_player1_coo2: {1}\navg_all_time_player2_coo1: {2}\navg_all_time_player2_coo2: {3}\n'.format(
            avg_all_time_player1_coo1, avg_all_time_player1_coo2, avg_all_time_player2_coo1,
            avg_all_time_player2_coo2))
    print((avg_all_time_player1_coo1+avg_all_time_player1_coo2+avg_all_time_player2_coo1+avg_all_time_player2_coo2)/4.0)
    print(visit)


if __name__== "__main__" :
    game_CIC_vs_CIC()