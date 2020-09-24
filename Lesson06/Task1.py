from time import sleep
from itertools import cycle


class TrafficLight:
    __color = {'red': [7, '\033[31m'], 'yellow': [2, '\033[33m'], 'green': [7, '\033[32m']}

    def running(self):
        i = 0
        for key, value in cycle(self.__color.items()):
            if i > 10:
                break
            i += 1
            print(f'{value[1]}{key}')
            sleep(value[0])


tl_1 = TrafficLight()
tl_1.running()
