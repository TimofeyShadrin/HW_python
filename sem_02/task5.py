# Реализуйте алгоритм перемешивания списка.
import random

order = list(range(30, 40))
print(f'Initial list: {order}')


def check(value=0, test=[]):
    back = False
    for digit in test:
        if value == digit:
            back = True
            break
    return back


positions = []


def indexes():
    global positions
    global order
    size = 1
    while size <= len(order):
        temp = random.randint(0, len(order) - 1)
        if not check(temp, positions):
            positions.append(temp)
            size += 1


product = []


def result():
    global order
    global positions
    global product
    for i in positions:
        product.append(order[i])


indexes()
print(f'Mix indexes: {positions}')
result()
print(f'List have been shuffled: {product}')
