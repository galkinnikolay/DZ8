def choose_mode():
    mode = input('Выберите режим для работы со справочником: запись или поиск ')
    if mode == 'запись':
        person = fill_person()
    elif mode == 'поиск':
        person = choice_last_name()
    else:
        print('Такого режима не существует!')
        choose_mode()
    return person, mode


def fill_person():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    second_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    return surname, name, second_name, phone

def choice_last_name():
    surname = input('Введите фамилию для поиска: ')
    return surname
    
    