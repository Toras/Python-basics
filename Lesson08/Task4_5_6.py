class OfficeEquipmentWarehouse:
    storage = dict()

    def __init__(self, name):
        self.oew_name = name

    '''Прием на склад'''
    def reception(self, oe, q):
        oe_in_storage = self.storage.get(oe)
        if oe_in_storage is None:
            self.storage.setdefault(oe, q)
        else:
            self.storage[oe] += q
        print(f'{oe.oq_name} передана на хранение в количестве {q}')

    '''Выдача в подразделение'''
    def commissioning(self, oe, q, division):
        if self.check_balance(oe, q):
            self.storage[oe] -= q
            print(f'{oe.oq_name} в количестве {q} переданы в эксплуатацию в {division}')
        else:
            print(f'На остатке {self.storage[oe]} не хватает {q - self.storage[oe]}')

    '''Проверка остатка номенклатуры'''
    def check_balance(self, oe, q):
        oe_in_storage = self.storage.get(oe)
        if oe_in_storage is None:
            return False
        elif self.storage[oe] >= q:
            return True
        else:
            return False


class OfficeEquipment:
    oq_type = ''
    oq_name = ''
    oq_manufacturer = ''

    def __init__(self, oq_type, oq_name, oq_manufacturer):
        self.oq_type = oq_type
        self.oq_name = oq_name
        self.oq_manufacturer = oq_manufacturer


class Printer(OfficeEquipment):

    def __init__(self, oq_name, oq_manufacturer):
        super().__init__('принтер', oq_name, oq_manufacturer)


class Scanner(OfficeEquipment):

    def __init__(self, oq_name, oq_manufacturer):
        super().__init__('сканнер', oq_name, oq_manufacturer)


class Xerox(OfficeEquipment):

    def __init__(self, oq_name, oq_manufacturer):
        super().__init__('ксерокс', oq_name, oq_manufacturer)


def oq_create(oq_type, oq_name, oq_man):
    if oq_type == 'принтер':
        return Printer(oq_name, oq_man)
    elif oq_type == 'сканнер':
        return Scanner(oq_name, oq_man)
    elif oq_type == 'ксерокс':
        return Xerox(oq_name, oq_man)
    else:
        return OfficeEquipment(oq_type, oq_name, oq_man)


ws_list = []
oe_list = []
cur_w = None

ws_list.append(OfficeEquipmentWarehouse('Первый склад'))
oe_list.append(OfficeEquipment('принтер', 'Принтер 1', 'Производитель 1'))
ws_list[0].storage.setdefault(oe_list[0], 2)

while True:
    choose = input(f'Меню({"склад не выбран" if cur_w is None else cur_w.oew_name}):\n'
                   '"1" - Добавить склад\n'
                   '"2" - Выбрать склад\n'
                   '"3" - Остаток по складу\n'
                   '"4" - Добавить номенклатуру\n'
                   '"5" - Поступление на склад\n'
                   '"6" - Передать в подразделение\n'
                   '"q" - Выход\n')
    if choose == 'q':
        break
    elif choose == '1':
        ws_list.append(OfficeEquipmentWarehouse(input('Имя нового склада: ')))
    elif choose == '2':
        if ws_list:
            for i, el in enumerate(ws_list):
                print(f'{i} - {el.oew_name}')
            cur_w = ws_list[int(input('Выберите склад: '))]
        else:
            print('--Добавьте склад!!!')
    elif choose == '3':
        if cur_w is None:
            print('--Выберите склад!!!')
        else:
            for key, value in cur_w.storage.items():
                print(f'{key.oq_name} - {value}')
    elif choose == '4':
        oq_type = input('сканнер/принтер/ксерокс/свое: ')
        n_name = input('Имя новой номенклатуры: ')
        n_man = input('Производитель: ')
        oe_list.append(oq_create(oq_type, n_name, n_man))
    elif choose == '5':
        if cur_w is None:
            print('--Выберите склад!!!')
        else:
            for i, el in enumerate(oe_list):
                print(f'{i} - {el.oq_name}')
            cur_w.reception(oe_list[int(input('Выберите номенклатуру: '))], int(input('Введите количество: ')))
    elif choose == '6':
        if cur_w is None:
            print('--Выберите склад!!!')
        else:
            for i, el in enumerate(cur_w.storage.keys()):
                print(f'{i} - {el.oq_name}')
            i = int(input('выберите номенклатуру: '))
            cur_w.commissioning(list(cur_w.storage.keys())[i],
                                int(input('Введите количество: ')),
                                input('Введите подразделение: '))
