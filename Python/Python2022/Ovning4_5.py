slut_ar = int(input('Ar: '))
invanare = 26000

for ar in range(2020, slut_ar + 1):
    fodda = int(0.007 * invanare)
    doda = int(0.006 * invanare)
    print(f'f {fodda} d {doda}')
    andring = fodda - doda + 300 - 325
    print(f'a {andring}')
    invanare += andring
    print(f'{ar}: {invanare}')
