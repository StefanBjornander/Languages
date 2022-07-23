def Maclaurin(x):
    term = 1
    i = 0
    summa = 0
    while term >= 1e-7:
        term = x ** i / nfak(i)
        summa += term
        i += 1
    return summa

def nfak(n):
    produkt = 1
    for i in range(1, n + 1):
        produkt *= i
    return produkt

x = int(input('x: '))
print(f'Maclaurin: {Maclaurin(x):.3}')

