def fyll(a, start, stop, varde):
    for i in range(start, stop + 1):
        a[i] = varde
    return a

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fyll(a, 5, 9, 2.3)
print(f'fyll: {a}')
