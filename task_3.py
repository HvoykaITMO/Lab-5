import re
import csv


def sub_material(ind, a):
    return re.sub(ind, ' ', a)


def find_mail(ind, a):
    k = r'\S{,30}?@.{,30}?\.' + ind
    return re.findall(k, a)


with open('task3.txt') as f:
    material = f.read()
    ID = sorted(list(map(int, re.findall(r'\d{,4}', material))))
    ID = re.findall(r'\d{1,4}', material)
    ID = sorted(set(list(map(int, ID))))
    print(ID)
    surname = re.findall(r'[A-Z][a-z]+', material)

    data = re.findall(r'\d{4}-\d{2}-\d{2}', material)
    website = re.findall(r'http.?://\S{,50}?/', material)

    ind1, ind2 = r'\d{4}-\d{2}-\d{2}', r'http.?://\S{,50}?/'
    material = sub_material(ind1, sub_material(ind2, material))

    mail = []
    check = True
    for i in range(2):
        for el in ['com.', 'biz', 'info', 'net', 'org']:
            if check:
                mail += find_mail(el, material)
            else:
                material = sub_material(r'\S{,30}?@.{,30}?\.' + el, material)
        check = False

    # ID = sorted(list(map(int, re.findall(r'\d+', material))))
    # material = sub_material(r'\d', material)

    print(len(surname), len(data), len(website), len(ID), len(mail))  # переизбыток ID, но их изначально больше.

    with open('task3.csv', 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"')
        for i in range(min(len(surname), len(data), len(website), len(ID), len(mail))):
            pass
            # writer.writerows(for_csv)
