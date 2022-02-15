import math;
radius = int(input("Radius: "));
volym = 4 * radius * radius * radius * math.pi / 3;
area = 4 * radius * radius * math.pi;
print(f'Volym: {volym:.3f}, Area: {area:.3f}');
