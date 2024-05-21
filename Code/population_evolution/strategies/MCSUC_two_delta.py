import random

class MCSUC_two_delta:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.delta1 = 2
        self.delta2 = 4
        self.p = 0.5

    def MCSUC_desicion(self, decision_player1, decision_player2):
        if decision_player1 == 1 or decision_player1 ==2:
            self.j += 1
        elif decision_player1 ==3 :
            self.j += 2
        if decision_player2 == 1 or decision_player2 ==2:
            self.i += 1
        elif decision_player2 ==3 :
            self.i += 2

        if self.delta1 < self.i - self.j <= self.delta2:
            if random.random() < self.p:
                decision = 1
            else:
                decision = 2
        elif self.i - self.j > self.delta2:
            decision = 3
        else:
            decision = 0

        return decision

    def MCSUC_reward1(self, decision_player1, decision_player2):
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

    def MCSUC_reward2(self, decision_player1, decision_player2):
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
