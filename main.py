import re
import csv


with open('task1-en.txt') as f:
    material = f.read()
    all_words_with_zapyatauya = [el[:-1] for el in re.findall(r'[^\W\d]{2,12}?,', material)]
    all_information_in_square = re.findall(r'\[.{0,100}?\]', material)
    answer_1 = all_words_with_zapyatauya + all_information_in_square


with open('task2.html', 'r') as f:
    try:
        material = ''
        for el in f:
            material += el
    except UnicodeDecodeError:
        pass
    colors_hex = re.findall(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})', material)


with open('task3.txt') as f:
    material = f.read()
    ID = [el.strip() for el in re.findall('\s[\d]{1,8}\s', material)]
    ID = sorted(list(map(int, ID)))
    surname = [el.strip() for el in re.findall('\s[^\d][\w]{2,20}\s', material)]
    mail = [el.strip() for el in re.findall('\s\w+@.{2,40}?\s', material)]
    website = [el.strip() for el in re.findall('\shttp.{2,40}?/\s', material)]
    print(mail)
    data = [el for el in re.findall('\d{4}-\d{2}-\d{2}', material)]


for_csv = [['ID', 'surname', 'mail', 'website', 'data']]
for i in range(min(len(ID), len(surname), len(mail), len(website), len(data))):
    for_csv.append([ID[i], surname[i], mail[i], website[i], data[i]])


with open('task3.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"')
    writer.writerows(for_csv)


with open('task_add.txt') as f:
    material = f.read()
    mail = [el.strip() for el in re.findall('\s\В{2,30}@\.\w{4,}', material)]
    website = [el.strip() for el in re.findall('\shttp.{2,30}?\s', material)]
    # print(mail)


