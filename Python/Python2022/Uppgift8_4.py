"""
def nfak(n):
    produkt = 1
    for i in range(1, n + 1):
        produkt *= i
    return produkt
"""

def nfak(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * nfak(n - 1)

tal = int(input('Tal: '))
print(f'Fakultet: {nfak(tal)}')
