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

string = input('Введите формулу для ее вычисления: ').strip().split()
string = ''.join(list(filter(lambda x: x != '', string)))


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
    print(digits)
    i = 0

    while '*' in digits or '/' in digits:
        if digits[i] == '*':
            digits[i] = str(int(int(digits[i - 1]) * int(digits[i + 1])))
            digits.remove(digits[i + 1])
            digits.remove(digits[i - 1])
            i = 0
        elif digits[i] == '/':
            if int(digits[i + 1]) != 0:
                digits[i] = str(int(int(digits[i - 1]) / int(digits[i + 1])))
                digits.remove(digits[i + 1])
                digits.remove(digits[i - 1])
                i = 0
            else:
                print('На 0 делить нельзя!')
                break
        i += 1
    print(digits)

    while '+' in digits or '-' in digits:
        if digits[i] == '-':
            digits[i] = str(int(digits[i - 1]) - int(digits[i + 1]))
            digits.remove(digits[i + 1])
            digits.remove(digits[i - 1])
            i = 0
        elif digits[i] == '+':
            digits[i] = str(int(digits[i - 1]) + int(digits[i + 1]))
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
        result += ''.join(calc(text[indexes[0] + 1:indexes[1]]))
        result += text[indexes[1] + 1::]
        return calc(result)
    else:
        return calc(text)


out = formula(string)
print('Результат равен = ', end='')
print(*out)
