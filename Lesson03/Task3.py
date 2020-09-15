def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.pop(my_list.index(min(my_list)))
    return sum(my_list)


try:
    print(my_func(float(input('Введите a: ')), float(input('Введите b: ')), float(input('Введите c: '))))
except ValueError as err:
    print(err)
