with open('text_6.txt', 'r', encoding='utf-8') as text6:
    d = dict()
    for el in text6.readlines():
        st = el.split(':')
        st1 = []
        for e in st[1].split():
            st_temp = ''.join(filter(lambda x: x.isdigit(), e))
            st1.append(int(st_temp) if st_temp.isdigit() else 0)
        d.setdefault(st[0], sum(map(int, st1)))
print(d)
