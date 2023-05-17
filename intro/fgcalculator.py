# Official player stats for 2021

players = [
    {
        "name": "Jayson Tatum",
        "field goals": 708,
        "field goals attempted": 1564,
    },
    {
        "name": "Devin Booker",
        "field goals": 662,
        "field goals attempted": 1421,
    },
    {
        "name": "Stephen Curry",
        "field goals": 535,
        "field goals attempted": 1224,
    },
]


def calculate_fg_percent(player):
    name = player["name"]
    fg = player["field goals"]
    fga = player["field goals attempted"]
    shooting_percent = fg / fga
    return name + " has a shooting percentage of " + str(shooting_percent)


for player in players:
    print(calculate_fg_percent(player))
