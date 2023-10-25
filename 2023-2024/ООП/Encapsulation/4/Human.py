from math import inf as infinite


class Human:
    def __init__(self, name, social_rating, gender, height, weight, waist, hair_length, beauty, iq, race, pets,
                 friends, profession):
        self.human_name = name
        self.social_rating = social_rating
        self.gender = gender
        self.height = height
        self.__weight = weight
        self.__waist_length = waist
        self.hair_length = hair_length
        self.beauty = beauty
        self.iq = iq
        self.human_race = race
        self.human_pets = pets
        self.friends = friends
        self.profession = profession

        self.Normal_parameters = {"height": [20, 240], "weight": [2, 140],
                                  "waist": [40, 150], "heir_length": [0, infinite], "beauty": [0, 10]}
        self.Professions_which_can_do_more = ["doctor"]

    def __say_weight(self):
        print(self.__weight)

    def __say_waist_length(self):
        print(self.__waist_length)

    def is_friend(self, consideration_object):
        if isinstance(consideration_object, Human):
            if consideration_object.human_name in self.friends or self.human_name == consideration_object.human_name:
                return True
        elif isinstance(consideration_object, str):
            if consideration_object in self.friends:
                return True
        else:
            return False

    def is_professions_which_can_do_more(self, consideration_object):
        if isinstance(consideration_object, Human):
            if consideration_object.profession in self.Professions_which_can_do_more:
                return True
        elif isinstance(consideration_object, str):
            if consideration_object in self.Professions_which_can_do_more:
                return True
        else:
            return False

    def cut_heir(self, stress_resistance_of_hairdresser=5):

        for i in range(stress_resistance_of_hairdresser):
            cm = int(input("На сколько вы хотите подстричь волосы?  "))
            if self.Normal_parameters["heir_length"][0] <= self.hair_length - cm <= \
                    self.Normal_parameters["heir_length"][
                        1]:
                self.hair_length -= cm
                print("\nВсё сделано\n")
                break
            else:
                print("Волосы слишком короткие")
        else:
            if self.social_rating > 10:
                self.social_rating -= 7
            print("\nНе приходите сюда больше🤨 \n")

    def do_sport(self, hours):
        if self.Normal_parameters["weight"][0] <= self.hair_length - hours * 0.07 <= \
                self.Normal_parameters["weight"][1]:
            self.hair_length -= hours * 0.07
        else:
            print("You cant")

    def ask_weight(self, questioner):
        if self.is_friend(questioner) or self.is_professions_which_can_do_more(questioner):
            self.__say_weight()
        else:
            print("\nНевежливо такое спрашивать\n")

    def ask_height(self, questioner):
        if self.is_friend(questioner) or self.is_professions_which_can_do_more(questioner):
            self.__say_weight()
        else:
            print("\nВам незачем это знать \n")
