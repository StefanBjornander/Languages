list_antal = int(input('Listans storlek: '))
list = []
for i in range(1, list_antal + 1):
    tal = int(input(f'  Tal {i}: '))
    list.append(tal)

tuple_antal = int(input('Tuplens storlek: '))
tuple_list = []
for i in range(1, tuple_antal + 1):
    tal = int(input(f'  Tal {i}: '))
    tuple_list.append(tal)
tuple = tuple(tuple_list)

if len(list) == len(tuple):
    for i in range(0, len(list)):
        if list[i] != tuple[i]:
            print('Ej lika')
            break
    else:
        print('Lika')
else:
    print('Ej lika')