class OwnErrorCheckDec(Exception):
    def __init__(self, txt):
        self.txt = txt


r_list = []
while True:
    try:
        d = input('Введите число (q for quit): ')
        if d == 'q':
            print(r_list)
            break
        if not d.isdecimal():
            raise OwnErrorCheckDec('Введите число!')
        r_list.append(int(d))
    except OwnErrorCheckDec as err:
        print(err)
    # else:
    #     print(r_list)
