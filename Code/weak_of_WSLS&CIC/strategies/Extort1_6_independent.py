import random

class Extort1_6_independent:
    def __init__(self):
        self.p = [[0.892, 0.892],
 [0.892, 0.33399999999999996],
 [0.33399999999999996, 0.892],
 [0.33399999999999996, 0.33399999999999996],
 [0.892, 0.504],
 [0.892, 0.0],
 [0.33399999999999996, 0.504],
 [0.33399999999999996, 0.0],
 [0.504, 0.892],
 [0.504, 0.33399999999999996],
 [0.0, 0.892],
 [0.0, 0.33399999999999996],
 [0.504, 0.504],
 [0.504, 0.0],
 [0.0, 0.504],
 [0.0, 0.0]]
        self.reward1 = 0
        self.reward2 = 0

    def Extort1_6_independent_desicion(self, decision_player1, decision_player2):
        i = decision_player1
        j = decision_player2
        if random.random() < self.p[i*4+j][0]:
            if random.random() < self.p[i*4+j][1]:
                decision = 0
            else:
                decision = 1
        else:
            if random.random() < self.p[i*4+j][1]:
                decision = 2
            else:
                decision = 3

        return decision

    def Extort1_6_independent_reward1(self, decision_player1, decision_player2):
        R1, S1, T1, P1 = 3, 0, 5, 1
        if decision_player1 <= 1:
            if decision_player2 <= 1:
                self.reward1 = R1
            else:
                self.reward1 = S1
        else:
            if decision_player2 <= 1:
                self.reward1 = T1
            else:
                self.reward1 = P1

        return self.reward1

    def Extort1_6_independent_reward2(self, decision_player1, decision_player2):
        R2, S2, T2, P2 = 3, 0, 5, 1
        if decision_player1 == 0 or decision_player1 == 2:
            if decision_player2 == 0 or decision_player2 == 2:
                self.reward2 = R2
            else:
                self.reward2 = S2
        else:
            if decision_player2 == 0 or decision_player2 == 2:
                self.reward2 = T2
            else:
                self.reward2 = P2

        return self.reward2
