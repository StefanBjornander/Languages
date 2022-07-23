def ref_demo(a, x):
    return sum([n for n in a if n >= x])

antal = int(input('Antal: '))
list = []

for i in range(1, antal + 1):
    n = int(input(f'Tal {i}: '))
    list.append(n)

limit = int(input('Limit: '))
print(f'ref_demo: {ref_demo(list, limit)}')
