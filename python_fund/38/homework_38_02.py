""" 02 История операций

Доработайте класс BankAccount:
- каждая операция пополнения и снятия должна сохраняться в историю history
- история операций должна
    - вызываться через атрибут history (только для чтения!)
    - и возвращать список

Operation history:
    Deposit: 150
    Withdraw: 100
"""

class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

    @property
    def history(self):
        return self.__history.copy()  # return list(self.__history)





if __name__ == "__main__":
    account = BankAccount("Alice", 50)

    account.deposit(150)
    account.withdraw(100)
    account.show_balance()

    print("Operation history:")
    for operation in account.history:
        print("\t", operation)

    account.history.append('injection')
    if account.history != ["Deposit: 150", "Withdraw: 100"]:
        print("ВНИМАНИЕ! \nАККАУНТ ВЗЛОМАН! \nИстория операций изменена хакерами!!!")


# Current balance: 100
# Operation history:
# 	 Deposit: 150
# 	 Withdraw: 100


"""
Если задаче решена верно, то этого сообщения вы не увидите:

ВНИМАНИЕ! 
АККАУНТ ВЗЛОМАН! 
История операций изменена хакерами!!!
"""


############ 2

# class BankAccount:
#     def __init__(self, name, balance):
#         self.__name = name
#         self.__balance = balance
#         self.__history = []
#
#     def _record_operation(self, operation_type, amount):
#         """Приватный метод для записи операции в историю."""
#         self.__history.append(f"{operation_type}: {amount}")
#
#     def _validate_amount(self, amount):
#         """Приватный метод для проверки суммы."""
#         if amount <= 0:
#             print("Error: Amount must be positive.")
#             return False
#         return True
#
#     def deposit(self, amount):
#         if self._validate_amount(amount):
#             self.__balance += amount
#             self._record_operation("Deposit", amount)
#
#     def withdraw(self, amount):
#         if not self._validate_amount(amount):
#             return
#         if amount > self.__balance:
#             print("Error: Not enough funds.")
#             return
#         self.__balance -= amount
#         self._record_operation("Withdraw", amount)
#
#     def show_balance(self):
#         print(f"Current balance: {self.__balance}")
#
#     @property
#     def history(self):
#         return self.__history.copy()
