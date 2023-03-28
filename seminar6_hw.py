# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def get_arithmetic_progression(first: int, diff: int, quantity: int):
    result = [first]
    for i in range(1, quantity):
        result.append(result[i - 1] + diff)
    return result


print("программа для генерации арифметической прогрессии.")
first_element = int(input("Введите первый элемент: "))
difference = int(input("Введите разность: "))
element_quantity = int(input("Введите количество элементов: "))

arithmetic_progression = get_arithmetic_progression(first_element, difference, element_quantity)
print(*arithmetic_progression)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random


def get_indexes_entries_in_range(input_list: list, min_val: int, max_val: int):
    indexes = []
    for i in range(len(input_list)):
        if min_val <= input_list[i] <= max_val:
            indexes.append(i)
    return indexes


input_list = [random.randint(1, 30) for _ in range(10)]
input_min = int(input("Введите минимальное значение: "))
input_max = int(input("Введите максимальное значение: "))

print(input_list)
indexes_entries_in_range = get_indexes_entries_in_range(input_list, input_min, input_max)
print(indexes_entries_in_range)
