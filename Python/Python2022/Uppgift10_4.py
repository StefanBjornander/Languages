import math

def omkrets(r):
    if r > 0:
        return 2 * r * math.pi
    else:
        return None

def area(r):
    if r > 0:
        return r ** 2 * math.pi
    else:
        return None

r = float(input('Cirkelns radie: '))

o = omkrets(r)
if o != None:
    print(f'Omkrets: {omkrets(r):.3f}')
else:
    print(f'Omkrets: Felaktig radie')

a = area(r)
if a != None:
    print(f'Area: {area(r):.3f}')
else:
    print(f'Areas: Felaktig radie')
