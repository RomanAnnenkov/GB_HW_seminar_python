# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import time

len_first_array = int(input("Введите количество чисел в первом множестве: "))
len_second_array = int(input("Введите количество чисел в втором множестве: "))
first_array = []
second_array = []
for i in range(len_first_array):
    first_array.append(int(input(f"Введите {i + 1}-е число первого множества: ")))
for i in range(len_second_array):
    second_array.append(int(input(f"Введите {i + 1}-е число второго множества: ")))

# решение через алгоритм
start = time.perf_counter()
first_array = tuple(set(first_array))
second_array = tuple(set(second_array))
cross_array = []
for i in first_array:
    if i in second_array:
        cross_array.append(i)
cross_array.sort()
print(*cross_array)
end = time.perf_counter()
first_time = end - start

# решение через пересечение множеств
start = time.perf_counter()
first_array = set(first_array)
second_array = set(second_array)
cross_array = list(first_array.intersection(second_array))
cross_array.sort()
print(*cross_array)
end = time.perf_counter()
second_time = end - start

print(f"Метод intersection быстрее в {round(first_time / second_time, 2)} раз(а)")

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

bush_quantity = int(input("Введите количество кустов: "))
garden_bed = []
for i in range(bush_quantity):
    garden_bed.append(int(input(f"Введите количество ягод на {i + 1}-м кусте: ")))
sum_berries = 0
for i in range(len(garden_bed)):
    previous_index = i - 1
    next_index = i + 1
    if next_index == len(garden_bed):
        next_index = 0
    current_sum = garden_bed[previous_index] + garden_bed[i] + garden_bed[next_index]
    if current_sum > sum_berries:
        sum_berries = current_sum
print(f"За один заход, модуль может собрать максимум {sum_berries} ягод")
