# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = input('Enter string: ').replace('абв', '').split(' ')
result = ' '.join(list(filter(lambda x: x != '', str)))
print(result)
