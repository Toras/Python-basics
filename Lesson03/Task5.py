def count_sum(l1):
    l2 = []
    for el in l1:
        if el.strip('-').isdigit():
            l2.append(float(el))

    return sum(l2)


my_list = []
while True:
    my_str = input('Введите строку чисел (q для завершения): ')
    my_list.extend(my_str.split())
    print(f'сумма введенной строки: {count_sum(my_str.split())}, сумма общая: {count_sum(my_list)}')
    if my_list.count('q') != 0:
        break
