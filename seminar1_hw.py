# Задача 2: Найдите сумму цифр трехзначного числа.
number = int(input("Введите трехзначное число: "))
sum = 0
while number != 0:
    sum = sum + number % 10
    number //= 10
print(sum)

# # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# # Вместе они сделали S журавликов.
# # Сколько журавликов сделал каждый ребенок, если известно,
# # что Петя и Сережа сделали одинаковое количество журавликов,
# # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# total = int(input("Ведите общее количество журавликов: "))
# if total % 6 == 0:
#     p = total // 6
#     k = p * 4
#     s = p
#     print(f"{p} {k} {s}")
# else:
#     print("ошибка ввода, возможно вы неверно посчитали журавликов")

# # Задача 6: Вы пользуетесь общественным транспортом?
# # Вероятно, вы расплачивались за проезд и получали билет с номером.
# # Счастливым билетом называют такой билет с шестизначным номером,
# # где сумма первых трех цифр равна сумме последних трех.
# # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# # Вам требуется написать программу, которая проверяет счастливость билета.
# ticket_number = input("Введите номер билета: ")
# if len(ticket_number) == 6:
#     first_part_sum = 0
#     second_part_sum = 0
#     for i in range(0, len(ticket_number)):
#         if i < 3:
#             first_part_sum += int(ticket_number[i])
#         else:
#             second_part_sum += int(ticket_number[i])
#     if first_part_sum == second_part_sum:
#         print("yes")
#     else:
#         print("no")
# else:
#     print("ошибка ввода, номер былета должен быть шестизначным")

# # Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# # долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
# # (то есть разломить шоколадку на два прямоугольника).
# n = int(input("Введите число n: "))
# m = int(input("Введите число m: "))
# k = int(input("Введите число k: "))
#
# if k % n == 0 or k % m == 0:
#     print("yes")
# else:
#     print("no")

