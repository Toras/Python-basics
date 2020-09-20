with open('text_3.txt', 'r', encoding='utf-8') as text3:
    content = text3.readlines()
    d = dict()
    for el in content:
        d.setdefault(el.split()[0], float(el.split()[1]))
print('Сотрудники с окладом менее 20000: ')
for key, value in d.items():
    if value < 20000:
        print(key)
print(f'Средний доход сотрудников: {sum(d.values())/len(d.keys()):.2f}')
