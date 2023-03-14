# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
coin_quantity = int(input("Введите количество монет : "))
zero_count = 0
one_count = 0
for coin in range(coin_quantity):
    current_coin = int(input(f"Введите сторону на которой лежит {coin + 1}-я монета(орел - 1, решка - 0): "))   
    while current_coin < 0 or current_coin > 1:
        print("ошибка ввода, ведите 0 или 1")
        current_coin = int(input(f"Введите сторону на которой лежит {coin + 1}-я монета(орел - 1, решка - 0): "))
    if current_coin == 0:
        zero_count += 1
    else:
        one_count += 1
if zero_count > one_count:
    print(f"Минимальное количество монет, которые нужно перевернуть {one_count}.")
else:
    print(f"Минимальное количество монет, которые нужно перевернуть {zero_count}.")

# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# математическое решение
prompt_sum = int(input("Введите подсказку - сумма чисел: "))
prompt_multiplication = int(input("Введите подсказку - произведение чисел: "))
d = prompt_sum ** 2 - 4 * (-1 * -prompt_multiplication)
y = round(-1 * ((-prompt_sum + d ** 0.5) / 2))
x = round(prompt_sum - y)
print(f"Петя загадал {x} {y}")
# решение через подбор
prompt_sum = int(input("Введите подсказку - сумма чисел: "))
prompt_multiplication = int(input("Введите подсказку - произведение чисел: "))
numbers_are_found = False
for x in range(prompt_sum):
    if numbers_are_found:
        break
    for y in range(prompt_sum):
        if x + y == prompt_sum and x * y == prompt_multiplication:
            print(f"Петя загадал {x} {y}")
            numbers_are_found = True

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2 ** k), 
# не превосходящие числа N.
print("Программа выводит все целые степени двойки не превосходящие числа N")
border_number = int(input("Введите число N: "))
for i in range(1, border_number):
    print_number = 2 ** i
    if print_number <= border_number:
        print(print_number, end=" ")
print()
