class Player:
    def __init__(self, name, pos, fgm, fga, threes_m, threes_a):
        self.name = name
        self.pos = pos
        self.fgm = fgm
        self.fga = fga
        self.threes_m = threes_m
        self.threes_a = threes_a

    def fg_percent(self):
        return self.fgm / self.fga

    def threes_percent(self):
        return self.threes_m / self.threes_a
