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
            if on_table > 0 and quantity > 0:
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


def step_of_player():
    global step
    global quantity
    while True:
        try:
            step = int(input(f'Введите сколько кофент заберете со стола: '))
            if 0 < step < quantity:
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

    temp = on_table % (quantity + 1)
    if count == 0 and not who:
        step = temp
    else:
        step = quantity + 1 - step


count = 0
#Определим количество ходов:
stop = (on_table // (quantity + 1)) + 1


def game():
    start()
    global count
    global stop
    choice()
    global who
    global on_table
    global step
    while count < stop:
        if who:
            step_of_player()
        else:
            pc_step()
        on_table -= step
        count += 1


game()
