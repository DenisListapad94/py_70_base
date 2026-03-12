import json

# 1
print("Введите 6 строк:")
with open("file1.txt", "w", encoding="utf-8") as f:
    for _ in range(6):
        line = input()
        f.write(line + "\n")


# 2
print("Введите 3 строки для добавления:")
with open("file1.txt", "a", encoding="utf-8") as f:
    for _ in range(3):
        line = input()
        f.write(line + "\n")


# 3
with open("file1.txt", "r", encoding="utf-8") as f:
    text = f.read()
    count = len(text.replace("\n", ""))
print("Количество символов (без \\n):", count)


# 4
lines_list = []
with open("file1.txt", "r", encoding="utf-8") as f:
    for line in f:
        lines_list.append(line.strip())
print("Список строк файла:")
print(lines_list)


# 5
with open("file1.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
with open("file2.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line.strip() + "!\n")
print("Создан файл file2.txt с восклицательными знаками.")
print("Введите строки (Ctrl+D или Ctrl+Z для завершения):")
try:
    while True:
        line = input()
        if "!" in line:
            print(line)
except EOFError:
    pass


# 6
print("Введите пункт назначения:")
city = input()
with open("flights.json", "r", encoding="utf-8") as f:
    flights = json.load(f)
for flight in flights:
    if flight["destination"] == city:
        print(flight["flight_number"], flight["departure_time"])