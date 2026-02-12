"""Создайте абстрактный класс PaymentMethod. Объявить абстрактный метод pay(amount). Реализовать минимум 3 класса-наследника с разной логикой оплаты.
 Обеспечить возможность работать с объектами через общий интерфейс.  Проверить полиморфное поведение при вызове pay"""
from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class ByCard(PaymentMethod):
    def pay(self, amount):
        print(f'Оплата картой на сумму {amount}')

class ByCash(PaymentMethod):
    def pay(self, amount):
        print(f'Оплата наличными на сумму {amount}')

class ByOnline(PaymentMethod):
    def pay(self, amount):
        print(f'Оплата онлайн на сумму {amount}')


#amounts = [ByCard(), ByCash(), ByOnline()]
#for amount in amounts:
#    amount.pay(500)

"""Создайте абстрактный класс Notification. Объявите абстрактный метод send(message). Реализуйте минимум 3 класса-наследника,
 каждый из которых отправляет сообщение по-разному."""

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class SendEmail(Notification):
    def send(self, message):
        print(f'send {message} massage by email')

class SendMsg(Notification):
    def send(self, message):
        print(f'send {message} massage by phone')

class SendPost(Notification):
    def send(self, message):
        print(f'send {message} massage by post')

#notifies = [SendEmail(), SendMsg(), SendPost()]
#for notify in notifies:
#    notify.send('hello')



"""Создай класс BankAccount, который имеет закрытый баланс __balance. 
Позволяет пополнять deposit и снимать withdraw деньгию. Не позволяет снимать больше, чем есть на счету. 
Вводит суточный лимит снятия (например, 5000). Сделайте ограничение по транзакциям, не более 3 – х
"""
class BankAccount:
    def __init__(self, balance:float=0):
        self.__balance = balance
        self.daily_limit = 5000
        self.withdrawals_today = 0
        self.max_withdrawals = 3

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError('депозит не может быть равным нулю или отрицательным')
        else:
            self.__balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            raise ValueError('Невозможно снимать больше, чем есть на счету')
        if self.max_withdrawals <=0:
            raise ValueError('Ограничение по транзакциям, не более 3 – х')
        if (self.withdrawals_today + amount) > self.daily_limit:
            raise ValueError('Вы достигли суточного лимит снятия  - 5000')

        self.withdrawals_today +=amount
        self.__balance -= amount
        self.max_withdrawals -= 1

    def get_balance(self):
        return self.__balance

#bank_1 = BankAccount(10000)
#bank_1.deposit(500)
#print(bank_1.get_balance())
#bank_1.withdraw(20000)
#bank_1.withdraw(300)
#bank_1.withdraw(5000)
#bank_1.withdraw(2)



"""Создайте класс User с ролью. Реализуйте policy-класс, определяющий доступ к методам. Создайте декоратор, который проверяет
 право пользователя на выполнение метода. Продемонстрируйте разрешённый и запрещённый доступ без if внутри метода."""
class User:
    def __init__(self, role):
        self.role = role

class Policy:
    @staticmethod
    def admin_only(user):
        return user.role == "admin"

def get_user_role(policy_func):
    def decorator(func):
        def wrapper(user):
            if not policy_func(user):
                return "Запрещен"
            return func(user)
        return wrapper
    return decorator

@get_user_role(Policy.admin_only)
def permis(user):
    return "Доступ разрешен"

admin = User("admin")
regular_user = User("user")
print(f"Admin: {permis(admin)}")
print(f"User:  {permis(regular_user)}")









