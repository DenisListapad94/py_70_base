#1 Опишите конструкцию отлова ошибок, так чтобы выводило, какую ошибку вы сделали. Код представлен ниже:
try:
    x = (1, 2, 5, 7)
    x = x / 2
except TypeError:
    print("Невозможно разделить кортеж на число")

#2
list_arr = [1,2,3]
try:
    print(list_arr[1])
    print(list_arr[5])
except IndexError:
    print("Такого элемнта нет в списке")

#3
try:
    import math
    a, b, c = map(int, input().split())
    if a == 0 or b == 0 or c == 0:
        raise ArithmeticError
    p = (a + b + c) / 2
    square = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(square)
except ArithmeticError:
    print('Сторона треугольника не может быть равной нулю')

#4
list_arr_4 = [1,2,3]
try:
    element = int(input('ведите элемент для удаления из списка'))
    if element in list_arr_4:
        find_elem = list_arr_4.index(element)
        del list_arr_4[find_elem]
        print(f'{element} удален из списка')
    else:
        raise TypeError
except TypeError:
    print('Такого элемента нет в списке')

#5
try:
    dict_list_shop = {'йогурт': '2р', 'каша': '3,5р', 'сыр': '4р' }
    dict_list_shop_key = input('введите название продукта')
    if dict_list_shop_key not in dict_list_shop:
        raise KeyError
    else:
        print(dict_list_shop[dict_list_shop_key])
except KeyError:
    print('Нет такого продукта')

#6
str_6 = "10 5 abc 3"
str_to_list = str_6.split()
sum_6 = 0
for item in str_to_list:
    try:
        sum_6 += int(item)
    except ValueError:
        continue
print(sum_6)

#7

a = "aaa bb ss rra aa b"
#a = 55

try:
    str_to_list = list(a)
    temp = []
    for item in str_to_list:
        if item in temp or item == ' ':
            continue
        else:
            print(f'{item} - {str_to_list.count(item)}')
            temp.append(item)
    del temp
except TypeError:
    print('Входные данные должны быть строковые')


try:
    dicti = {}
    for item in a:
        if item == ' ':
            continue
        if item in dicti:
            dicti[item] += 1
        else:
            dicti[item] = 1
    for key, val in dicti.items():
       print(f'{key} - {val}')
except TypeError:
    print('Входные данные должны быть строковые')

#8
arr = [20,30,40,50,60,70,80,90,100,110]
x = 20
if arr != sorted(arr):
    raise ValueError
try:
    left = 0
    right = len(arr) - 1
    while left <= right:
        arr_midle = (left + right) // 2
        mid = arr[arr_midle]
        if mid == x:
            print(f"Найден {mid} по индексу {arr_midle}")
            break
        elif x > mid:
            left = arr_midle + 1
        else:
            right = arr_midle - 1
    else:
        print(None)
except ValueError: print('Список не отсортирован')

