antal = int(input('Antal: '))

list = []
for i in range(1, antal + 1):
    tal = int(input(f'Tal {i}: '))
    list.append(tal)

written = []
for tal in list:
    if not tal in written:
        print(tal)
        written.append(tal)
