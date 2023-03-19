# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.
import time

list_len = int(input("Введите количество чисел в массиве: "))
numbers_list = []
for i in range(list_len):
    numbers_list.append(int(input(f"Введите {i + 1}-е число: ")))
search_number = int(input("Введите число для поиска в массиве: "))

# решение через сравнение каждого элемента списка
start = time.perf_counter()
count = 0
for i in numbers_list:
    if i == search_number:
        count += 1
print(f"Найдено - {count}")
end = time.perf_counter()
first_time = end - start

# Решение через метод count
start = time.perf_counter()
print(f"Найдено - {numbers_list.count(search_number)}")
end = time.perf_counter()
second_time = end - start

print(f"Метод count быстрее в {round(first_time / second_time, 2)} раз(а)")

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элементк заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

list_len = int(input("Введите количество чисел в массиве: "))
numbers_list = []
for i in range(list_len):
    numbers_list.append(int(input(f"Введите {i + 1}-е число: ")))
search_number = int(input("Введите число для поиска ближайшего к нему числа в массиве: "))

numbers_list.sort()
first_index = 0
last_index = len(numbers_list) - 1
min_number = numbers_list[first_index]
max_number = numbers_list[last_index]

if min == max == search_number:
    print("Нельзя найти ближайшее число, т.к. введены одинаковые числа")
elif search_number > max_number:
    print(f"Ближайшее число: {max_number}")
elif search_number < min_number:
    print(f"Ближайшее число: {min_number}")
else:
    index_closest_number = 0
    min_difference = max
    for i in range(list_len):
        current_difference = search_number - numbers_list[i]
        if current_difference == 0:
            continue
        if current_difference < 0:
            current_difference *= -1
        if current_difference < min_difference:
            min_difference = current_difference
            index_closest_number = i
    closest_numbers = set()
    closest_numbers.add(numbers_list[index_closest_number])
    for i in range(index_closest_number, list_len):
        current_difference = search_number - numbers_list[i]
        if current_difference < 0:
            current_difference *= -1
        if current_difference == min_difference:
            closest_numbers.add(numbers_list[i])
    if len(closest_numbers) == 1:
        print("Ближайшее число: {}".format(*closest_numbers))
    else:
        print("Ближайшие числа: {} {}".format(*closest_numbers))

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

scrabble_word = input("Введите слово для подсчета очков за каждую букву: ").upper()

values_letters = {
    1: ("A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"),
    2: ("D", "G", "Д", "К", "Л", "М", "П", "У"),
    3: ("B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"),
    4: ("F", "H", "V", "W", "Y", "Й", "Ы"),
    5: ("K", "Ж", "З", "Х", "Ц", "Ч"),
    8: ("J", "X", "Ш", "Э", "Ю"),
    10: ("Q", "Z", "Ф", "Щ", "Ъ")
}
current_value = 0
for character in scrabble_word:
    for value in values_letters.keys():
        if character in values_letters[value]:
            current_value += value

print(current_value)
