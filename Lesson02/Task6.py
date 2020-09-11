# products = [(1, {"Название": "", "Цена": "", "Количество": "", "ед": ""})]
products = []
analytics = {"Название": [], "Цена": [], "Количество": [], "ед": []}
action = ''
while action != 'выход':
    action = input('Ввести новый товар? (д/н/выход): ')
    if action == 'д':
        name = input('Введите название: ')
        price = float(input('Введите цену: '))
        quantity = float(input('Введите количество: '))
        ed = input('Введите единицу измерения: ')
        products.append((len(products)+1, {"Название": name, "Цена": price, "Количество": quantity, "ед": ed}))
        for el in products:
            print(el)
    elif action == 'н':
        for el in products:
            for key, item in el[1].items():
                analytics[key].append(item)
        for key, el in analytics.items():
            print(key, el)
    elif action == 'выход':
        pass
    else:
        pass
