
# показывает содержимое справочника
def show_data():
    with open('Pyt_hw8\data.txt', 'r', encoding='utf-8') as file:
        book = file.read()#.split('\n')
    return book

# добавляет контакт в справочник     
# не пойму Почему не печатает с новой строки, уже все перепробовала(((( 
# сначала печатал, а потом отвалился, перзагрузка не помогает
def new_data():
     with open('Pyt_hw8\data.txt', 'a', encoding='utf-8') as file:
        file.write(input('\n Введите данные контакта: ' + ' \n'))
    
# ищет информацию в справочнике
def find_data():
    with open('Pyt_hw8\data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('кого ищем?: ')
        for i in book:
            if temp in i:
                print(i)

# Удаляет данные        не пойму почему не изменяет и не удаляет контакт
def delete_contact(name):
    contact = file.read_data()
    with open("Pyt_hw8\data.txt", "w", encoding="utf-8" ) as file:
        for contact in contact:
            if name != contact:
                file.write(contact)

# Изменяет данные
def change_contact(new_name, old_name):
    contact = file.read_data()
    with open("Pyt_hw8\data.txt", "w", encoding="utf-8" ) as file:
        for contact in contact:
            if  old_name != contact:
                file.write(contact)
            else:
                file.write(new_name + "\n")


while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-изменить, 5-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('кого удаляем?: ')
        delete_contact(name)
    elif mode == '4':
        old_name = input('какой контакт переименовать?: ')
        new_name = input('введите имя как переименовать: ')
        change_contact(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('не найдено')
