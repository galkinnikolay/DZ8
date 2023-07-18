from user import choose_mode
from fill_phonebook import filling

def running():
    person, mode = choose_mode()
    if mode == 'запись':
        filling(person)
    else:
        pass