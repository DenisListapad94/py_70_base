# TUPLE
#1.	Дан кортеж. Найти разность между его максимальным и минимальный элементом.
digits_range = (2,4,99,7,8,3,44,14,39,1,3)
print(max(digits_range) - min(digits_range))

#2.
digits_range_2 = (5, 2, -2, 7, -8, -9, 1)
count = 0
for digit in range(len(digits_range_2) - 1):
    if digits_range_2[digit] * digits_range_2[digit + 1] < 0:
        count += 1
print(count)

#3. Дан кортеж. Вывести на экран все простые числа в данном кортеже.
digits_range_3 = (2, 4, 99, 7, 8, 3, 44, 14, 39, 1, 3)
result = []
for digit in digits_range_3:
    if digit <= 1:
        continue
    temp = True
    for i in range(2, digit):
        if digit % i == 0:
            temp = False
            break
    if temp:
        result.append(digit)
print(result)

#5.	*Дан кортеж. Без функций и дополнительных списков вывести все повторяющиеся элементы. (count не использовать). (1,2,4,1,2,6) 1 2
digits_range_5 = (1, 2, 4, 4, 1, 2, 6, 6, 6, 6)
result_5 = []
for digit in range(len(digits_range_5)):
    for item in range(digit + 1, len(digits_range_5)):
        if digits_range_5[digit] == digits_range_5[item]:
            if digits_range_5[digit] not in result_5:
                result_5.append(digits_range_5[digit])
            break
print(result_5)

#LIST
#6.	Задано два списка. Найти наименьшие среди элементов первого списка, которые не входят во второй список.
#[4,1,6,9]  [8,1,2,4,9,5,7,6] -> нет такого элемента
list1 = [4, 1, 6, 9, 10, 13]
list2 = [8, 1, 2, 4, 9, 5, 7, 6]
unique_elements = []
for digit in list1:
    if digit not in list2:
        unique_elements.append(digit)
if len(unique_elements) > 0:
    print("Наименьший элемент:", min(unique_elements))
else:
    print("Нет такого элемента")

#7.	Дан список положительных целых чисел . Вставить после каждого чётного числа его перевёртыш. 18 81, 42 24, 8 8, 122 221
digits_range_7 = [4,18,24,221,8,8]
result = []
for digit in digits_range_7:
    if digit % 2 == 0:
        result.append(str(digit))
        result.append(str(digit)[::-1])
    else:
        result.append(str(digit))
print(' '.join(result))

#8 Дан список . Вычислить сколько раз в нем встречается каждый элемент, не используя сортировки. [5,2,4,5,1,2] 1 – 1 2 – 2 4 – 1 5 - 2
digits_range_8 = [5,2,4,5,1,2]
result_list = []
for digit in digits_range_8:
    count = digits_range_8.count(digit)
    result_list.append(f'{digit} - {count}')
print(set(result_list))

#9.	 *Дан список . Перезаписать его так, чтобы сначала были все положительные числа, а затем все отрицательные и нули, сохраняя порядок их следования. [5,2,0,-2,-7,1,8,0,-1] -> [5,2,1,8,-2,-7,-1,0,0]
digits_range_9 = [5, 2, 0, -2, -7, 1, 8, 0, -1]
positives = []
negatives = []
zeros = []
for x in digits_range_9:
    if x > 0:
        positives.append(x)
    elif x < 0:
        negatives.append(x)
    else:
        zeros.append(x)
new_digits_range_9 = positives + negatives + zeros
print(new_digits_range_9)

#10.	*Дан список . Продублировать все неповторяющиеся элементы.[5,2,7,3,8,2,4,1,6,5] -> [5,2,7,7,3,3,8,8,2,4,4,1,1,6,6,5]
digits_range_10 = [5, 2, 7, 3, 8, 2, 4, 1, 6, 5]
result_list = []
for digit in digits_range_10:
    count = digits_range_10.count(digit)
    result_list.append(digit)
    if count == 1:
        result_list.append(digit)
print(result_list)

#11
numbers = input().split()
seen = set()
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)

#13
school = {"9а": 25,"9б": 27,"9в": 24,"9м": 26,"9ф": 23}
school["9б"] = 28
school["9г"] = 22
del school["9ф"]
total = 0
for students in school.values():
    total += students
print("Всего учеников в 9 классах:", total)
