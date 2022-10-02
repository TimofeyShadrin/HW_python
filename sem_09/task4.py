# Иван решил создать самый большой словарь в мире.
# Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение»
# и обновляет созданный им словарь my_dict,
# состоящий всего из одного элемента «first_one» со значением «we can do it».
# Воссоздайте эту функцию.

my_dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs):
    for key, value in kwargs.items():
        my_dict.setdefault(key, value)
    print(my_dict)

biggest_dict(И='Иван', М='Мария', П='Петр', Я='Яна')