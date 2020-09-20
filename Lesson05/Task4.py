from translate import Translator

with open('text_4.txt', 'r', encoding='utf-8') as text4:
    content = text4.readlines()
    l_content = []
    for el in content:
        l_content.append(el.split())

translator = Translator(to_lang='ru')
text4new = open('text_4new.txt', 'w', encoding='utf-8')
for el in l_content:
    el[0] = translator.translate(el[0]).split()[-1].title()
    text4new.write(f'{" ".join(el[i] for i in range(0, 3))}\n')
text4new.close()
