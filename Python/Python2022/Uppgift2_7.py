import math

radie = float(input('Cirkelns radie: '))

#Berakna cirkelns omkrets
omkrets = 2 * radie * math.pi

# Berakna cirkelns area
area = radie ** 2 * math.pi

print(f'Omkrets: {omkrets:.3f}')
print(f'Area: {area:.3f}')
