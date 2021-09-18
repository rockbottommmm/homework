import csv

dict_list = [
        {'name': 'Masha', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Vasya', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Eduard', 'age': 48, 'job': 'Big boss'},
    ]
with open('csv_practice.csv', 'w', encoding = 'utf-8', newline = '') as f:
    headers = ['name','age','job']
    writer = csv.DictWriter(f,headers,delimiter = ';')
    writer.writeheader()
    for name in dict_list:
        writer.writerow(name)

