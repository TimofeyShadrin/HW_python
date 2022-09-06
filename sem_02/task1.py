def sumOfDigits(number: float = 0.0):
    temp = str(number).split('.')
    result = 0
    for char in (''.join(temp)):
        result += int(char)
    print(f'The sum of the digits in your real number is {result}.')

while True:
    try:
        variable = float(input('Please enter real number: '))
        sumOfDigits(variable)
        break
    except:
        print('Your input is incorrect! Try again.')