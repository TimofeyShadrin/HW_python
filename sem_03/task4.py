# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import random

number = random.randint(0, 100)
print(number)
result = ''

while number != 0:
    result += str(number % 2)
    number //= 2

data = ''.join(reversed(result))
print(data)
