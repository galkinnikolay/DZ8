def filling(person):
    with open("example.txt", 'a', encoding='utf-8') as file:
        for el in person:
            file.readline(el + '\n')
        file.readline('\n')