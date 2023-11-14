from Human import Human


Human1 = Human("Alexander", 1488, "male", 180, 70, 100, 30,
               10, 128, "caucasoid", ["cat"], ["Danil"], "genius")


Human1.ask_weight("Danil")
Human1.cut_heir()
print(Human1.is_friend(Human1))
