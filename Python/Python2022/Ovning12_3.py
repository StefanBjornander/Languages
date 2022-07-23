import json

try:
    with open('varulager.txt', 'r') as f:
        map = json.load(f)
except:
    map = dict()

while True:
    text = input('Code: ')
    if text.strip() == '':
        break
    code = int(text)
    text = input('Text: ')
    antal = int(input('Antal: '))
    pris = float(input('Pris: '))
    map[code] = [text, antal, pris]

with open('varulager.txt', 'w') as f:
    json.dump(map, f)
