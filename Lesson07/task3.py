class Cell():
    cells_count = 0

    def __init__(self, cells_count):
        self.cells_count = cells_count
    
    def __add__(self, other):
        return Cell(self.cells_count + other.cells_count)
            
    def __sub__(self, other):
        if self.cells_count < other.cells_count:
            return 'Меньше 0!'
        else:
            return Cell(self.cells_count - other.cells_count)
    
    def __mul__(self, other):
        return Cell(self.cells_count * self.cells_count)
    
    def __truediv__(self, other):
        return Cell(round(self.cells_count / other.cells_count, 0))
    
    def __str__(self):
        return f'{self.cells_count}'
    
    def make_order(self, cells_in_row):
        cir = self.cells_count // cells_in_row
        cir_tail = self.cells_count % cells_in_row
        st = ''
        for i in range(cir):
            st += ''.join('*' for _ in range(cells_in_row)) + '\n'
        st += ''.join('*' for _ in range(cir_tail))
        return st


c_1 = Cell(12)
c_2 = Cell(6)
print(f'Клетка 1: {c_1}')
print(f'Клетка 2: {c_2}')
print(f'Сложение: {c_1 + c_2}')
print(f'Вычитание: {c_1 - c_2}')
print(f'Умножение: {c_1 * c_2}')
print(f'Деление: {c_1 / c_2}')
print(f'Клетка 1х5: \n{c_1.make_order(5)}')
print(f'Клетка 2х5: \n{c_2.make_order(5)}')
