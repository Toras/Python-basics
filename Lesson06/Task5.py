class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title} - Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой "{self.title}"')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашем "{self.title}"')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером "{self.title}"')


s1 = Stationery('бельичья кисть')
s1.draw()
pen1 = Pen('синяя')
pen1.draw()
pencil1 = Pencil('простой')
pencil1.draw()
handle1 = Handle('зеленый')
handle1.draw()
