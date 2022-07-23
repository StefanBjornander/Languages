import math
antal = int(input('Antal: '))

a = []
for i in range(1, antal + 1):
    list = []
    for j in range(1, antal + 1):
        list.append(i * j)
    a.append(list)

max_bredd = 0
for list in a:
    for tal in list:
        bredd = int(math.log10(tal)) + 1
        if bredd > max_bredd:
            max_bredd = bredd

for list in a:
    for tal in list:
        print(f'{tal:{max_bredd}}', end = ' ')
    print()
