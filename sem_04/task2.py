# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

import math

number = int(input('Задайте натуральное число: '))
result = []

while number % 2 == 0:
    result.append(2)
    number /= 2

for i in range(3, int(math.sqrt(number)) + 1, 2):
    while number % i == 0:
        result.append(i)
        number /= i

if number > 2:
    result.append(number)

print(f'Список простых множитлей: ', end='')
print(*result, sep=', ', end='.')
