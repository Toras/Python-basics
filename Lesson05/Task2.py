with open("text_2.txt", "r", encoding="utf-8") as text2:
    all_list = text2.readlines()
    print(f'Количество строк: {len(all_list)}')
    for el in all_list:
        print(f'Количество слов в строке №{all_list.index(el)+1}: {len(el.split())}')
