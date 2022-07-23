text = input('Personnummer: ').replace('-', '')

sum = 0
faktor = 2
for c in text:
    term = faktor * int(c)
    faktor = 1 if faktor == 2 else 2

    if term >= 10:
        sum += term // 10 + term % 10
    else:
        sum += term

print(sum)

if sum % 10 == 0:
    print("Korrekt")
else:
    print('Ej korrekt')

