antal = int(input('Antal: '))

list = []
for i in range(1, antal + 1):
    tal = int(input(f'  Tal {i}: '))
    list.append(tal)
list.sort()

if len(list) % 2 == 1:
    median = list[len(list) // 2]
else:
    median = (list[len(list) // 2 - 1] + list[len(list) // 2]) / 2
print(f'Median: {median}')
