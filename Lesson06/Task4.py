class Car:
    speed = 0

    def __init__(self, color, name, is_police = False):
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'{self.name}`s speed - {self.speed}')

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} Go!')

    def stop(self):
        self.speed = 0
        print(f'{self.name} Stop!')

    def turn(self, direction):
        print(f'{self.name} turn {direction}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} speeding! (max speed - 60)')
        else:
            print(f'{self.name}`s speed - {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} speeding! (max speed - 40)')
        else:
            print(f'{self.name}`s speed - {self.speed}')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


t_car1 = TownCar('Red', 'mazda')
t_car1.go(70)
t_car1.show_speed()

s_car1 = SportCar('yellow', 'honda')
s_car1.go(150)
s_car1.show_speed()

w_car1 = WorkCar('grey', 'kamaz')
w_car1.go(35)
w_car1.show_speed()

p_car1 = PoliceCar('white', 'Police')
p_car1.go(50)
p_car1.show_speed()

t_car1.turn('left')
t_car1.stop()
