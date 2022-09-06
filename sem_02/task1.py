def sumOfDigits(number: float = 0.0):
    temp = str(number).split('.')
    result = 0
    for char in (''.join(temp)):
        result += int(char)
    print(result)

try:

sumOfDigits(0.56)