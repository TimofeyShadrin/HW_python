# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

size = random.randint(5, 7)
numbers = []

for _ in range(size):
    numbers.append(random.randint(0, 10))

print(numbers)

result = 0
for i in range(size):
    if i % 2 == 1:
        result += numbers[i]

print(result)

