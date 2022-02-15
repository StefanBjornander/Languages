import math;
x1 = float(input("x1: "));
y1 = float(input("y1: "));
x2 = float(input("x2: "));
y2 = float(input("y2: "));
xDelta = x1 - x2;
yDelta = y1 - y2;
distance = math.sqrt(xDelta * xDelta + yDelta * yDelta)
print(f'Distance: {distance:.3f}');
