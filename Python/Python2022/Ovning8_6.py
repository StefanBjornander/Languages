def rotera(a):
    return a[len(a) - 1:] + (a[:len(a) - 1])

antal = int(input('Antal: '))
list = []
for i in range(1, antal + 1):
    tal = int(input(f'Tal {i}: '))
    list.append(tal)

print(list)
print(rotera(list))