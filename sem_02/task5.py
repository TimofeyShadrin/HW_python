# Реализуйте алгоритм перемешивания списка.
import random


order = list(range(0, 10))
print(f'Initial list: {order}')
random.shuffle(order)
print(f'Shuffled list: {order}')