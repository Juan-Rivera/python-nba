class Player:
    def __init__(self, name, pos, fgm, fga):
        self.name = name
        self.pos = pos
        self.fgm = fgm
        self.fga = fga

    def fg_percent(self):
        return self.fgm / self.fga
