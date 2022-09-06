# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random


quantity = random.randint(2, 10)
work = []


def fill_list():
    global work
    for i in range(quantity):
        work.append(random.randint(-quantity, quantity))

unique = []
size = 0


def create_indexes():
    global size
    size = random.randint(2, quantity)
    list_of_index = []
    global unique
    while len(unique) != size:
        list_of_index.append(random.randint(0, quantity - 1))
        unique = list(set(list_of_index))
    with open("indexes.txt", "w") as file:
        for position in unique:
            file.write(f'{str(position)}\n')


product = 1
indexes = []


def result():
    global product
    global indexes
    with open("indexes.txt", "r") as file:
        for line in file:
            indexes.append(int(line))
            product *= work[int(line)]


fill_list()
create_indexes()
print(f'Количество элементов списка: {quantity}')
print(f'Список: {work}')
print(f'Размер списка с индексами: {size}')
print(f'Список индексов записанный в файл: {unique}\n')
result()
print(f'Список индексов считанный из файла: {indexes}')
print(f'Результат произведение элементов на указанных позициях: {product}')