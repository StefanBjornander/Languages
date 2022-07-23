class Person:
    def __init__(self, namn):
        self.namn = namn
    
class Bil:
    _skattesats = 0

    def __init__(self, regnr, fabrikat, arsmodell, tjanstetvikt, motoreffekt, agare):
        self.regnr = regnr
        self.fabrikat = fabrikat
        self.arsmodell = arsmodell
        self.tjanstetvikt = tjanstetvikt
        self.motoreffekt = motoreffekt
        self.agare = agare        

    def skatt(self):
        return self.tjanstetvikt * Bil._skattesats

    @classmethod
    def set_skattesats(cls, skattesats):
        cls._skattesats = skattesats

Bil.set_skattesats(4.0)

adam = Person("adam")
bil1 = Bil('ABC123', 'Volvo', 2000, 1000, 2000, adam)
print(bil1.regnr)
print(bil1.fabrikat)
print(bil1.arsmodell)
print(bil1.tjanstetvikt)
print(bil1.motoreffekt)
print(bil1.skatt())
print()

bertil = Person("bertil")
bil2 = Bil('ABD124', 'Saab', 1990, 1100, 2200, bertil)
print(bil2.regnr)
print(bil2.fabrikat)
print(bil2.arsmodell)
print(bil2.tjanstetvikt)
print(bil2.motoreffekt)
print(bil2.agare.namn)
print(bil2.skatt())
