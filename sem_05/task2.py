# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

on_table = 0
quantity = 0


def start():
    global on_table
    global quantity
    while True:
        try:
            # На столе конфет:
            on_table = int(input('Введите количество конфет на столе: '))
            # Сколько конфет можно забрать за один ход:
            quantity = int(input('Сколько конфет можно забрать за один ход: '))
            if on_table > quantity > 0:
                break
            else:
                print('Ваш ввод неверен, проверьте его и поробуйте еще раз!')
        except:
            print('Ваш ввод неверен, проверьте его и поробуйте еще раз!')


who = True


def choice():
    global who
    temp = random.randint(0, 1)
    if temp == 0:
        print('Вы ходите первым!')
        who = True
    else:
        print('Бот ходит первым!')
        who = False


step = 0
count = 0


def step_of_player():
    global step
    global quantity
    global on_table
    while True:
        try:
            step = int(input(f'Введите сколько кофент заберете со стола: '))
            if on_table >= quantity:
                if 0 < step <= quantity:
                    on_table -= step
                    print(f'На столе осталось {on_table} конфет')
                    break
                else:
                    print('Ваш ввод неверен, проверьте его и поробуйте еще раз!')
            else:
                if 0 < step <= on_table:
                    on_table -= step
                    print(f'На столе осталось {on_table} конфет')
                    break
                else:
                    print('Ваш ввод неверен, проверьте его и поробуйте еще раз!')
        except:
            print('Ваш ввод неверен, проверьте его и поробуйте еще раз!')


def pc_step():
    global step
    global on_table
    global quantity
    global who
    global count
    temp = on_table % (quantity + 1)
    if count == 0 and not who:
        step = temp
    elif count > 0 and on_table >= quantity:
        step = quantity + 1 - step
    else:
        step = on_table
    on_table -= step
    print(f'Бот забрал со стола {step} конфет')
    print(f'На столе осталось {on_table} конфет')



#Определим количество ходов:
stop = True


def game():
    start()
    global count
    global stop
    choice()
    global who
    global on_table
    global step
    while on_table != 0:
        if who and count == 0:
            step_of_player()
        elif not who and count == 0:
            pc_step()
        elif count > 0 and who:
            pc_step()
            step_of_player()
            stop = True
        else:
            step_of_player()
            pc_step()
            stop = False
        count += 1
    if not stop:
        print('PC выиграл!')
    else:
        print('Вы победили! Ура!')


game()
