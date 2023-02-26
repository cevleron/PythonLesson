import pandas as pd
import os


INFILE = 'HomeWork/Contacts/contacts.txt'
OUTFILE = 'HomeWork/Contacts/newcontacts.txt'
def all_contacts():
    with open(INFILE, 'r') as data:
        for line in data:
            print(line)
# all_contacts()

def find_contact(name):
    with open(INFILE, 'r') as data:
        for line in data:
            if name in line:
                print(line)
# find_contact('Савин')

# def delet_contact():
#     name = input("Введите удаляемое имя: ")
#     with open(INFILE, 'r',encoding='utf-8') as data:
#         name = input("Введите удаляемое имя: ")
#         for line in data:
#             if name not in line.():
#                 with open(OUTFILE,'a') as data:
#                     data.write('\n')
#                     print(line)

def delet_contact():
    with open(INFILE, 'r', encoding="utf-8") as infile:
        names = input('Введите Имя или Фамилию для удаления: ')
        lines = infile.readlines()
        with open(INFILE, 'w', encoding="utf-8") as infile:
            for line in lines:
                if names in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    infile.write(line)

# def delet_contact(name):   
#     with open(INFILE, 'r', encoding='utf-8') as infile:    
#         for line in infile:
#             if name in line:
#                 with open(OUTFILE, 'a') as outfile:
#                     outfile.write("\n" + name)
#                 print("Контакт удален")
#             else:
#                 print("Такого имени нет")




# def delet_contact():
#     with open(INFILE, 'r', encoding='utf-8') as infile, open(OUTFILE,'w', encoding='utf-8') as outfile:
#         name = input("Введите удаляемое имя: ")
#         for line in infile:
#             if name not in line:
#                 outfile.write(line)
#                 os.remove(INFILE)
#                 os.rename(OUTFILE,INFILE)
                

def add_contact(new_contact):
    with open(INFILE, 'a') as data:
        data.write('\n' + new_contact)

def main_menu(numb):
    
    if numb == 1:
        all_contacts()
    elif numb == 2:
        name = input("Введите искомое имя: ")
        find_contact(name)
    elif numb == 3:
        data = input("Введите новый контакт: ")
        add_contact(data)
    elif numb == 5:
        # name = input("Введите имя для удаления: ")
        delet_contact()

while True:
    print("1. Выгрузить весь телефонный справочник.")
    print("2. Поиск по ключевому имени")
    print("3. Добавить новый контакт")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Выйти из программы")
    numb = int(input("Введите номер пункта из меню: "))
    if numb == 6:
        break
    main_menu(numb)

