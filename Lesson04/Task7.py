def fact(n):
    for i in range(1, n+1):
        yield i


for el in fact(4):
    print(f'{el}')
