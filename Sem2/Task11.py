# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# number = int(input("Введите число: "))
# i = 3
# fib_one = 0
# fib_two = 1
# answer = fib_one + fib_two
# while answer < number:
#     fib_one = fib_two
#     fib_two = answer
#     answer = fib_one + fib_two
#     i = i + 1
# if number == answer:
#     print(i)
# else:
#     print(-1)

limit = int(input("Введите число: "))

fib_1 = 0
fib_2 = 1
position = 2

while fib_2 < limit:
    fib_2, fib_1 = fib_2 + fib_1, fib_2
    position += 1

if limit == fib_2:
    print(f"В последовательности Фибоначчи число {fib_2} стоит на {position} позиции")
else:
    print(-1)
