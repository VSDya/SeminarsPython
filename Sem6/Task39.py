# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# from random import randint
# my_list = [randint(0,10) for i in range(15)]
# my_list1 = [randint(0,10) for i in range(5)]
# my_list_final = []
# for i in my_list:
#     if i not in my_list1:
#         my_list_final.append(i)
# print(my_list)
# print(my_list1)
# print(my_list_final)

# Решение от преподавателя

import random
f_list = [random.randint(0,10) for _ in range(10)] # лист комприкейшен
s_list = [random.randint(0,10) for _ in range(5)]
print(f_list, s_list, sep="\n")
print([item for item in f_list if item not in s_list])

