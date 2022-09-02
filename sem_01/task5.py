# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
from cmath import sqrt

while True:
    try:
        print('Please enter the coordinates of point A:')
        aX = float(input('\tx = '))
        aY = float(input('\ty = '))
        print('Please enter the coordinates of point B:')
        bX = float(input('\tx = '))
        bY = float(input('\ty = '))
        ab = round(sqrt((bX - aX) ** 2 + (bY - aY) ** 2).real, 2)
        result = str(ab).split('.')
        if int(result[1]) != 0:
            print(f'Result:\n'
                  f'\tA ({round(aX)};{round(aY)}); B ({round(bX)};{round(bY)})'
                  f' -> {ab}')
        else:
            print(f'Result:\n'
                  f'\tA ({round(aX)};{round(aY)}); B ({round(bX)};{round(bY)})'
                  f' -> {result[0]}')
        break
    except:
        print('Try again')
