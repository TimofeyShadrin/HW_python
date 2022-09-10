# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


n = int(input('Enter digit: '))


def fib(n: int):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


result=[]
for i in range(-n, n+1):
    if i == 0:
        result.append(0)
    elif i > 0:
        result.append(fib(i))
    else:
        result.append(((-1)**(-i+1))*fib(-i))

print(result)
