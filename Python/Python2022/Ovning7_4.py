"""
while True:
    text = input('Tal: ')

    if text == '':
        break

    tal = int(text)
    primtal = True

    for k in range(2, tal):
        if tal % k == 0:
            primtal = False
            break

    print(f'Primtal: {primtal}')
"""

n = int(input('n: '))
for i in range(1, n):
    primtal = True
    for k in range(2, i):
        if i % k == 0:
            primtal = False
            break
    print(f'Primtal {i}: {primtal}')
