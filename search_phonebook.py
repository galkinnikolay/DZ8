def search(surname):
    with open("example.txt", 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            if line[:-1] == surname:
                print(line[:-1])
                print(file.readline()[:-1])
                print(file.readline()[:-1])
                print(file.readline()[:-1])
                print()
