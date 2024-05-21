import random

class CURE:
    def __init__(self):
        self.i_channel1 = 0
        self.i_channel2 = 0
        self.j_channel1 = 0
        self.j_channel2 = 0
        self.delta1 = 2
        self.delta2 = 2


    def CURE_desicion(self, decision_player1, decision_player2):
        if decision_player1 == 0:
            pass
        elif decision_player1 == 1:
            self.j_channel2 += 1
        elif decision_player1 == 2:
            self.j_channel1 += 1
        elif decision_player1 == 3:
            self.j_channel1+=1
            self.j_channel2+=1
        if decision_player2 == 0:
            pass
        elif decision_player2 == 1:
            self.i_channel2 += 1
        elif decision_player2 == 2:
            self.i_channel1 += 1
        elif decision_player2 == 3:
            self.i_channel1 += 1
            self.i_channel2 += 1

        if self.i_channel1 - self.j_channel1 <= self.delta1:
            if self.i_channel2 -self.j_channel2 <= self.delta2:
                decision = 0
            else:
                decision = 1
        else:
            if self.i_channel2 -self.j_channel2 <= self.delta2:
                decision = 2
            else:
                decision = 3

        return decision

    def CURE_reward1(self, decision_player1, decision_player2):
        R1, S1, T1, P1 = 3, 0, 5, 1
        if decision_player1 <= 1:
            if decision_player2 <= 1:
                reward1 = R1
            else:
                reward1 = S1
        else:
            if decision_player2 <= 1:
                reward1 = T1
            else:
                reward1 = P1

        return reward1

    def CURE_reward2(self, decision_player1, decision_player2):
        R2, S2, T2, P2 = 3, 0, 5, 1
        if decision_player1 == 0 or decision_player1 == 2:
            if decision_player2 == 0 or decision_player2 == 2:
                reward2 = R2
            else:
                reward2 = S2
        else:
            if decision_player2 == 0 or decision_player2 == 2:
                reward2 = T2
            else:
                reward2 = P2

        return reward2
