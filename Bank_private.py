class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # приватная переменная
    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount # Функция вноса денег на счёт, если баланс положительный
    def withdraw(self, amount):
        if 0<amount<=self.__balance:
            self.__balance -= amount # Функция снятия денег, если баланс не отрицательный
        else:
            print('Недостаточно средств')
    def get_balance(self):
        return self.__balance   # Возвращает переменную  __balance
account = BankAccount(1000) # Создаёт объект account с балансом 1000
account.deposit(500) # Вызывает метод вноса денег на счёт
account.withdraw(170) # Вызывает метод снятия денег с счёта
print(account.get_balance()) #1500
# account.__balance # Будет ошибка, т.к. __balance приватна
# Приватная переменная защищает код от (не)преднамеренного изменения пользователем