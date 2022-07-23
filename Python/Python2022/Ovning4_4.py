antal = int(input('Rader: '))

for rad in range(1, antal + 1):
    for column in range(1, antal + 1):
        tal = rad * column
        print(f'{tal:4d}', end = '')
    print()
