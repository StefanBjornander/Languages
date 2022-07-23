import json

try:
    with open('elever.txt', 'r') as f:
        map = json.load(f)
except:
    map = dict()

while True:
    namn = input('Name: ')

    if namn.strip() == '':
        break

    text = input('Poang: ')
    poang = [int(p) for p in text.split(' ')]
    map[namn] = poang

with open('elever.txt', 'w') as f:
    json.dump(map, f)

elev = input('Elev: ')
print(map[elev])