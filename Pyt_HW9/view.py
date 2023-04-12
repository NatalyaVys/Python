
import text_fields as txt


def main_menu ()-> int:
    print('''Главное меню:
          1. открыть файл
          2. сохранить файл
          3. показать все контакты
          4. создать контакт
          5. найти контакт
          6. изменить контакт
          7. удалить контакт
          8. выход''')
    choice = ''
    while True :
        choice = input('введите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < 9 :
            return int(choice)
        else:
            print('введите чисо от 1 до 8')
            
def print_info(message: str):
    print('\n' + '-'*len(message))
    print(message)
    print('-'*len(message) + '\n')

def show_contacts(book: list(dict), message: str):
    if book:
        print('\n' + '-' * 63)
        for n, contact in enumerate(book, 1):
            print(f'{n:>3}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print('-' * 63 + '\n')
    else:
        print(message)
        
        
def new_contact() -> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {'name':name, 'phone': phone, 'comment': comment}

def find() -> str:
    print()
    find = input(txt.input_find)
    return find

def change_contact(book: list, message: str) -> tuple[int, dict[str,str]]:
    index = 0
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book) +1:
            index = int(choice)
            break
    print(txt.enter_or_delete)
    contact = new_contact()
    return index, contact
    
    
def input_del_name(book: list, message: str) ->int:
    while True:
        choice = input (message)
        if choice.isdigit() and 0 < int(choice) < len(book) +1:
            return int(choice)
        

def confirm(message: str) -> bool:
    print()
    answer = input(message + ' (y/n) -> ')
    if answer.lower() == 'y':
        return True
    else:
        return False

