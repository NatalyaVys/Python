no_contact_or_file = 'телефонная книга пуста или не окрыта'

load_successful = 'телефонная книга успешно загружена'
save_successful = 'телефонная книга успешно сохранена'


new_contact_successful = 'контакт успешно создан!'

new_name = 'введите фио контакта:' 
new_phone = 'введите телефон контакта: '
new_comment = 'введите комментарий к контакту: '


is_changed ='были внесены изменения. сохранить?'

input_find = 'введите кого ищем: '
not_find = 'контакт не найден'

empty_or_not_open_file = 'телефонная книга пуста или файл не открыт'
input_index = 'введите номер изменяемого контекта'
def change_successful(name: str) -> str:
    return f'контакт {name} успешно сохранен'
    

enter_or_delete='введите новые значения или оставьте без изменения'

def confirm_delete(name: str) -> str :
    return 'вы точно хотите удалить контакт?'

del_contact(name: str) -> str:
    return 'контакт успешно удален!'

bye_bye = 'до свидания! Всего хорошего!'