class BankAccount:
    def __init__(self, n, n_s, b, p):
        self.name = n
        self.bank_account_number = n_s
        self.__balance = b
        self.__password = p

    def show_balance(self, number_of_attempts=3):

        for i in range(number_of_attempts):
            if self.is_password_right(input("Введите пароль: ")):
                print(self.__balance)
                break
            else:
                print("Неверный пароль")
            print(f"Количество оставшихся попыток {number_of_attempts - i - 1}")
        else:
            print("Вас забанили, подождите минуточку")

    def is_password_right(self, password):
        if str(self.__password) == str(password):
            return True
        else:
            return False

    def withdraw_money(self, number_of_attempts=3):
        right_password = self.is_password_right(input("Введите пароль: "))
        for i in range(number_of_attempts):
            if right_password:
                amount_of_money = float(input("Сколько вы хотите снять? "))
                if len(str(amount_of_money % 1)) > 2:
                    print("Минимальный выдаваемый номинал 1 копейка")
                else:
                    if self.__balance - amount_of_money >= 0:
                        print(f"{self.__balance} - {amount_of_money}: {self.__balance - amount_of_money}")
                        self.__balance -= amount_of_money
                        break
                    else:
                        print("Недостаточно средств")
            else:
                print("Неверный пароль")
                right_password = self.is_password_right(input("Введите пароль: "))
            print(f"Количество оставшихся попыток {number_of_attempts - i - 1}")
        else:
            print("Превышен лимит попыток. Попробуйте позже")
