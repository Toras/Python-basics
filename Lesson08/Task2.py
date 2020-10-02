class OwnErrorDivZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    d1 = int(input('Введите делимое: '))
    d2 = int(input('Введите делитель: '))
    if d2 == 0:
        raise OwnErrorDivZero('На ноль делить нельзя')
    print(d1 / d2)
except ValueError as err:
    print(err)
except OwnErrorDivZero as err:
    print(err)
