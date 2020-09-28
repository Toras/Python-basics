from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def count_r(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def count_r(self):
        return f'{self.v/6.5 + 0.5:.2f}'


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def count_r(self):
        return f'{2*self.h+0.3:.2f}'


p_1 = Coat(45)
s_1 = Suit(180)
print(p_1.count_r)
print(s_1.count_r)
