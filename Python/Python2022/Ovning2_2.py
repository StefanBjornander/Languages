import math

radie = float(input('Sfarens radie: '))
volym = 4 / 3 * math.pi * radie ** 3
area = 4 * math.pi * radie ** 2

print(f'Volym: {volym:.3f}')
print(f'Area: {area:.3f}')
