import math
storlek = int(input('Storlek: '))

vektor1 = []
for i in range(1, storlek + 1):
    tal = float(input(f'Vecktor 1, Tal {i}: '))
    vektor1.append(tal)

vektor2 = []
for i in range(1, storlek + 1):
    tal = float(input(f'Vecktor 2, Tal {i}: '))
    vektor2.append(tal)

summa = 0
for i in range(0, storlek):
    tal1 = vektor1[i]
    tal2 = vektor2[i]
    summa += tal1 * tal2

print(f'{"Ortogonal" if summa == 0 else "Ej ortogonal"}')