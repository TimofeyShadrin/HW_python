# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

digit = input('Введите число: ').split('.')
accuracy = input('Введите точность в виде 0.001: ').split('.')
result = ''

while len(digit[1]) != len(accuracy[1]):
    if len(digit[1]) >= len(accuracy[1]):
        result = str(round(float(digit[0] + '.' + digit[1][0:len(accuracy[1]) + 1]), len(accuracy[1])))
    else:
        result = '.'.join(digit)
        for _ in range(len(accuracy[1]) - len(digit[1])):
            result += '0'
    digit = result.split('.')
print(result)
