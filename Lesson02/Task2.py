my_list = []

while True:
    todo = input('Ввести новый элемент списка? (y/n): ')
    if todo == 'n':
        break
    my_list.append(input('Введите новый элемент списка: '))

print(f'Введенный список: {my_list}')

for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(f'Измененный список: {my_list}')
