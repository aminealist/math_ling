class Car:
    def __init__(self, number_of_pistons, volume_cistern, amount_of_gasoline):
        self.V_cistern = volume_cistern
        self.amount_of_gasoline = amount_of_gasoline
        self.number_of_pistons = number_of_pistons

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
