phone_book =[]
start_phone_book = []
PATH = 'phone_book.txt'


def get_pb():
    return phone_book

def load_file():
    global phone_book, start_phone_book
    with open(PATH,'r', ecoding='utf-8') as file:
        data = file.readline()
    for contact in data:
        contact = contact.split().split(':')
        phone_book.append({'name':contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
    start_phone_book = phone_book.copy()
    
    
def save_file():
    global phone_book
    data= []
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))
    data= '\n'.join(data)
    with open(PATH, 'w', encoding='utf-8') as file:
        file.write(data)


def add_contact(contact: dict):
    
    global phone_book
    phone_book.append(contact)
    
def find_contact(name: str) -> list[dict[str, str]]:
    result = []
    for contact in phone_book:
        for field in contact.values():
            print(field)
            if name in field:
                result.append(contact)
                return result


def change_contact(change_contact: tuple[int, dict[[str , str]]]) -> None:
    index, contact = change_contact
    basic_contact= phone_book.pop(index-1)
    contact={'name': contact.get('name') if contact.get('name') else basic_contact.get('name'),
             'phone': contact.get('phone') if contact.get('phone') else basic_contact.get('phone'),
             'comment': contact.get('comment') if contact.get('comment') else basic_contact.get('comment')}
    phone_book.insert(index-1, contact)
    
def delete_contact(index: int) -> str:
    del_element= phone.book.pop(index-1)
    return del_element.get('name')

def exit_pb() -> bool:
    global phone_book, start_phone_book
    if phone_book == start_phone_book:
        return False
    else:
        return True