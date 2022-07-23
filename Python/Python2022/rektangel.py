class Rektangel:
    def __init__(self, top, left, hojd, bredd):
        self.top = top
        self.left = left
        self.hojd = hojd
        self.bredd = bredd

    def get_hojd(self):
        return self.hojd

    def set_hojd(self, hojd):
        self.hojd = hojd

    def get_bredd(self):
        return self.bredd

    def set_bredd(self, bredd):
        self.bredd = bredd

    def area(self):
        return self.hojd * self.bredd        

    def omkrets(self):
        return 2 * (self.hojd + self.bredd)
