class HardMajority:
    def __init__(self):
        self.opp_cooperate_times_channel1 = 0
        self.opp_defect_times_channel1 = 0
        self.opp_cooperate_times_channel2 = 0
        self.opp_defect_times_channel2 = 0

    def HardMajority_desicion(self):
        weigh = 0
        if self.opp_cooperate_times_channel1 > self.opp_defect_times_channel1+weigh:
            if self.opp_cooperate_times_channel2 > self.opp_defect_times_channel2+weigh:
                decision = 0
            else:
                decision = 1
        else:
            if self.opp_cooperate_times_channel2 > self.opp_defect_times_channel2+weigh:
                decision = 2
            else:
                decision = 3

        return decision

    def HardMajority_opp_decision_store(self, decision_player2):
        if decision_player2 == 0:
            self.opp_cooperate_times_channel1 += 1
            self.opp_cooperate_times_channel2 += 1
        elif decision_player2 == 1:
            self.opp_cooperate_times_channel1 += 1
            self.opp_defect_times_channel2 += 1
        elif decision_player2 == 2:
            self.opp_defect_times_channel1 += 1
            self.opp_cooperate_times_channel2 += 1
        elif decision_player2 == 3:
            self.opp_defect_times_channel1 += 1
            self.opp_defect_times_channel2 += 1


    def HardMajority_reward1(self, decision_player1, decision_player2):
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

    def HardMajority_reward2(self, decision_player1, decision_player2):
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
