# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

digit = input('Введите число: ')
accuracy = input('Введите точность: ')
result = ''

if len(digit) >= len(accuracy):
    result = digit[0:len(accuracy)]

print(result)
