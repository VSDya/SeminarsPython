# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# num_a = int(input("Введите число: "))
# num_b = int(input("Введите степень числа: "))
# result = num_a**num_b
# print(f"A = {num_a}; B = {num_b} -> {result}")

num_a = int(input("Введите число: "))
num_b = int(input("Введите степень числа: "))

def degree_of_number(a, b):
    if b == 0:
        return 1
    return a * degree_of_number(a, b - 1)

print(degree_of_number(num_a, num_b))