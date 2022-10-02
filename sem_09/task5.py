# Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

import random

my_string = ' '.join([str(random.randint(0, 9)) for _ in range(40)])
print(my_string)


def count_it(sequence: str):
    my_keys = list(filter(lambda x: x != ' ', set(sequence.strip())))
    my_list = sequence.strip()
    result = {}
    for item in my_keys:
        result.setdefault(item, my_list.count(item))
    result = dict(sorted(result.items(), key=lambda x: x[1]))
    result_dict = {}
    for i in range(3):
        temp = result.popitem()
        result_dict.setdefault(temp[0], temp[1])
    print(result_dict)


count_it(my_string)
