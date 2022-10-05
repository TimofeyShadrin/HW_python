class Road:

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calc_mass(self, depth: int):
        return print(f'Asphalt mass is '
                     f'{self._width * self._length * 25 * depth / 1000} '
                     f'metric tons')

mass = Road(20, 5000)
mass.calc_mass(5)
