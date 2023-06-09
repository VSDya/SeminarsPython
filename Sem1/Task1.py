# dist = int(input('Сколько машина проезжает за день: '))
# total = int(input('Сколько надо проехать: '))

# print(f'Машине понадобиться {int((total + dist - 0.1) // dist)} дней')

# print(f'Машине понадобиться {total // dist + (total % dist > 0)} дней')

import math

number = float(input("Введите число: "))

print(number)
print(round(number, 0))
print(math.ceil(number))
print(math.floor(number))
