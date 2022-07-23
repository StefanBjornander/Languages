antal = int(input('Antal: '))

list = []
for i in range(1, antal + 1):
    tal = int(input(f'Temperatur {i}: '))
    list.append(tal)

summa = 0
for tal in list:
    summa += tal
medel = summa / antal
print(f'Medel: {medel}')

for (index, tal) in enumerate(list):
    if tal > medel:
        print(f'Temperatur {index + 1}: {tal}')
