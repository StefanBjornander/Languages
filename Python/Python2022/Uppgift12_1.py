list = []

while True:
    text = input('Farger: ')

    if text.strip() == '':
        break

    list.append(set(text.split(' ')))

u = set(list[0])
i = set(list[0])

for s in list[1:]:
    u = set.union(u, s)
    i = set.intersection(i, s)

print('union:', u)
print('intersection:', i)
    