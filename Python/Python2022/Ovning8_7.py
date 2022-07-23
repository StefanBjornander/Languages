def binominalkoefficienten(n, k):
    return nfak(n) // (nfak(k) * nfak(n - k))

def nfak(n):
    produkt = 1
    for i in range(1, n + 1):
        produkt *= i
    return produkt

"""
def nfak(n):
    # return 1 if n == 0 else n * nfak(n - 1)
    if n == 1:
        return 1
    else:
        return n * nfak(n - 1)
"""

n = int(input('n: '))
k = int(input('k: '))
print(f'Fakultet: {nfak(n)} {nfak(k)}')
print(f'Binominalkoefficienten: {binominalkoefficienten(n, k)}')
