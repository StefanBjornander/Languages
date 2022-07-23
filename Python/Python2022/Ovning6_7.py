storlek = int(input('Storlek: '))

matris = []
for i in range(1, storlek + 1):
    vektor = []
    for j in range(1, storlek + 1):
        tal = int(input(f'Tal [{i}, {j}]: '))
        vektor.append(tal)
    matris.append(vektor)

"""
storlek = 4
matris = [[16, 9, 2, 7], [6, 3, 12, 13], [11, 14, 5, 4], [1, 8, 15, 10]]
"""

magisk = True
summa = 0
forst = True

for rad in range(0, storlek):
    radsumma = 0
    for column in range(0, storlek):
        radsumma += matris[rad][column]
    if forst:
        summa = radsumma
        forst = False
    elif summa != radsumma:
        magisk = False
        break

if magisk:
    for column in range(0, storlek):
        columnsumma = 0
        for rad in range(0, storlek):
            columnsumma += matris[rad][column]
        if summa != columnsumma:
            magisk = False
            break

if magisk:
    diagonalsumma = 0
    for index in range(0, storlek):
        diagonalsumma += matris[index][index]
    if diagonalsumma != summa:
        magisk = False

if magisk:
    diagonalsumma = 0
    for index in range(0, storlek):
        diagonalsumma += matris[index][storlek - index - 1]
    if diagonalsumma != summa:
        magisk = False

print(f'Magisk: {magisk}')        
