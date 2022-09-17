# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import json

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
    while i != len(sorted):

        quantity = 0
        indexes = []
        index = 0

        for word in words:
            if word == sorted[i]:
                indexes.append(words.index(word, index))
                index += words.index(word, index) + 1
                quantity += 1

        dic[sorted[i]] = quantity, indexes
        i += 1

    print(dic)


load()
compress()


def save():
    with open("result.json", "w", encoding="utf-8") as fh:
        for key in dic:
            fh.write(json.dumps(key, ensure_ascii=False))
            fh.write(json.dumps(dic[key], ensure_ascii=False))
    print("Saved!")


save()