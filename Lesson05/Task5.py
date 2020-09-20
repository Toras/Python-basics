from random import randint

with open('text_5.txt', 'w') as text5:
    text5.write(' '.join(map(str, [randint(-1000, 1000) for _ in range(0, randint(10, 1000))])))

with open('text_5.txt', 'r') as text5:
    my_list = map(int, ' '.join(text5.readlines()).split())
    print(f'Сумма в файле = {sum(my_list)}')
