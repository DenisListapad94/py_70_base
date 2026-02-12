#1.	Дано число n. Вывести все числа от 1 до n.
n_1 = 30
for digits in range(n_1):
    print(digits)

#2.	Вывести на экран число "10" 20 раз столбиком.
num_2 = 10
iteration = 20
while iteration > 0:
    print(num_2)
    iteration -= 1

#3. Дано число n. Посчитать сумму всех чётных чисел от 0 до n.
n_3 = 5
result_3 = 0
for digits in range(n_3):
    if digits % 2 == 0:
        result_3 += digits
print(result_3)

#4 Дано натуральное число. Определить произведение цифр в нем которые кратны 2, кроме числа 0.
num_4 = 1250
num_4_to_string = list(str(num_4))
result = 1
for digits in num_4_to_string:
    if int(digits) == 0:
        continue
    elif int(digits) % 2 == 0:
        result *= int(digits)
print(result)

#5.Дано натуральное число n. Вывести на экран факториал этого числа. Например: 5! = 1 * 2 * 3 * 4 * 5 = 120
num_5 = 5
result_5 = 1
while num_5 > 0:
    result_5 *= num_5
    num_5 -= 1
print(result_5)

#7.	Дано число n. Найти сумму цифр в этом числе.
num_7 = 3090
num_7_to_string = list(str(num_7))
result_sum = 0
for digits in num_7_to_string:
    result_sum += int(digits)
print(result_sum)

#6 Дано число n. Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше n.
num_n_6 = 25
result = []
for digits in range(num_n_6):
    if digits < 1:
        continue
    elif digits ** 2 <= num_n_6:
        result.append(digits ** 2)
    else:
        break
print(result)

#8 Дано натуральное число n. Найти значение минимальной цифры в данном числе .
num_n = 201388513411
num_n_to_string = list(str(num_n))
result = int(num_n_to_string[1])
for item in num_n_to_string:
    if int(item) < result:
        result = int(item)
print(result)

#9 Дан текст. Написать программу, вставляющую после каждой запятой по одному пробелу.
# Если в тексте встречается два и более пробелов, требуется оставить один.
text = input("Введите текст: ")
text = text.replace(",", ", ")
while "  " in text:
    text = text.replace("  ", " ")
print(text)

#10
num = int(input())
for digit in range(1, num + 1):
    if 11 <= digit % 100 <= 14:
        word = "коров"
    else:
        last_digit = digit % 10
        if last_digit == 1:
            word = "корова"
        elif 2 <= last_digit <= 4:
            word = "коровы"
        else:
            word = "коров"
    print(f"На лугу {digit} {word}")



