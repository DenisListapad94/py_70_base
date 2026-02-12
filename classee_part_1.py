'''
Создать класс с двумя переменными.
Добавить функцию вывода на экран и функцию изменения этих переменных.
Добавить функцию,которая находит сумму значений этих переменных,
и функцию которая находит наибольшее значение из этих двух переменных.
'''
class Params():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_params(self):
        print(f'fist param is {self.a} , second params is {self.b}')
    def change_params(self):
        self.a += 1
        self.b += 1
    def sum_of_params(self):
        return print(self.a + self.b)
    def biggest_of_params(self):
        if self.a != self.b:
            return print(self.a if self.a > self.b else self.b)
        else:
            return print('числа одинаковык')

case_params_1 = Params(2,2)
case_params_1.change_params()
case_params_1.biggest_of_params()
case_params_1.sum_of_params()
case_params_1.print_params()




'''Описать класс, реализующий десятичный счетчик'''
class Count():
    def __init__(self, num = 1, start = 0, stop = 99):
        self.num = num
        self.start = start
        self.stop = stop

    def print_count(self):
        if (self.num > self.stop or self.num < self.start):
            print(f'Счетчик {self.num}  находится вне диапазона от {self.start} до {self.stop} ')
        else:
            print(f'Счетчик {self.num} находится в диапазоне от {self.start} до {self.stop} ')

    def increase_count(self):
        if self.num > self.stop or self.num < self.start:
            print(f'Счетчик должен находится в  диапазоне от {self.start} до {self.stop} ')
            return self.num
        else:
            self.num += 1

    def decrease_count(self):
        if self.num > self.stop or self.num < self.start:
            print(f' Счетчик должен находится в  диапазоне от {self.start} до {self.stop} ')
            return self.num
        else:
            self.num -= 1


num_for_count = Count(1, 7, 85)
num_for_count.print_count()
num_for_count.decrease_count()
num_for_count.print_count()
num_for_count.increase_count()
num_for_count.print_count()




'''
Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов,
поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.'''
class Shop():

    def __init__(self, product, count):
        self.product = product
        self.count = count
        self.storage = {}
        self.storage[self.product] = self.count

    def print_state(self):
        print(f'В магазине следующие товары {self.storage}')

    def search(self, product):
        print(f'{product} есть в наличии ' if product in self.storage else f'{product} нет в наличии')

    def add_product(self, product, count):
       if product in self.storage:
           self.storage[product] += count
       else:
           self.storage[product] = count

    def del_product(self, product):
        try:
            del self.storage[product]
            print(f'Продукт {product} удален')
        except KeyError:
            print('Введено некорректное название для удаления')

evroopt = Shop('apple', 100)
evroopt.print_state()
evroopt.add_product('potato', 350)
evroopt.add_product('eggs', 50)
evroopt.print_state()
evroopt.del_product('potato')
evroopt.del_product('egs')
evroopt.print_state()
evroopt.search('eggs')




'''Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную вместимость,
которая выражается целым числом – количеством монет(capacity -вместимость), которые можно положить в копилку.
Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать,
можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

При создании копилки, число монет в ней равно 0.
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
'''
class MoneyBox:
    def __init__(self, capacity):
        #конструктор с аргументом- вместимость копилки\
        self.capacity = capacity
        self.current_amount = 0
    def print_current_amount(self):
        print(f'количество монет в копилке - {self.current_amount}')
    def can_add(self,v):
    #True, если можно добавить v монет, False иначе
        if self.current_amount + v <= self.capacity:
            return True
        else:
            return False
    def add(self,v):
        #положить v монет в копилку
        if self.can_add(v):
            self.current_amount += v
        else:
            print(f'нельзя полложить в копилку {v} монет. Сейчас в копилке {self.current_amount}. Максимальная вместимость копилки- {self.capacity }')

money_box_1 = MoneyBox(5)
money_box_1.print_current_amount()
money_box_1.add(2)
money_box_1.add(5)



'''1.	Задача на взаимодействие между классами. Разработать систему «Интернет-магазин».
Товаровед добавляет информацию о Товаре. Клиент делает заявку на товар,
если товар есть в наличие в магазине то покупатель оплачивает товар иначе
товаровед делает запрос на склад о наличии товара.'''


class Shop():
    arr = []

    def __init__(self, name_product, sklad):
        self.name_product = name_product
        self.arr.append(name_product)
        self.sklad = sklad

    def has_product(self, name_product):
        return name_product in self.arr

    def has_product_sklad(self, name_product):
        if self.sklad.has_product(name_product):
            print(f'Товара под названием {name_product} есть на складе')
        else:
            print(f'Товара под названием {name_product} нет на складе')


class Customer():
    def __init__(self, name, product_want, product_shop):
        self.name = name
        self.product_want = product_want
        self.product_shop = product_shop

    def do_zayavka(self):
        if self.product_shop.has_product(self.product_want):
            print(f'{self.name} хочет купить {self.product_want}')
        else:
            self.product_shop.has_product_sklad(self.product_want)


class Sklad:
    arr = []

    def __init__(self, *args):
        self.items = args
        self.arr.extend(self.items)

    def has_product(self, name_product):
        return name_product in self.arr


sklad = Sklad('сковорода', 'тарелка', 'ложка', 'лыжи')
shop = Shop('плита', sklad)
shop = Shop('утюг', sklad)
customer = Customer('Василий', 'лыжи', shop)
customer_1 = Customer('Петя', 'ноутбук', shop)
customer_3 = Customer('Иван', 'плита', shop)
customer.do_zayavka()
customer_1.do_zayavka()
customer_3.do_zayavka()
