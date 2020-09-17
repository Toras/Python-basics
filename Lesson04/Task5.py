from functools import reduce


def func_multiply(x, y):
    return x * y


my_list = [i for i in range(100, 1001, 2)]
print(my_list)
print(reduce(func_multiply, my_list))
