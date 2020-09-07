earnings = int(input("Введите величину выручки: "))
expenses = int(input("Введите величину издержек: "))
FinResult = earnings - expenses
if FinResult > 0:
    print(f"Фирма работает с прибылью ({FinResult})")
    print(f"Рентальность = {FinResult / earnings :.2f}")
    StaffQ = int(input("Введите количество сотрудников: "))
    print(f"Прибыль на одного сотрудника = {FinResult / StaffQ :.2f}")
elif FinResult < 0:
    print("Фирма работает с убытком")
else:
    print("Фирма работает в 0")
