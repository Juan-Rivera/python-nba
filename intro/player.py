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


if __name__ == "__main__":
    curry = Player("Steph Curry", "PG", 535, 1224, 285, 750)
    print(curry.pos)
    print(round(curry.fg_percent(), 3))
    print(curry.shooting_percent())
