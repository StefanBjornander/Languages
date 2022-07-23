min = 0
max = 0

while True:
    tal = float(input('Tal: '))

    if tal == 0:
        continue

    if tal < 0:
        break

    if min == 0 or tal < min:
        min = tal

    if tal > max:
        max = tal

print('min:', min)
print('max:', max)
