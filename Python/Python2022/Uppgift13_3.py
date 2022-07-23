class Bil:
    def __init__(self, regnr, fabrikat, arsmodell, tjanstetvikt, motoreffekt):
        self.regnr = regnr
        self.fabrikat = fabrikat
        self.arsmodell = arsmodell
        self.tjanstetvikt = tjanstetvikt
        self.motoreffekt = motoreffekt
        
bil1 = Bil('ABC123', 'Volvo', 2000, 1000, 2000)
print(bil1.regnr)
print(bil1.fabrikat)
print(bil1.arsmodell)
print(bil1.tjanstetvikt)
print(bil1.motoreffekt)
print()

bil2 = Bil('ABD124', 'Saab', 1990, 1100, 2200)
print(bil2.regnr)
print(bil2.fabrikat)
print(bil2.arsmodell)
print(bil2.tjanstetvikt)
print(bil2.motoreffekt)

