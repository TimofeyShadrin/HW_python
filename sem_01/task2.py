#Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for i in [0, 1]:
    for j in [0, 1]:
        for k in [0, 1]:
            test = (not (i or j or k) == (not i and not j and not k))
            print(f'{i}{j}{k} = {test}')

