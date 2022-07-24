class Bok:
    def __init__(self, titel, forfattare, sidantal, pris):
        self.titel = titel
        self.forfattare = forfattare
        self.sidantal = sidantal
        self.pris = pris

    def __str__(self):
        return f'{self.forfattare}: {self.titel} ({self.sidantal} sidor) pris {self.pris:.2} kr'

a = Bok('Python från början', 'Jan Skansholm', 295, 519.00)
b = Bok('Heureka! Fysik 1', 'Rune Alphonse', 400, 504.00)

print(a)
print(b)



        