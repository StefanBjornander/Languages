class Person:
    def __init__(self, namn):
        self.namn = namn
    
class Bil:
    def __init__(self, regnr, fabrikat, arsmodell, tjanstetvikt, motoreffekt, agare):
        self.regnr = regnr
        self.fabrikat = fabrikat
        self.arsmodell = arsmodell
        self.tjanstetvikt = tjanstetvikt
        self.motoreffekt = motoreffekt
        self.agare = agare
        
adam = Person("adam")
bil1 = Bil('ABC123', 'Volvo', 2000, 1000, 2000, adam)
print(bil1.regnr)
print(bil1.fabrikat)
print(bil1.arsmodell)
print(bil1.tjanstetvikt)
print(bil1.motoreffekt)
print(bil1.agare.namn)
print()

bertil = Person("bertil")
bil2 = Bil('ABD124', 'Saab', 1990, 1100, 2200, bertil)
print(bil2.regnr)
print(bil2.fabrikat)
print(bil2.arsmodell)
print(bil2.tjanstetvikt)
print(bil2.motoreffekt)
print(bil2.agare.namn)
