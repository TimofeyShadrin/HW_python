# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import create_list as cl

numbers = cl.new_list(4, 9, 0, 9)
print(numbers)

result = []

for i in range(len(numbers) // 2):
    result.append(numbers[i] + numbers[len(numbers) - 1 - i])

if len(numbers) % 2 == 1:
    i = len(numbers) // 2
    result.append(numbers[i] * 2)

print(result)
