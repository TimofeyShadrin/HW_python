# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import json
import pickle
from random import shuffle

text = ''


def load(filename='text.json'):
    try:
        global text
        with open(filename, "r", encoding="utf-8") as fh:
            text = json.load(fh)
        print("File loaded!")
    except:
        print('Your file not found!')


dic = {}
words = []


def compress():
    global text
    global dic
    global words
    words = text.strip().split()
    words = list(filter((lambda x: x != ''), words))

    print(words)
    sorted = list(set(words))
    print(sorted)

    i = 0
    while i < len(sorted):

        quantity = 0
        indexes = []

        for j, item in enumerate(words, start=0):
            if item == sorted[i]:
                indexes.append(j)
                quantity += 1

        dic[sorted[i]] = quantity, indexes
        i += 1

    print(dic)


load()
print(text)
compress()


def save():
    with open('result.txt', 'wb') as f:
        pickle.dump(dic, f)
    print("Saved!")


save()
test = {}
size = 0
dec = []


def decompress():
    global test
    global size
    global dec
    with open('result.json', 'rb') as f:
        test = pickle.load(f)
        print('File loaded!')
    for key in test:
        size += test[key][0]
    dec = [str(n) for n in range(size)]
    for key in test:
        temp = test[key][1]
        print(temp)
        for i in range(0, test[key][0]):
            dec[temp[i]] = key


decompress()
print(size)
print(test)
print(dec)

