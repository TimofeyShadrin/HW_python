# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
import math

result = []

def Factorial(number: int = 1):
    work = []
    for i in range(1, number + 1):
        work.append(math.factorial(i))
    return work

def Collection(digit: int = 0):
    global result
    if digit < 0:
        digit = -digit
        result = Factorial(digit)
    elif digit == 0:
        result.append(1)
    else:
        result = Factorial(digit)
    print(f'A set of products of numbers is: {result}')

while True:
    try:
        value = int(input('Please enter integer number: '))
        Collection(value)
        break
    except:
        print('Your input is incorrect! Try again.')