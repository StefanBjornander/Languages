antal = int(input('Antal: '))

list = []
for i in range(1, antal + 1):
    tal = int(input(f'Tal {i}: '))
    list.append(tal)

count = 0;
for tal in list:
    if tal < 0:
        count += 1
print(f'{count} tal mindre an noll')