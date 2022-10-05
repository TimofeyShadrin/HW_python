import keyboard
import time


class TrafficLight:

    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self, time_red: int, time_yellow: int, time_green: int):
        print('For stop - press whitespace with key sticking')
        while not keyboard.is_pressed(' '):
            for i in range(time_red):
                time.sleep(1)
                print(f'\r{self.__color[0]} - ', end=f'{time_red - i}s')
            for i in range(time_yellow):
                time.sleep(1)
                print(f'\r{self.__color[1]} - ', end=f'{time_yellow - i}s')
            for i in range(time_green):
                time.sleep(1)
                print(f'\r{self.__color[2]} - ', end=f'{time_green - i}s')


light = TrafficLight()
light.running(7, 2, 8)
