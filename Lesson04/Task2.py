from random import randint

my_list = [randint(0, 1000) for i in range(randint(30, 100))]
print(len(my_list), my_list)
r_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(len(r_list), r_list)
