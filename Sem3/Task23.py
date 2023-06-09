# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

from random import randint

num = int(input("Введите длину списка: "))
my_list = []
for i in range(num):
    my_list.append(randint(0, 10))
print(my_list)
count = 0
for i in range(len(my_list) - 1):
    if my_list[i + 1] > my_list[i]:
        count += 1
print(count)
