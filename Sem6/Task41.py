# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# Общий зал
# from random import randint
# my_list = [randint(0,10) for _ in range(15)]
# kol = 0
# for i in range(1, len(my_list) - 1):
#     if my_list[i-1] < my_list[i] > my_list[i+1]:
#         kol += 1
# if my_list[-1] < my_list[0] > my_list[1]:
#     kol += 1
# elif my_list[0] < my_list[-1] > my_list[-2]:
#     kol += 1
# print(my_list)
# print(kol)

# Второй зал
# from random import randint
# first_list = [randint(0,10) for _ in range(15)]
# second_list = [1 for i in range(1, (len(first_list) - 1)) if first_list[i-1] < first_list[i] > first_list[i+1]]
# print(first_list)
# print(second_list)
# print(sum(second_list))

# Решение от преподавателя
from random import randint
my_list = [randint(0,10) for _ in range(10)]
count = 0
for i in range(len(my_list)):
    index = i % len(my_list) # бесконечный цикл
    if my_list[(i-1) % len(my_list)] < my_list[i % len(my_list) > my_list[(i+1) % len(my_list)]]:
        count += 1
print(my_list)
print(count)
