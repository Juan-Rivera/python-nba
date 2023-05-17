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


def get_shooting_percent(player):
    if type(player) is not dict:
        print("You need to pass in a dictionary!")
        return
    else:
        pass

    fg = player["field goals"]
    fga = player["field goals attempted"]

    if fg > fga:
        print("You can not have more shots made than shots attempted")
        return
    else:
        pass

    shooting_percent = fg / fga

    return shooting_percent


tatum = players[0]
tatum_shooting_percent = get_shooting_percent(tatum)
print(tatum_shooting_percent)
