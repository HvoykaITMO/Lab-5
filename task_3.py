import re


with open('task3.txt') as f:
    material = f.read()
    data = re.findall(r'\d{4}-\d{2}-\d{2}', material)
    website = re.findall(r'http.{0,1}://\S{,50}?/', material)
    # material2 = re.split((r'\d{4}-\d{2}-\d{2}', r'\d{4}-\d{2}-\d{2}', material)
    material2 = re.sub(r'http.{0,1}://\S{,50}?/', ' ', material)
    material3 = re.sub(r'\d{4}-\d{2}-\d{2}', ' ', material2)
    mail = re.findall(r'\S{,30}?@.{,20}\.com', material3) + re.findall(r'\S{,30}?@.{,20}\.biz', material3) + re.findall(r'\S{,30}?@.{,20}\.info', material3) + re.findall(r'\S{,30}?@.{,20}\.net', material3) + re.findall(r'\S{,30}?@.{,20}\.org', material3)


    print(len(mail))