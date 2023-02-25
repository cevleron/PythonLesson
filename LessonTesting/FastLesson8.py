# Задача No49.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def all_contacts():
    with open('LessonTesting/phone_number.txt', 'r') as data:
        for line in data:
            print(line)
# all_contacts()

def find_contact(name):
    with open('LessonTesting/phone_number.txt', 'r') as data:
        for line in data:
            if name in line:
                print(line)
# find_contact('Савин')

def add_contact(new_contact):
    with open('LessonTesting/phone_number.txt', 'a') as data:
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
    

while True:
    numb = int(input("Введите 1 для выгрузки всего справочник, 2 для поиска по имени," 
                     "3 для добавления нового контакта , 4 для выхода: "))
    if numb == 4:
        break
    main_menu(numb)





# print('1 - вывести все контакты /n') 
# print('2 - поиск контакта \n') 
# print('3 -добавить контакт \n')
# print('4 - Выход \n')
# file_path = 'phone_book.txt'
# def tasks(task):
#     if task == 4: print("до свидания")
#     else:
#         match task:
#             case 1: # вывести все контакты
#                 with open(file_path, 'r', encoding='utf8') as open_book:
#                     for line in open_book:
#                         print(line)
#                     tasks(int(input("введите номер залачи от 1 до 4: ")))

#             case 2: # поиск контактов
#                 with open(file_path, 'r', encoding='utf8') as open_book:
#                     seach_param = input("Введите параметр для поиска:")
#                 for line in open_book: 
#                     if seach_param in line:
#                         print(line)
#                     tasks(int(input("введите номер залачи от 1 до 4:")))
            
#             case 3: # добавить контакт
#                 with open(file_path, 'a', encoding='utf8') as open_book:
#                     add_n1 = input("Введите фамилию: ")
            
#             case 4:
#                 with open(file_path, 'r', encoding='utf8') as open_book:
#                     print()