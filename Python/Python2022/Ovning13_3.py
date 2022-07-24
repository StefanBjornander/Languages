import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def flytta_horisontell(self, delta_x):
        self.x += delta_x

    def flytta_vertikalt(self, delta_y):
        self.y += delta_y

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f'({self.x}, {self.y})'

p = Punkt(1, 1)
p.flytta_horisontell(2)
p.flytta_vertikalt(3)
print(p)
print(f'{p.distance():.3f}')
