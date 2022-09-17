# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import json

text = ''

def load():
    try:
        global text
        with open("text.json", "r", encoding="utf-8") as fh:
            text = json.load(fh)
        print("File loaded!")
    except:
        print('Your file not found!')

load()