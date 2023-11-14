from random import randint as boss_feeling
from random import uniform as opinion


class OBC:
    def __init__(self, money_per_perf: int, num_of_soloists: int, num_of_musicians: int):
        self._money_per_perf = money_per_perf
        self.__num_of_soloists = num_of_soloists
        self.__num_of_musicians = num_of_musicians

    def kick_mate(self):
        if round(opinion(0, 1)) + round(opinion(0, 1)) + round(opinion(0, 1)) + round(opinion(0, 1)) + round(opinion(0, 1)) + round(opinion(0, 1)) > 4:
            if round(opinion(0, 1)) == 1:
                self.__num_of_musicians -= 1
            else:
                self.__num_of_soloists -= 1

    def do_something(self):
        if boss_feeling(0, 1) == 0:
            self._money_per_perf *= 0.9
