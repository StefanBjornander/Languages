antal = int(input('Antal: '))

list = [2]
k = 3

for i in range(1, antal):
    list.append(k * list[len(list) - 1])

print(list)