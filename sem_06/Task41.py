# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
#
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

text = input('Введите формулу для ее вычисления: ')
word = ''
digits = []

for char in text:
    if char == '+':
        word += ' + '
    elif char == '-':
        word += ' - '
    elif char == '*':
        word += ' * '
    elif char == '/':
        word += ' / '
    else:
        word += char


digits = word.split()
i = 0
print(digits)


size = 0
for item in digits:
    if item == '*' or item == '/':
        size += 1
size = len(digits) - size * 2


while len(digits) != size:
    if digits[i] == '*':
        digits[i] = str(round(int(digits[i - 1]) * int(digits[i + 1]), 2))
        digits.remove(digits[i + 1])
        digits.remove(digits[i - 1])
        i = 0
    elif digits[i] == '/':
        digits[i] = str(round(int(digits[i - 1]) / int(digits[i + 1]), 2))
        digits.remove(digits[i + 1])
        digits.remove(digits[i - 1])
        i = 0
    i += 1


size = 0
for item in digits:
    if item == '+' or item == '-':
        size += 1
size = len(digits) - size * 2


while len(digits) != size:
    if digits[i] == '-':
        digits[i] = str(float(digits[i - 1]) - float(digits[i + 1]))
        digits.remove(digits[i + 1])
        digits.remove(digits[i - 1])
        i = 0
    elif digits[i] == '+':
        digits[i] = str(round(float(digits[i - 1]) + float(digits[i + 1]), 2))
        digits.remove(digits[i + 1])
        digits.remove(digits[i - 1])
        i = 0
    i += 1


print(digits)
