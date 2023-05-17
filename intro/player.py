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

    def twos_percent(self):
        return (self.fgm - self.threes_m) / (self.fga - self.threes_a)

    def shooting_percent(self):
        return {
            "overall": self.fg_percent(),
            "3P%": self.threes_percent(),
            "2P%": self.twos_percent(),
        }
