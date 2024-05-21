class ALLC:

    def __init__(self):
        self.p = []


    def ALLC_desicion(self, decision_player1, decision_player2):
        decision = 0

        return decision

    def ALLC_reward1(self, decision_player1, decision_player2):
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

    def ALLC_reward2(self, decision_player1, decision_player2):
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
