# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

while True:
    x = int(input('Please enter the x coordinate: '))
    y = int(input('Please enter the y coordinate: '))
    if x == 0 and y == 0:
        print('Try again')
    else:                        # without match case
        if x > 0 and y > 0:
            print('One')
            break
        elif x < 0 and y > 0:
            print('Two')
            break
        elif x < 0 and y < 0:
            print('Three')
            break
        else:
            print('Four')
            break
