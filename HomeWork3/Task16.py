# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

#     5
#     1 2 3 4 5
#     3 -> 1

# from random import randint

# my_list = []
# len_list = int(input("Введите количество элементов в массиве: "))
# num_x = int(input("Введите некоторое число X: "))
# count = 0
# for i in range(len_list):
#     my_list.append(randint(1, 10))
#     if my_list[i] == num_x:
#         count += 1
# print(len_list)
# print(my_list)
# print(f"{num_x} -> {count}")

# Идеальное решение

import random

my_list = []
for i in range(15):
    my_list.append(random.randint(0, 10))
print(my_list)
number = int(input("Введите искомое число: "))

print(f"Число {number} встречается в списке {my_list.count(number)} раз")
