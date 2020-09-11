seasons = ["Зима", "Весна", "Лето", "Осень"]
month = int(input('Введите номер месяца: '))
if month in [1, 2, 12]:
    print(seasons[0])
elif month in [3, 4, 5]:
    print(seasons[1])
elif month in [6, 7, 8]:
    print(seasons[2])
else:
    print(seasons[3])
