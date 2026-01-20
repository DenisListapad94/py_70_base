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
# ENCLOSING замыкающая область функции
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