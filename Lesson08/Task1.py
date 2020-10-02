class MyDate:
    day = 1
    month = 1
    year = 1900

    def __new__(cls, st):
        date_list = cls.create_date(st)
        if not date_list:
            return None
        if cls.check_date(date_list):
            return object.__new__(cls)
        else:
            pass
            # return None

    def __init__(self, st):
        date_list = MyDate.create_date(st)
        self.day = date_list[0]
        self.month = date_list[1]
        self.year = date_list[2]

    def __str__(self):
        return f'{self.day:02d}-{self.month:02d}-{self.year:d}'

    @staticmethod
    def check_date(d_l):
        if d_l[0] not in range(1, 32):
            print(f'{d_l[0]} - День задан неверно.')
            return False
        elif d_l[1] not in range(1, 13):
            print(f'{d_l[1]} - Месяц задан неверно.')
            return False
        else:
            return True

    @classmethod
    def create_date(cls, st):
        try:
            date_list = list(map(int, st.split('-')))
            return date_list
        except ValueError:
            print(f'{st} - Введите дату в виде "dd-mm-yyyy"')
            return False


md1 = MyDate('s1-32-1999')
md2 = MyDate('42-02-1999')
md3 = MyDate('01-05-2000')
print(md1)
print(md2)
print(md3)
