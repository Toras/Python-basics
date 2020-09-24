class Road:
    _length = None
    _width = None

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_mass(self, asphalt_mass, asphalt_height) -> float:
        return self._length * self._width * asphalt_mass * asphalt_height


M35 = Road(5000, 20)
print(f'{round(M35.calc_asphalt_mass(25, 5)/1000)} т')
