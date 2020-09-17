from sys import argv

sc_name, hours, rate, bonus = argv

print(f'Сумма з/п (часы*ставка + премия) = {int(hours) * int(rate) + int(bonus)}')
