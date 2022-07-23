antal = int(input('Antal: '))

list = []
for i in range(1, antal + 1):
    tal = int(input(f'Tal {i}: '))
    list.append(tal)

while 0 in list:
    list.remove(0)
print(list)