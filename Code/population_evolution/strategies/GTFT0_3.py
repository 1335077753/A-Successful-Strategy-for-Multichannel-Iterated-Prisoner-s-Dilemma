import random
class GTFT:

    def __init__(self):
        self.generosity = 0.3

    def GTFT_desicion(self, decision_player1, decision_player2):
        if decision_player2 == 0:
            decision = 0
        elif decision_player2 == 1:
            if random.random() < self.generosity:
                decision = 0
            else:
                decision = 1
        elif decision_player2 == 2:
            if random.random() < self.generosity:
                decision = 0
            else:
                decision = 2
        elif decision_player2 == 3:
            ran_num = random.random()
            if ran_num < self.generosity * self.generosity:
                decision = 0
            elif self.generosity * self.generosity < ran_num < self.generosity * self.generosity + self.generosity:
                decision = 1
            elif self.generosity * self.generosity + self.generosity < ran_num < self.generosity * self.generosity + 2 * self.generosity:
                decision = 2
            else:
                decision = 3

        return decision

    def GTFT_reward1(self, decision_player1, decision_player2):
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

    def GTFT_reward2(self, decision_player1, decision_player2):
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
