# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import create_list as cl

numbers = cl.new_list(4, 7, 0.00, 10.00, 2)
print(numbers)

for i in range(len(numbers)):
    fraction = str(numbers[i]).split('.')[1]
    numbers[i] = float('0.' + str(fraction))
print(numbers)

result = max(numbers) - min(numbers)
print(round(result, 2))
