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
print("task_1")