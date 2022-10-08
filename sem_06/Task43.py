# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
import random

numbers = [random.randint(1, 10) for _ in range(8)]
print(numbers)
replay = 0
back = False


def count(item, data=None):
    if data is None:
        data = []
    global replay
    global back
    for el in data:
        if el == item:
            replay += 1
    if replay > 1:
        for el in data:
            for _ in range(replay):
                if el == item:
                    data.remove(el)
                    back = True
    else:
        back = False
    return data


result: list
i = 0
size = len(numbers)
while i < size:
    temp = numbers[i]
    result = count(temp, numbers)
    print(replay)
    if back:
        size -= replay
    else:
        i += 1
    replay = 0
    print(result)
