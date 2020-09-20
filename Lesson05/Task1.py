with open("my_file.txt", "w") as my_file:
    st = None
    while st != "":
        st = input()
        my_file.write(f'{st}\n')
