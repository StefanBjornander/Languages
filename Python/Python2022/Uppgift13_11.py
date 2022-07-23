from math import pi

class Cirkel:
    def __init__(self, x, y, radie):
        self.x = x
        self.y = y
        self.radie = radie

    def area(self):
        return self.radie ** 2 * math.pi

    def omkrets(self):
        return 2 * self.radie * math.pi

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.radie == other.radie

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.radie < other.radie

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return self > other or self == other

c1 = Cirkel(1, 2, 3)
print(c1 == c1)
print(c1 != c1)
print(c1 < c1)
print(c1 <= c1)
print(c1 > c1)
print(c1 >= c1)
print()

c2 = Cirkel(1, 2, 4)
print(c1 == c2)
print(c1 != c2)
print(c1 < c2)
print(c1 <= c2)
print(c1 > c2)
print(c1 >= c2)
