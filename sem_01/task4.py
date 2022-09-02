#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

infinity = '\u221E'
while True:
    quarter = int(input('Please enter quarter: '))
    if 0 > quarter or quarter > 4:
        print('Try again')
    else:
        match quarter:
            case 1:
                print(f'0 < x < {infinity} and 0 < y < {infinity}')
            case 2:
                print(f'-{infinity} < x < 0 and 0 < y < {infinity}')
            case 3:
                print(f'-{infinity} < x < 0 and -{infinity} < y < 0')