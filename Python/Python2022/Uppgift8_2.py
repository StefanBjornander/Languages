import math

def omkrets_area(r):
    return (2 * r * math.pi, r ** 2 * math.pi)

radie = float(input('Cirkelns radie: '))
(o, a) = omkrets_area(radie)
print(f'Omkrets: {o:.3f}')
print(f'Area: {a:.3f}')
