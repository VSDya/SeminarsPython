# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Пример
# 2 2
# 4

num_a = int(input("Введите число a: "))
num_b = int(input("Введите число b: "))

def sum_of_number(a, b):
    if a == 0:
        return b
    return sum_of_number(a - 1, b + 1)

print(sum_of_number(num_a, num_b))
