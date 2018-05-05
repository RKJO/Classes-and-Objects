class BankAccount:
    __next_acc_number = 1

    def __init__(self):
        self.__number = BankAccount.__next_acc_number
        BankAccount.__next_acc_number += 1
        self.__cash = 0.0

        # if isinstance(number, int):
        #     self.__number = number
        # else:
        #     self.__number = -1

    def get_number(self):
        return self.__number

    def get_cash(self):
        return '{} PLN'.format(self.__cash)

    def deposit_cash(self, amount):
        if isinstance(amount, int) and amount > 0.0:
            self.__cash += amount
        else:
            print("Amount is invalid. It isn't number or it's not positive")

    def withdraw_cash(self, amount):
        if isinstance(amount, int) and amount > 0.0:
            if self.__cash >= amount:
                self.__cash -= amount
                return amount
            else:
                withdraw = self.__cash
                self.__cash = 0.0
                return withdraw
        else:
            print("Amount is invalid. It isn't number or it's not positive")

    def print_info(self):
        print('Bank number account {}, cash: {}'.format(self.__number, self.__cash))


b = BankAccount()
b.print_info()
b.deposit_cash(100)
b.print_info()
print(b.withdraw_cash(50))
b.print_info()
print(b.withdraw_cash(100))
b1 = BankAccount()
c1 = BankAccount()
d1 = BankAccount()

b1.print_info()
c1.print_info()
d1.print_info()