class BankAccount:
    def __init__(self, n, n_s, b, p):
        self.name = n
        self.account_numb = n_s
        self.__balance = b
        self.__password = p

    def show_me_balance(self):
        p = 3
        while p != 0:
            if input("Введите пароль: ") == str(self.__password):
                print(self.__balance)
            else:
                p -= 1
        if p == 0:
            print("Вас забанили, подождите минуточку")

    def i_need_money(self):
        p = 3
        while p != 0:

            if input("Введите пароль: ") == str(self.__password):
                k = 0
                while k != 3:
                    k += 1
                    x = input("Сколько вы хотите снять? ")
                    if self.__balance - int(x) >= 0:
                        print(f"{self.__balance} - {int(x)} = {self.__balance - int(x)}")
                        self.__balance -= int(x)
                        p = 0
                        break
                    else:
                        print("Недостаточно средств")
                        p = 0
                        break
            else:
                p -= 1
                print(f"У вас осталось {p} попыток")
