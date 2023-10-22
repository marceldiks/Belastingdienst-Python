class BankAccount:

    def __init__(self, number, holder, balance = 0):
        self._holder = holder
        self._number = number
        self._balance = balance

    def __str__(self):
        return f'Bankaccount: {self._number} - {self._holder}, balance €{self._balance}.'

    def __repr__(self):
        return f'Bankaccount("{self._number}", "{self._holder}", {self._balance})'

    def withdraw(self, amount):
        self._balance -= amount
        print(f'Withdraw of €{amount}')

    def deposit(self, amount):
        self._balance += amount
        print(f'Deposit of €{amount}')

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a balance of €{self._balance}.'


# ---------------------------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount('NL01ABCD0234567890', 'Peter')
    acc2 = BankAccount('NL01ABCD0234567777', 'Guido', balance = 1000)

    print(acc1.get_info())
    print(acc2.get_info())

    print(repr(acc1))
    print(str(acc1))
    print(repr(acc2))
    print(str(acc2))

    acc1.deposit(1000)
    acc1.withdraw(100)
    acc1.withdraw(22)

    acc2.deposit(10000)
    acc2.withdraw(1090)
    acc2.withdraw(220)

    print(acc1.get_info())
    print(acc2.get_info())
