antal = int(input('Antal: '))
a = []
for i in range(1, antal + 1):
    tal = int(input(f'Tal {i}: '))
    a.append(tal)

b = list(filter(lambda n : n % 2 == 0, a))
print(b);
