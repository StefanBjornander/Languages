class Djur:
    def __init__(self, late):
        self.__late = late

    def late(self):
        return self.__late;
    
class Daggdjur(Djur):
    def __init__(self, late):
        super().__init__(late)

class Kraldjur(Djur):
    def __init__(self, late):
        super().__init__(late)

class Fagel(Djur):
    def __init__(self, late):
        super().__init__(late)

l = [Daggdjur('A'), Kraldjur('B'), Fagel('C')]
for x in l:
    print(x.late())


