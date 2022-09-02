# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
while True:
    digit = int(input('Please enter the day number in weeks: '))
    if 0 < digit < 6:
        print('No')
        break
    elif digit < 1 or digit > 7:
        print('Try again')
    else:
        print('Yes')
        break
