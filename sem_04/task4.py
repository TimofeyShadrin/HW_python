# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

import random

pow = int(input('Задайте натуральную степень: '))
ratio = [random.randint(0, 5) for _ in range(pow + 1)]

result = []
for i in range(pow):
    if ratio[i] > 1 and pow - i > 1:
        result.append(f'{str(ratio[i])}X^{pow - i}')
    elif ratio[i] > 1 and pow - i == 1:
        result.append(f'{str(ratio[i])}X')
    elif ratio[i] == 1 and pow - i > 1:
        result.append(f'X^{pow - i}')
    elif ratio[i] == 1 and pow - i == 1:
        result.append('X')
if ratio[-1] != 0:
    result.append(str(ratio[-1]))

temp = ' + '.join(result) + ' = 0'

with open("polynom.txt", "a", encoding="utf8") as file:
    file.write(f'Степень: {pow}\n', )
    file.write(f'Список коэффициентов: {ratio}\n')
    file.write(f'Многочлен: {temp}\n')
