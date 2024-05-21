import random
class TFT:

    def __init__(self):
        self.p = [[1,1],[1,0],[0,1],[0,0],
                  [1,1],[1,0],[0,1],[0,0],
                  [1,1],[1,0],[0,1],[0,0],
                  [1,1],[1,0],[0,1],[0,0]]
        self.reward1 = 0
        self.reward2 = 0

    def TFT_desicion(self, decision_player1, decision_player2):
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

    def TFT_reward1(self, decision_player1, decision_player2):
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

    def TFT_reward2(self, decision_player1, decision_player2):
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
