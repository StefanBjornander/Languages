def fyll(a, start, stop, varde):
    assert start >= 0, ('Felaktigt startindex', start)
    assert stop < len(a), ('Felaktigt stopindex', stop)
    assert start <= stop, ('Felaktigta index', start, stop)
    for i in range(start, stop + 1):
        a[i] = varde
    return a

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first = int(input('Forst: '))
last = int(input('Sist: '))

fyll(a, first, last, 2.3)
print(f'fyll: {a}')
