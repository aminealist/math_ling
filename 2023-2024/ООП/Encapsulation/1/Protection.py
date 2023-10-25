from random import randint as boss_feeling
from random import uniform as opinion


class OBC:
    def __init__(self, m_f_o_c, n_o_s, n_o_m):
        self._money_per_perf = m_f_o_c
        self.__num_of_soloists = n_o_s
        self.__num_of_musicians = n_o_m

    def kick_mate(self):
        if round(opinion(0, 1)) + round(opinion(0, 1)) + round(opinion(0, 1)) + round(opinion(0, 1)) + round(
                opinion(0, 1)) + round(opinion(0, 1)) > 4:
            if round(opinion(0, 1)) == 1:
                self.__num_of_musicians -= 1
            else:
                self.__num_of_soloists -= 1

    def do_something(self):
        if boss_feeling(0, 1) == 0:
            self._money_per_perf *= 0.9
