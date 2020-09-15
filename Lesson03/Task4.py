def my_func1(x, y):
    return x**y


def my_func2(x, y):
    for i in range(1, abs(y)):
        x *= x
    return 1/x


a = input('Введите действительное положительное число x: ')
while True:
    if not a.strip('-').isdigit():
        a = input('Введите число x: ')
        continue
    if float(a) <= 0:
        a = input('Введите действительное положительное число x: ')
        continue
    break
b = input('Введите целое отрицательное число y: ')
while True:
    if not b.strip('-').isdecimal():
        b = input('Введите число y: ')
        continue
    if int(b) > 0:
        b = input('Введите целое отрицательное число y: ')
        continue
    break

print(my_func1(float(a), int(b)))
print(my_func2(float(a), int(b)))
