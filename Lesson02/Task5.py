my_list = [7, 5, 3, 3, 2]
print(my_list)
while True:
    num = input('Введите число: ')
    if not num.isdigit():
        print('Нужно ввести число!')
        continue
    ind = -1
    for i in range(0, len(my_list)):
        if int(num) > my_list[i]:
            ind = i
            break
    if ind == -1:
        my_list.append(num)
    else:
        my_list.insert(ind, num)
    print(my_list)
    break
