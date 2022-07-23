import datetime
class Datum:
    def __init__(self):
        d = datetime.datetime.now().date()
        self.ar = d.year
        self.manad = d.month
        self.dag = d.day

    def __str__(self):
        return f'{self.ar:04}-{self.manad:02}-{self.dag:02}'

d = Datum()
print(d)
