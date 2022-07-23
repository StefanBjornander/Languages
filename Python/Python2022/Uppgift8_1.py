import math

def omkrets(r):
    return 2 * r * math.pi

def area(r):
    return r ** 2 * math.pi

radie = float(input('Cirkelns radie: '))
print(f'Omkrets: {omkrets(radie):.3f}')
print(f'Area: {area(radie):.3f}')
