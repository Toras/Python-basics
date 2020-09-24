class Worker:
    _income = {}

    def __init__(self, surname, name, position, wage, bonus):
        self.surname = surname
        self.name = name
        self.position = position
        self._income = {'wage': float(wage), 'bonus': float(bonus)}


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


w1 = Position('Ропшин', 'Виктор', 'Журналист', 15000, 30000)
print(f'{w1.get_full_name()} - {w1.get_total_income()}')
