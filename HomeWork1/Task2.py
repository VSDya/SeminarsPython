# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input("Введите трехначное число: ")
if len(number) != 3:
    print("Это не трехначное число")
else:
    result = int(number[0]) + int(number[1]) + int(number[2])
    print(f"{number} -> {result} ({number[0]} + {number[1]} + {number[2]})")
