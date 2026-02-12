# height = 10
# up = 6
# down = 2
#
# print((height - up - 1)//(up-down)  + 1 + 1 )
# print(0**0**((height - up) % (up-down)))
# boolean
# var_1 = ["Hello"]
# var_2 = ["Hello"]
# print(ord("H"))
# print(ord("h"))
# print(var_1 == var_2) # False
# print(var_1 != var_2) # True
# print(var_1 >= var_2) # False
# print(var_1 <= var_2) # True
# print(var_1 > var_2) # False
# print(var_1 < var_2) # True
# print(var_1 is var_2) # False
import random
import time
from functools import reduce


# else if  elif
# and и or или not  не
# var_1 =  13
# if var_1 > 0: # boolean True False
#     print("positive")
#     if var_1 >= 10 and var_1 <= 99:
#         print("2 sign number")
#
# elif var_1 == 0:
#     print("zero")
# else:
#     print("negative")
# var = None
# if type(var) is NoneType: # boolean
#     print(var)

# bool_a = True
# bool_b = True
# bool_c = False
# if not bool_c and not(bool_c or bool_c):
#     print(bool_a)
# var_1 = 6
# var_2 = 0
# var_3 = var_1 and var_2
# print(var_3)

# String - не изменяема

# 012345
# str_1 = "0123456789" # ascii кодом
# length = len(str_1)
# print(length)
# print(str_1[10::-1]) # concat
# slice start end step
# print(id(str_1[0]))
# print(id(str_1[1]))
# print(id(str_1[2]))
# print(id(str_1[3]))
# print(str_1[-4])
# print(str_1[-5])
# print(str_1[-6])
# s = "hello"
# print(s)

# s_1, s_2, s_3 = map(int,input("Введите 3 значния:").split())
# s = "hello"
# lst = list(s)
# print(lst)
# s = "hello"
# print(id(s))
# s = "2" + s[1:]
# print(id(s))
# num_1 = 2
# num_2 = 3
# print((num_1  + num_2) % 2  == 0)
# num = 3313
# print(num % 1111 == 0)

# 9.	Дана строка. Если в этой строке буква f встречается только один раз,
# выведите её индекс.  Если она встречается два и более раз, выведите индекс её
# второго появления и количество букв f.
# some_str = "dhdfsadfdasddasffadasdf"
# if some_str.count("f") > 1:
#     first_f_index = some_str.find("f")
#     second_f_index = some_str.find("f",first_f_index + 1)
#     print(first_f_index)
#     print(second_f_index)

# x1, y1 = map(int, input().split("enter slon koord"))
# x2, y2 = map(int, input().split("enter kon koord"))
# if x1 == x2 and y1 == y2:
#     print("фигуры не могут стоять на одной клетке")
# elif x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2 or y1 - x1 == y2 - x2:
#     print("cлон бъёт коня")
# elif abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
#     print("конь бъёт слона")
# else:
#     print("all good")


#  list 50 45 dict
# tuple 4 1 set
# frozenset frozendict 0.001 = 0

# tuple =>кортеж неизменяемая коллекция структурированных данных
#      0    1     2   3    4     5  6
# tup = (4, "dasd", 42.2, None, (None,2, 1,6), 2312, 4)
# for index in range(len(tup)):
#     print(tup[index])

# print(tup)

# set => множество - исзменяемая коллекция уникальных неизменяемых данных)
# хэш-таблица
# set_1 = {2, 6, "sdsad",None, 2, False, 0, (4,2,1),()}
#
# set_2 = set()


# lst => измиеняемая коллекция структурированных данных
# tuple => неизмиеняемая коллекция структурированных данных
#      0   1     2
# lst = [5,1,5,2,6,1,2,6]
# lst[0] += 12
# lst.append([5,1,1])
# lst.extend([5,1,2])
# print(lst.insert(0,77))
# lst.sort(key=lambda elem: not elem%2 )
# print(lst)

# dict => коллекция уникальных пар ключ значение (хэш-таблица)
# users = {
#     "users": {
#         "user_1": {
#             "name": "Vasya",
#             "last_name": "pupkin",
#             "age": 23,
#             "bank_account": [
#                 {
#                     "belarusbank": [
#                         {
#                             "usdt_acc":{},
#                             "eur_acc":{},
#                         }
#
#
#                     ]
#                 },
#                 {
#                     "alpha": [
#                         {
#                             "usdt_acc": {},
#                             "eur_acc": {},
#                         }
#
#                     ]
#                 }
#
#             ]
#         },
#         "user_2":{
#             "name": "VlaD",
#             "last_name": "Voroshil"
#         },
#     }
# }
# dct["heds"] = "hello"
# dct[23] = 555
# print(dct["key_3"])

# for value in dct.values():
#     print(value)
# print(users["users"]["user_1"]["bank_account"][1]["alpha"])
# JSON
# 6. Дано число n. Вывести на экран числа 1, 4, 9, 16, 25, ...
# которые меньше n.
# Sample Input :
# 15
# Sample Output :
# 1 4 9
# number = 90
# for i in range(1, int((number ** 0.5)  + 1)):
#     if i ** 2 < number:
#         print(i**2, end =" ")
#
# i = 1
# print()
# number = 90
# while i ** 2 < number:
#     print( i**2, end=" ")
#     i+=1

# s = "aaaabbcaacccuureeer"
# s += " "
# new_decoded_s = ""
# counter = 1
# for ind in range(len(s) - 1):
#     if s[ind] == s[ind+1]:
#         counter += 1
#     else:
#         new_decoded_s += s[ind] + str(counter)
#         counter = 1
# print(new_decoded_s)
# class CustomExceptions(Exception):
#     pass

# def some_fun():
#     try:
#         numb_1 = 5
#         numb_2 = {}
#         print(numb_1 + numb_2)
#     except Exception:
#         print("Error")
#         raise
#         # raise ArithmeticError("XAXAXA")
#
#
# try:
#     some_fun()
#
# except ArithmeticError as exc:
#     print("cod failed: ArithmeticError",exc.args)
# except IndexError:
#     print("cod failed: IndexError")
# except TypeError:
#     print("cod failed: TypeError")
# except Exception as exc:
#     print(type(exc),exc.args)
# # else:
# #     print("all good")
# finally:
#     print("always")

# DRY
# KISS keep it simple stupid
# YAGNI
# sum = 0
# for i in range(10):
#     print(i)
#     sum += i
# чистая функция
# def print_stars(count):
#     if count >= 50:
#         return
#     for i in range(count):
#         print("*",end="")
#     return "\nfunction complete"
# print_stars(10)
#
# print()
# print("hello world")
#
# print(print_stars("30"))

# def some_example_args_function(attr_int1, attr_str2, *args,**kwargs):
#     print(attr_int1 + 3)
#     print(attr_str2  + " !")
#     print(args)
#     print(kwargs)
#
#
# lst = [4,5,1,6,2]
# some_str = "sdasda"
# some_dict = {"a": 22, "b": 5}
# some_example_args_function(30,"10",1,5,2,6,2,6,2,5,2,*lst,*some_str,54,val_1=2,val_2=4,**some_dict)
# GLEB
# GLOBAL область видимости модуля
# LOCAL область видимости
# ENCLOSING замыкающая область функцбюбии
# # BUILDINS scope область встроенных функций
# var_a = 12
# var_b = "hello"
#
# def some_new_fun(counter: int, some_str: str) -> None:
#     """
#     :param counter: count of value
#     :param some_str: some random string
#     :return: some data
#     show detail info about args
#     """
#     def inner_fun():
#         nonlocal counter
#         counter = 55
#         var_inner = 22
#         print(locals())
#
#     inner_fun()
#     print(locals())
#     # return counter, some_str
#
# #
# result = some_new_fun(counter=10,some_str="hello")
# # print(some_new_fun)
#
# print(var_a)
# print(globals())

# lambda args1,args2: ()f
# def some_sum_fun(x1,x2):
#     return x1 + x2
# fun = lambda x_1, x_2: x_1 + x_2
# fun2 = some_sum_fun
# print(fun2(x1=4,x2=5))
# print(fun(x_1=4,x_2=5))
# lst = [50,2,52,60,2,50,21,2,120]
# lst.sort(key = lambda x: x % 10 == 0)
# print(lst)

# lst = [5,2,1,8,5,7,2,4]
# some_str = "dadqwd"
# ЧТО МЫ ХОТИМ ПОМЕСТИТЬ FOR из ЧЕГО БЕРЁМ in Итерабельный объект
# new_list = [el * 3 for el in lst]
# ЧТО МЫ ХОТИМ ПОМЕСТИТЬ FOR из ЧЕГО БЕРЁМ in Итерабельный объект if условие верно
# new_list = [el * 3 for el in lst if not el % 2 ]
# ЧТО МЫ  ПОМЕСТИМ если условие верно иначе что поместим FOR из ЧЕГО БЕРЁМ in Итерабельный объект

# def some_fun_1(el):
#     return el * 3
#
# def some_fun_2(el):
#     return el - 3
#
# new_list = {some_fun_1(el) if not el % 2  else some_fun_2(el) for el in lst}
# print(new_list)
# lst = [5,2,5,1,23,5,1]
# new_dict = { lst[index]: lst[index]**2 if lst[index] not in lst[:index] for index in range(len(lst))}
# print(new_dict)
# size = 10
#
# matrix = [[random.randint(0,1) for _ in range(size)]  for _ in range(size)]
# for row in matrix:
#     print(row)
#
#
# obj = tuple(int(elem) for elem in input().split() if elem.isdigit())

# print(obj)

# map filter reduce
# obj = ["1","5","2","5","1",]
# new_obj = list(map(lambda item: int(item) ** 2,obj))
# print(new_obj)
#
# str_obj = ["fsaad dssss dsa dasd da","da das das www","gjfdgreg","","dadagaggaaaa ww wda",]
# new_str_obj = list(map(lambda item: " ".join([elem for elem in item.split() if "a" not in elem]),str_obj))
# print(new_str_obj)

# filter
# lst = [5,222,16,0,45,0,21]
# new_obj = list(map(lambda item: item //3 ,(filter(lambda item: not (item % 3) and  item != 0,lst))))
# print(new_obj)
# lst_summa = []
# def some_check(value):
#     if value > 50:
#         lst_summa.append(value)
#         value = 0
#     return value
#
# value =  reduce(lambda x, y: some_check(x) + y, [11, 25, 36, 4, 5,2,12,4,22,19,26,33,5])
# print(lst_summa)

# GLEB

# def wrapper(x: int):
#     def inner(y: int):
#         nonlocal x
#         x += 1
#         return x+y
#     return inner
#
#
# closure = wrapper(1)
# for i in range(10):
#     print(closure(2))


#
# def decorator(fun: callable):
#     def inner(*args,**kwargs):
#         for i in range(100):
#             print("*",end="")
#         print()
#         count = fun(*args,**kwargs)
#         #
#         # if count > 5:
#         #     raise TypeError
#         print(count)
#         return count
#
#     return inner
#
# @decorator
# def some_fun(*args,**kwargs):
#     print("some fun")
#     print(kwargs)
#     return 1 + sum(args) + sum(kwargs.values())
#
# # some_fun = decorator(some_fun)
# counter = some_fun(1)
# counter = some_fun(counter,**{"key":2})
# counter = some_fun(counter)
# counter = some_fun(counter,**{"key":2,"key2":3})
# counter = some_fun(counter)
#
# from typing import Any
#
#
# lst = []
# def decorator(fun):
#     def inner(arg: Any):
#         try:
#             item = fun(arg)
#             lst.append(item)
#             return item
#         except TypeError as e:
#             print("TypeError args is ",*e.args)
#
#
#     return inner
#
# def decorator_2(fun):
#     def inner(arg: Any):
#         item = fun(arg)
#         print(item)
#     return inner
#
#
# @decorator_2
# @decorator
# def some_fun(arg: Any):
#     if type(arg) == list:
#         raise TypeError(arg)
#     return arg
#
# some_fun(5)
# some_fun("5")
# some_fun(True)
# some_fun([2])
# print(lst)
# def super_wrapper(x: int):
#     def decorator(fun):
#         def inner(value):
#             nonlocal x
#             print("begin inner")
#             res  = fun(value)
#             print("end inner")
#             x += res
#             print("x:",x)
#             return res  +  x
#         return inner
#     return decorator
#
# # @super_wrapper(42)
# def some_fun(value):
#     return value + 3
#
#
# some_fun = super_wrapper(42)(some_fun)
# some_fun(1)
# some_fun(1)
# some_fun(1)
# some_fun(1)
# some_fun(1)


# class Person(object):
#     DEFAULT_HIGH = 1.75 # атрибут класса
#
# def __new__(cls, *args, **kwargs):
#     print("new obj")
#     return super().__new__(cls)
#
# def __init__(self, name: str, age: int, high: float = DEFAULT_HIGH):
#     self.name = name # public
#     self._high = high # protected
#     self.__age = age  # private
#
#
# def set_name(self, name: str) -> None: # метод экземпяра класса
#     self.name = name  # атрибут экземляра класса
#
#
# def set_high(self, high: float) -> None:
#     self._high = high


# @property
# def old(self) -> int:
#     return self.__age
#
# @old.setter
# def old(self, age: int) -> None:
#     self.__age = age
#
# @old.deleter
# def old(self) -> None:
#     del self.__age

# old = property(get_age,set_age,del_age)

# def info(self):
#     print(f"person name: {self.name} age: {self.__age} high: {self._high}")
#
# def go_to_city(self, city):
#     print(f"{self.name} go to {city}")
#
# def __call__(self):
#     return self.__age * 12
#
# def __str__(self):
#     return  f"name: {self.name}"

# def __del__(self):
#     print("del obj")
#     del self

# print(Person().DEFAULT_HIGH)
# person_1 = Person(name="Ivan",age=18)
# person_1._Person__age = 23
# print(person_1._Person__age)
# print(person_1.old)
# print(person_1.__dict__)
# person_1.info()
# person_1.old = 10
# print(person_1.old)
# del person_1.old
# person_1.set_age(24)
# person_1.info()
# person_1.del_age()
# person_1.set_age(27)
# person_1.info()
# print(Person.__dict__)
# person_2 = Person(name="Kolya",age=23,high=1.87)
# # person_1.set_name("Ivan")
# # person_2.set_name("Kolya")
# # person_1.set_high(1.71)
# # person_2.set_high(1.87)
# person_2.info()
# person_2.age = 24
#
# person_1.info()
# person_2.info()
# person_2.go_to_city("Gomel")
# print(person_1)
#
# person_1.info()
#
#
# for i in range(10):
#     person_1.info()
#     time.sleep(1)
#     if i==5:
#         del person_1
# Person.say_name(person_1,"Philip")
# var = 10
# print(type(var).__bases__)
# print(TypeError.__bases__[0].__bases__[0].__bases__[0])
#
# from abc import ABC, abstractmethod
#
# class Weapon(ABC):
#     @abstractmethod
#     def use(self):
#         pass
#
# class Gun(Weapon):
#     color = "black"
#     def use(self):
#         print("bax")
#
# class Automat(Gun):
#     def use(self,shoot_mode  = None):
#         print("bax bax bax") if not shoot_mode else super().use()
#
# class Knife(Weapon):
#     def use(self):
#         print("wjooooox")

# weapon = Weapon()
#
# tokarev = Gun()
# ak_74 = Automat()
# knife = Knife()
#
# tokarev.use()

# ak_74.use()


# knife.use()

# class Player:
#     def take_weapon(self,weapon:Weapon):
#         weapon.use()
#
# player_1 = Player()
# player_1.take_weapon(knife)
# print(ak_74.color)

#
# class Manufacture:
#     def use(self):
#         print("use manufacture logic")
#
#     def construct(self):
#         print("some construct")
#
# class Vehicle(Manufacture):
#     pass
# def use(self):
#     print("use vehicle")

# class Engine(Manufacture):
#     def use(self):
#         print("use engine")
#
# class Car(Vehicle,Engine):
#     pass
# def use(self):
#     print("use car")

# C V E M O
# car = Car()
# car.use()
# print(Car.mro())

# MRO2 Diamond Problem
# MRO3 C3 Linerization Python3 Object


# class ExampleMethodsClass:
#     def __init__(self,attr = None):
#         self.attr = attr
#
#     def some_object_method(self): # метод экземпляра класса
#         print(f"I am object method and have attr: {self.attr}")
#         self.some_static_method()
#
#     @staticmethod
#     def some_static_method(): # cтатический метод
#         print("Some static method")
#
#     @classmethod
#     def  some_class_method(cls, attr = None, policy: str = "admin"):
# print("This is class method")

# cls.some_static_method()
# if attr:
#     return cls(attr)

#
# obj_new = ExampleMethodsClass.some_class_method()
#
# if obj_new:
#     obj_new.some_object_method()
# obj_new.some_object_method()
# object_1 = ExampleMethodsClass(10)
# object_1.some_object_method()
# ExampleMethodsClass.some_static_method()


# Миксин Mixin
# class CalculateMixin:
#     @property
#     def formula(self):
#         return 100
#
#
# class EnergyCalculate(CalculateMixin):
#     def calculate(self, days: int) -> float:
#         return self.formula * days
#
#
# class WaterCalculate(CalculateMixin):
#     def calculate(self, days: int) -> float:
#         return self.formula * days / 12
#
# energy = EnergyCalculate()
# print(energy.calculate(10))
#
# water = WaterCalculate()
# print(water.calculate(10))

#
# user = User("user_1",12)
#
# print(user.name)
# print(user.age)
# print(user)

# table users
# id user age
# 1  Ivan 23

#
from dataclasses import dataclass
#
# @dataclass
# class User:
#     id: int
#     name: str
#     age: int
#     bill: int
#     def __str__(self):
#         return f"user: {self.name}"
#
#
# user_data = {"id":1,"name":"Ivan","age":23,"bill": 24}#"""select from user where id = 1 """
#
# user = User(**user_data)
# user.bill -= 20
# print(user.bill)
# """update user set bill=user.bill where id = user.id """
#
# class CalculateBill:
#     def calculate(self,bill:int,user:User):
#         user.bill -= bill
#         return user

# lst = [1,2,4,5]
#
# gen = (i for i in range(10))
# print(gen)
# for el in gen:
#     print(el)


# class Iterator:
#     def __init__(self, count=10):
#         self.count = count
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count -= 1
#         if self.count > 0:
#             return self.count
#         raise StopIteration
#
# iterator = Iterator()
# for it in iterator:
#     print(it)


# lst = [i for i in range(1,10)]
# new_map = map(lambda x: x**2, lst)
# print(list(new_map))
# for el in new_map:
#     print(el)

# генеративная функция!!!


# def generator_function(counter: int):
#     print("before yielding...")
#     summa = 0
#     for elem in range(counter):
#         x = yield elem
#         summa += x if type(x) == int else 0
#     print(f"summa: {summa}")
#
#
# def generator_function_2(elem):
#     print(elem)
#     yield elem ** 2
#
# gen = generator_function(100)
#
# while True:
#     data = next(generator_function_2(next(gen)))
#     gen.send(data)

# def some_generator():
#     print(1)
#     yield
#     print(2)
#     yield
#     print(3)
#     yield
#     print(4)
#     yield
#     print(5)
#     yield
#     print(6)
#     yield

import os
from pathlib import Path
# name_dir = "test2"

# print(os.getcwd())
# path = "C:\\Users\Denis\PycharmProjects\py70_base"
#
# os.rmdir(path)
#
# is_exist  = os.path.exists(path)
# if not is_exist:
#     os.mkdir(name_dir)

# print(os.listdir("test"))
# file = open(
#     file="test/test.txt",
#     mode="a",
#     encoding="Utf-8"
# )
# path = "test/test.txt"
# mode = "w"
# encoding = "Utf-8"
# with open(
#     file=path,
#     mode=mode,
#     encoding=encoding
# ) as file:
#     lst_str = ["dsada","dsda","dsadsa"]
#     for line in lst_str:
#         file.write(line + "\n")
# lst = []
# names = {}
# for line in file:
#     name, age = line.strip().split()
#     names[name] = int(age)
# print(names)
# json
import json
path = "test/parker_info.json"
mode = "w"
# with open(file=path,mode=mode,encoding='Utf-8') as file:
#     data = json.load(file)
#     print(data["phoneNumbers"])
# data = {
#     "firstName": "Peter",
#     "lastName": "Parker",
#     "gender": "male",
#     "age": 20,
#     "address": {
#         "streetAddress": "101",
#         "city": "NY",
#         "state": "NY"
#     },
#     "phoneNumbers": [
#         {
#             "type": "home",
#             "number": "7349282382"
#         },
#     ]
# }
# with open(file=path,mode=mode,encoding='Utf-8') as file:
#     json.dump(data,file,indent=4)

# path = "test/test_csv.csv"
# mode = "r"
#
# import csv
# data = [
#     [2,2,4,1,5,1,25,24,2],
#     [2,2,4,1,5,1,25,24,2],
#     [2,2,4,1,5,1,25,24,2]
# ]
# with open(path,mode=mode) as file:
#     for line in data:
#         file.write(",".join(line) + "\n")
    # csv_writer = csv.writer(file)
    # for row in data:
    #     csv_writer.writerow(row)

# from csv import reader as csv_reader
# with open(path,mode=mode) as file:
#     data = csv_reader(file,delimiter=";")
#     lst = []
#     for item in data:
#         lst.extend(map(int,item))
# print(lst)