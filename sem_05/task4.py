# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import json

text = ''

def save():
    with open("text.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(text, ensure_ascii=False))
    print("Saved!")


save()