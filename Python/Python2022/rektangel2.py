class Rektangel:
    def __init__(self, top, left, hojd, bredd):
        self.top = top
        self.left = left
        self.hojd = hojd
        self.bredd = bredd

    @property
    def hojd(self):
        return self._hojd

    @hojd.setter
    def hojd(self, h):
        self._hojd = h

    @property
    def bredd(self):
        return self._bredd

    @bredd.setter
    def bredd(self, b):
        self._bredd = b

    def area(self):
        return self.hojd * self.bredd        

    def omkrets(self):
        return 2 * (self.hojd + self.bredd)
