class Car:
    def __init__(self, n_o_p, v_c, a_of_g):
        self.V_cistern = v_c
        self.amount_of_gasoline = a_of_g
        self.number_of_pistons = n_o_p

    def __start_engin(self):
        if self.amount_of_gasoline > 3:
            print("Engin sound")
            self.__gasoline_supply()
        else:
            print("NO gasoline")

    def __gasoline_supply(self):
        self.amount_of_gasoline -= 1

    def start_the_car(self):
        self.__start_engin()
