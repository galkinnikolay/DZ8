from user import choose_mode
from fill_phonebook import filling
from search_phonebook import search

def running():
    person, mode = choose_mode()
    if mode == 'запись':
        filling(person)
    else:
        search(person)