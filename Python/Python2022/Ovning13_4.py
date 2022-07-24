class Raknare:
    def __init__(self, min, max, varde):
        if min > max:
            raise ValueError(f'Limits {min} > {max}')
        self.__min = min
        self.__max = max
        self.__varde = varde

    def oka(self):
        if self.__varde == self.__max:
            raise ValueError(f'Overflow {self.__max}')
        self.__varde += 1

    def minska(self):
        if self.__varde == self.__min:
            raise ValueError(f'Underflow {self.__min}')
        self.__varde -= 1

    def __str__(self):
        return f'{self.__min} <= {self.__varde} <= {self.__max}'

try:
    r = Raknare(1, 10, 5)
    print(r)
    r.minska()
    print(r)
    r.oka()
    print(r)
except ValueError as message:
    print('Fel:', message)
