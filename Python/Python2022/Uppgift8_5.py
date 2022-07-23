def faktorer(n):
    list = []
    for i in range(1, n):
        if n % i == 0:
            list.append(i)
    return list

def ar_perfekt(n):
    l = faktorer(n)
    summa = 0
    for i in l:
        summa += i
    return summa == n

tal = int(input('Tal: '))
print(f'Perfekt: {ar_perfekt(tal)}')
