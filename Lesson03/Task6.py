def int_func(st):
    return st.title()


text = input('Введите строку из маленьких латинских букв: ')
k = ''
for i in range(97, 123):
    k += chr(i)
text_list = text.split()
new_text_list = []
for el in text_list:
    word = ''
    for l in el:
        if l in k:
            word += l
    new_text_list.append(word)
new_text = ' '.join(new_text_list)

print(int_func(new_text))
