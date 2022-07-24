class C:
    _total_antal = 0

    @classmethod
    def __init__(self, varde):
        self._total_antal += 1
        self.__varde = varde

    @classmethod
    def get_total_antal(cls):
        return cls._total_antal

    @classmethod
    def __str__(self):
        return f'{self.__varde} {self._total_antal}'

a = C(1)
b = C(2)
c = C(3)
print(a)
print(b)
print(c)
print(C.get_total_antal())



