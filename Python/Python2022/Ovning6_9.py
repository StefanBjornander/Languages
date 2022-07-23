import math
storlek = int(input('Storlek: '))

vektor = []
for i in range(1, storlek + 1):
    tal = int(input(f'Tal {i}: '))
    vektor.append(tal)

kvadratsumma = 0
for tal in vektor:
    kvadratsumma += tal ** 2
langd = math.sqrt(kvadratsumma)
print(f'Langd: {langd}')