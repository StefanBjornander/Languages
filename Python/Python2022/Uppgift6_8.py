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

langd = 1
for list in a:
    for j in range(0, langd):
        tal = list[j]
        print(f'{tal:{max_bredd}}', end = ' ')
    langd += 1
    print()
