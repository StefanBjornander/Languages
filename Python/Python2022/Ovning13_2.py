class Position:
    def __init__(self, latitud_vaderstreck, latitud_timme, latitud_minut, latitud_secund, \
                       longitud_vaderstreck, longitud_timme, longitud_minut, longitud_secund):
        self.latitud_vaderstreck = latitud_vaderstreck
        self.latitud_timme = latitud_timme
        self.latitud_minut = latitud_minut
        self.latitud_secund = latitud_secund
        self.longitud_vaderstreck = longitud_vaderstreck
        self.longitud_timme = longitud_timme
        self.longitud_minut = longitud_minut
        self.longitud_secund = longitud_secund

    def __str__(self):
        return f'latitud {self.latitud_timme}, {self.latitud_timme}, ' \
                       f'{self.latitud_timme} {self.latitud_vaderstreck}, ' \
               f'longitud {self.longitud_timme}, {self.longitud_timme}, ' \
                        f'{self.longitud_timme} {self.longitud_vaderstreck}'
               
g = Position('N', 57, 39, 47, 'O', 12, 16, 58)
print(g)
s = Position('N', 55, 53, 17, 'O', 17, 1, 21)
print(s)

"""
class Position:
    def __init__(self, latitud_vaderstreck, latitud_timme, latitud_minut, latitud_secund, \
                       longitud_vaderstreck, longitud_timme, longitud_minut, longitud_secund):
        self.latitud_vaderstreck = latitud_vaderstreck
        self.latitud_timme = latitud_timme
        self.latitud_minut = latitud_minut
        self.latitud_secund = latitud_secund
        self.longitud_vaderstreck = longitud_vaderstreck
        self.longitud_timme = longitud_timme
        self.longitud_minut = longitud_minut
        self.longitud_secund = longitud_secund

    def __str__(self):
        return f'latitud {self.latitud_timme}, {self.latitud_timme}, ' \
                       f'{self.latitud_timme} {self.latitud_vaderstreck}, ' \
               f'longitud {self.longitud_timme}, {self.longitud_timme}, ' \
                        f'{self.longitud_timme} {self.longitud_vaderstreck}'
               
g = Position('N', 57, 39, 47, 'O', 12, 16, 58)
print(g)
s = Position('N', 55, 53, 17, 'O', 17, 1, 21)
print(s)
"""