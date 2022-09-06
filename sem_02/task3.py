# Задайте список из n чисел последовательности (1 + 1/n) ** n и
# выведите на экран их сумму.

work = []
def Order(number: int = 1):
    global work
    for i in range(1, number + 1):
        work.append(round(((1 + 1 / i) ** i), 2))

back = True
total = 0
def Result(digit: int):
    global total
    global back
    if digit < 0:
        digit = abs(digit)
        Order(digit)
        total = round(sum(work), 2)
        back = True
    elif digit == 0:
        print('Your input is incorrect! Try again.')
        back = False
    else:
        Order(digit)
        total = round(sum(work), 2)
        back = True

while True:
    try:
        value = int(input('Please enter integer number: '))
        Result(value)
        if back == True:
            print('Elements of your list are: ', end='')
            print(*work, sep=', ')
            print(f'and the sum of all elements of him is: {total}')
            break
    except:
        print('Your input is incorrect! Try again.')