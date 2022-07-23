import math

matar_idag = int(input('Matarstallning idag? '))
matar_ett_ar = int(input('Matarstallning for ett ar sedan? '))
antal_korda_mil = matar_idag - matar_ett_ar
print(f'Antal korda mil: {antal_korda_mil:d}')

liter_bensin = float(input('Antal liter bensin: '))
forbrukning_per_mil = liter_bensin / antal_korda_mil
print(f'Forbrukning per mil: {forbrukning_per_mil:.2f}')
