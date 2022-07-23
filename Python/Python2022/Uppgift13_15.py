class Hus:
    def __init__(self, l, b):
        self.langd = l
        self.bredd = b

    @property
    def langd(self):
        return self._langd

    @langd.setter
    def langd(self, l):
        self._langd = l

    @property
    def bredd(self):
        return self._bredd

    @bredd.setter
    def bredd(self, b):
        self._bredd = b

    def kvadratiskt(self):
        return self.langd * self.bredd

    def yta(self):
        return self.langd * self.bredd
    
    def __str__(self):
        return "Hus (" + str(self.langd) + "," + str(self.bredd) + ")"

class Flervaningshus(Hus):
    def __init__(self, l, b, v):
        super().__init__(l, b)
        self.antal_vaningar = v

    def hoghos(self):
        return self.antal_vaningar >= 10

    def yta(self):
        return self.langd * self.bredd * self.antal_vaningar

    def __str__(self):
        return "Flervaningshus (" + str(self.langd) + "," + str(self.bredd) + "," + str(self.antal_vaningar) + ")"

class Skola(Flervaningshus):
    def __init__(self, l, b, v, a):
        super().__init__(l, b, v)
        self.antal_klassrum = a

    def set_antalklassrum(self, a):
        self.antal_klassrum = a

    def medel(self):
        return self.antal_klassrum / self.antal_vaningar

    def yta(self):
        return self.antal_klassrum * 50

    def __str__(self):
        return "Skola (" + str(self.langd) + "," + str(self.bredd) + "," + \
                           str(self.antal_vaningar) + "," + str(self.antal_klassrum) + ")"

h = Hus(10, 20)
print(h)

f = Flervaningshus(11, 22, 5)
print(f)

s = Skola(12, 24, 6, 60)
print(s)

f.bredd = 15
s.bredd = 15

#f.set_antalklassrum(100)
s.set_antalklassrum(100)

#print(f.antal_klassrum)
print(s.antal_klassrum)

#print(f.medel())
print(s.medel())

print(f.yta())
print(s.yta())

l = [h, f, s]
for h in l:
    print(h.yta())