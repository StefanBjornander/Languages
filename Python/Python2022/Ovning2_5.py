import math

x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

delta_x = x2 - x1
delta_y = y2 - y1
distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
print(f'Distance: {distance:.3f}')
