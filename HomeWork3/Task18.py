# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

#     5
#     1 2 3 4 5
#     6 -> 5

import random

my_list = []
for i in range(5):
    my_list.append(random.randint(0, 10))
print(my_list)
number = int(input("Введите искомое число: "))

min_dist = float("inf")
nearest = []

for item in my_list:
    if abs(number - item) <= min_dist:
        min_dist = abs(number - item)

if (number - min_dist) in my_list:
    nearest.append(number - min_dist)
if (number + min_dist) in my_list:
    nearest.append(number + min_dist)

print(f"Ближайшее число к {number} будет {nearest}")
