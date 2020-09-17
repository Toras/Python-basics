from sys import argv
from itertools import cycle


sc_name, max_i = argv
my_list = ["Меркурий", "Венера", "Земля", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун", "Плутон"]
i = 1
for el in cycle(my_list):
    print(el)
    i += 1
    if i > int(max_i):
        break
