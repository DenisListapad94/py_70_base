#1.	Напишите функцию m(a, b), вычисляющую минимум двух чисел. С помощью вашей функции найдите минимальное четырёх чисел.
import random

def m(a, b:int) ->int:
    return min(a,b)
print(m(m(7,3),m(2,4)))

#2	Дано натуральное число n > 1. Проверьте, является ли оно совершенным. Программа должна вывести слово YES, если число совершенное и NO, в противном случае.
n = 6
def perfect_or_no(num:int)->str:
    arr = []
    for i in range(1,num):
        if num % i == 0:
            arr.append(i)
    return 'Yes' if sum(arr) == num else 'No'
print(perfect_or_no(n))
def perfect_or_no_compr(num):
    return 'Yes' if sum([i for i in range(1, n) if n % i == 0]) == n else 'No'
print(perfect_or_no_compr(n))

result = [[[random.randint(10,90)]  for _ in range(4)]]


#Напишите функцию fib(n),
# которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
n = 9


def find_fib(n: int) -> int:
    fib_1, fib_2 = 0, 1

    arr_fib = [0, 1]

    for _ in range(1, n):
        fib = fib_1 + fib_2
        arr_fib.append(fib)
        fib_1 = arr_fib[-1]
        fib_2 = arr_fib[-2]
    return arr_fib[-1]


print(find_fib(n))


#4
num = 6


def closest_mod_5(n: int) -> int:
    if n % 5 == 0 and n >=num:
        return n
    else:
        return closest_mod_5(n+1)


print(closest_mod_5(num))

#6
list_nums = [num for num in range(1, 100) if not num % 2 == 0]
print(list_nums)

#7
list_nums_2 = [num for num in range(1, 1000) if num % 3 == 0 and num % 5 == 0]
print(list_nums_2)

#8Напишите функцию которая определяет количество в нем различных элементов. set функцию не использовать.
arr = [{}, 0, None, None, 'a', 'a', 'aaa', 5555, 'bbbcs', 'lovers', 'lovers', 'lovers', '1111111111']
def count_unic(arr: list) -> int:
    temp = arr[0]
    count = 1

    for item in arr[1:]:
        if item != temp:
            count += 1
            temp = item
    return count
print(count_unic(arr))


#9
list_nums = '1 3 5 6 10'
def sum_neibor(list_nums: list) ->list:
    arr_nums = list_nums.split(' ')
    new_arr_nums = [int(item) for item in arr_nums]
    new_arr = []
    if len(new_arr_nums) == 1:
        return ''.join(map(str, new_arr_nums))
    for index in range(len(new_arr_nums)):
        if index == 0:
            new_arr.append(new_arr_nums[1] + new_arr_nums[-1])
            continue
        if index == len(new_arr_nums) - 1:
            new_arr.append(new_arr_nums[0] + new_arr_nums[-2])
            continue
        else:
            new_arr.append(new_arr_nums[index - 1] + new_arr_nums[index + 1])
    return ' '.join(map(str,new_arr))

print(sum_neibor(list_nums))


#10.	Дан список, состоящий из строк. Отсортировать его по длине слов. Сначала должны идти длинные слова затем короткие.
arr = ['', 'aaa', 'a', 'bbbcs', '0av', 'ff', 'etstetetesfdsf']
def findHight(arr: list) -> int:
    hight = len(arr[0])
    hight_index = 0
    for item in range(len(arr)):
        if len(arr[item]) > hight:
            hight  = len(arr[item])
            hight_index = item
    return hight_index

def selection(arr: list) -> list:
    newArr = []
    for item in range(1, len(arr)):
        findHightest = findHight(arr)
        newArr.append(arr.pop(findHightest))
    return newArr

print(selection(arr))

#11.	Дан список состоящий из слов. Отсортировать его по количеству вхождений буквы 'a'
words = ['aabc', 'abcabba', 'a', 'baba']

def find_count_min(arr):
    min_count = arr[0].count('a')
    min_count_index = 0
    for item in range(1, len(arr)):
        if arr[item].count('a') < min_count:
            min_count = arr[item].count('a')
            min_count_index = item
    return min_count_index

def selection(arr):
    new_arr = []
    for item in range(len(arr)):
        min_count = find_count_min(arr)
        new_arr.append(words.pop(min_count))
    return new_arr


print(selection(words))