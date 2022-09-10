import random


def new_list(min_size: int, max_size: int, min_value: int, max_value: int):
    size = random.randint(min_size, max_size)
    numbers = []
    for _ in range(size):
        numbers.append(random.randint(min_value, max_value))
    return numbers


def new_list(min_size: int, max_size: int, min_value: float, max_value: float, accuracy: int):
    size = random.randint(min_size, max_size)
    numbers = []
    for _ in range(size):
        numbers.append(round(random.uniform(min_value, max_value), accuracy))
    return numbers