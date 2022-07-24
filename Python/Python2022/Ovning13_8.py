from math import pi

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

class Figur:
    def __init__(self, startpunkt):
        self._startpunkt = startpunkt

class Cirkel(Figur):
    def __init__(self, startpunkt, radie):
        super().__init__(startpunkt)
        self.__radie = radie

    def area(self):
        return self.__radie ** 2 * pi
        
    def __str__(self):
        return f'Cirkel {str(self._startpunkt)}, radie {self.__radie}'

class Triangel(Figur):
    def __init__(self, startpunkt, hojd, bredd):
        super().__init__(startpunkt)
        self.__hojd = hojd
        self.__bredd = bredd

    def area(self):
        return self.__hojd * self.__bredd / 2

    def __str__(self):
        return f'Triangel {str(self._startpunkt)}, hojd {self.__hojd}, bredd {self.__bredd}'

class Rektangel(Figur):
    def __init__(self, startpunkt, hojd, bredd):
        super().__init__(startpunkt)
        self.__hojd = hojd
        self.__bredd = bredd

    def area(self):
        return self.__hojd * self.__bredd

    def __str__(self):
        return f'Rektangel {str(self._startpunkt)}, hojd {self.__hojd}, bredd {self.__bredd}'

c = Cirkel(Punkt(1, 2), 3)
print(c)
print(f'area {c.area():.3f}')
print()

t = Triangel(Punkt(3, 4), 5, 6)
print(t)
print(f'area {t.area():.3f}')
print()

r = Rektangel(Punkt(7, 8), 9, 10)
print(r)
print(f'area {r.area():.3f}')
