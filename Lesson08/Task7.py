class MyComplex:
    Re = 0
    Im = 0

    def __init__(self, real, fake):
        self.Re = real
        self.Im = fake

    def __add__(self, other):
        return MyComplex(self.Re + other.Re, self.Im + other.Im)

    def __mul__(self, other):
        return MyComplex((self.Re * other.Re - self.Im * other.Im), (self.Re * other.Im + self.Im * other.Re))

    def __str__(self):
        return f'{self.Re}{self.Im:+}i'


c_1 = MyComplex(5, 9)
c_2 = MyComplex(-9, -2)
print(c_1)
print(c_2)
print(c_1 + c_2)
print(c_1 * c_2)
