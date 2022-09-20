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

string = input('Введите формулу для ее вычисления: ')


def calc(text: str):
    word = ''

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

    size = 0
    for item in digits:
        if item == '*' or item == '/':
            size += 1
    size = len(digits) - size * 2

    while len(digits) != size:
        if digits[i] == '*':
            digits[i] = str(round(float(digits[i - 1]) * float(digits[i + 1]), 2))
            digits.remove(digits[i + 1])
            digits.remove(digits[i - 1])
            i = 0
        elif digits[i] == '/':
            digits[i] = str(round(float(digits[i - 1]) / float(digits[i + 1]), 2))
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
            digits[i] = str(round(float(digits[i - 1]) - float(digits[i + 1]), 2))
            digits.remove(digits[i + 1])
            digits.remove(digits[i - 1])
            i = 0
        elif digits[i] == '+':
            digits[i] = str(round(float(digits[i - 1]) + float(digits[i + 1]), 2))
            digits.remove(digits[i + 1])
            digits.remove(digits[i - 1])
            i = 0
        i += 1
    return digits


def formula(text: str):
    indexes = []
    result = ''
    if text.find('(') != -1:
        for i in range(len(text)):
            if text[i] == '(' or text[i] == ')':
                indexes.append(i)
        result += text[0:indexes[0]]
        result += ''.join(calc(text[indexes[0]+1:indexes[1]]))
        result += text[indexes[1]+1::]
        temp =''.join(result.split())
        return calc(temp)
    else:
        return calc(text)


out = formula(string)
print('Результат равен = ', end='')
print(*out)