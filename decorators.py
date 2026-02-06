#1 Написать декоратор log_result, который печатает результат выполнения функции.
# Применить к функции возведения числа в квадрат.
def decorator(some_fun):
    def inner(n):
        result = some_fun(n)
        print(f'Результат ф-ции {some_fun.__name__} {result}')
        return result
    return inner

@decorator
def some_fun(n):
    return n * 2

print(some_fun(5))

# 2.Написать декоратор repeat(n), который повторяет вызов функции n раз и
# возвращает последний результат.
count_repeat = 5

def repeat(n):
    def inner(count_repeat):
        result = n()
        count = 0
        while count < count_repeat:
            count += 1
            result += 2
        return result
    return inner

@repeat
def some_fun_2():
    return 2

print(some_fun_2(count_repeat))

# 3 Написать декоратор bench, который измеряет ошибки:
# если функция завершилась ошибкой, вывести её тип и сообщение.

a = 0

def bench(fun):
    def inner(x):
        try:
            result_1 = fun(x)
        except BaseException:
            print('ERROR')

    return inner


@bench
def some_fun(x):
    return 10 / x


print(some_fun(a))

# 4 Дан список слов. Получить список их длин.

lst_words = ['a', 'ddda', '']


def decorator(fun):
    def inner(lst):
        result = fun(lst)
        result_1 = [len(x) for x in result]
        return result_1

    return inner


@decorator
def lst_return(lst):
    return lst


print(lst_return(lst_words))

# 5Дан список: ['apple', 'Banana', 'cherry', 'DATE']. Получите новый список, оставив только слова в нижнем регистре.

lst_words_5 = ['apple', 'Banana', 'cherry', 'DATE']


def decorator_5(fun):
    def inner(list):
        result = (list)
        result_1 = [x for x in result if x.islower()]

    return inner


@decorator_5
def return_list_5(lst):
    return lst_words


return_list_5(lst_words_5)

# 6 Дан список кортежей (имя, возраст). Получите новый список,
# оставив кортеж в котором возраст > 18.

lst_of_tupple = [('Vasya', 19), ('Lena', 23), ('Gena', 9)]


def decorator_6(fun):
    def inner(lst):
        result = fun(lst)
        new_list = [(name, age) for (name, age) in lst_of_tupple if age > 18]
        return new_list

    return inner


@decorator_6
def age_person(lst):
    return lst


print(age_person(lst_of_tupple))

# 7.	Дан список списков: [[1,2],[3,4],[5,6]]
# С помощью reduce объединить в один список: [1,2,3,4,5,6].

list_of_list = [[1, 2], [3, 4], [5, 6]]

from functools import reduce

def decorator_7(fun):
    def inner(lst):
        result = fun(lst)
        new_lst = reduce(lambda x, y: x + y, lst)
        return new_lst

    return inner

@decorator_7
def return_list(lst):
    return lst

print(return_list(list_of_list))

# 8.	Дан список ['cat','car','mouse','dog','snake','cow'].
# Получить словарь: {начальная буква: [слова...]}.

lst_8 = ['cat', 'car', 'mouse', 'dog', 'snake', 'cow']

def decorator_8(fun):
    def inner(lst):
        dictionary = {}
        result = fun(lst)
        for item in lst:
            dictionary[item[0]] = item
        return dictionary

    return inner

@decorator_8
def return_lst_8(lst):
    return lst

print(return_lst_8(lst_8))

#9.	Дан список кортежей (товар, цена, количество).
#Получить список сумм: цена * количество.

lst_8 = [('milk', 2.5, 100),('cheese', 4.36, 134),('eggs', 2.3, 20)]

def decorator_8(fun):
    def inner(lst):
        result = fun(lst)
        result = [item[-1] * item[-2] for item in lst]
        return result
    return inner

@decorator_8
def return_lst_8(lst):
    return lst_8

print(return_lst_8(lst_8))


#10.	Написать декоратор cache, который кеширует результаты функции,
#чтобы повторные вызовы с теми же аргументами не вычислялись.

temp = 0

def cache(fun):
    list_of_result = []
    def inner(lst):
        result = fun(lst)
        if not result in list_of_result:
            list_of_result.append(result)
            return result
    return inner

@cache
def return_lst_8(x):
    return x

print(return_lst_8(temp))
print(return_lst_8(2))
print(return_lst_8(0))
print(return_lst_8(2))