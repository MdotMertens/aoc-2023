from functools import reduce

input = open("input.txt", "r")


def read_game_data_2(lines: list[str]):
    time = int(
        "".join([x for x in lines[0].rstrip().split(":")[1].split(" ") if x != ""])
    )
    record = int(
        "".join([x for x in lines[1].rstrip().split(":")[1].split(" ") if x != ""])
    )

    return time, record


def get_winning_strategies_2(time: int, record: int):
    win_strats = 0
    for index in range(time):
        if (time - index) * index > record:
            win_strats += 1
    return win_strats


def read_game_data(lines: list[str]):
    times = [int(x) for x in lines[0].rstrip().split(":")[1].split(" ") if x != ""]
    records = [int(x) for x in lines[1].rstrip().split(":")[1].split(" ") if x != ""]

    games = []
    for index, _ in enumerate(times):
        games.append((times[index], records[index]))
    return games


def get_winning_strategies(games: list[tuple[int, int]]):
    winning_strategies = []

    for game in games:
        win_strats = 0
        for index in range(game[0]):
            if (game[0] - index) * index > game[1]:
                win_strats += 1
        if win_strats != 0:
            winning_strategies.append(win_strats)
    return reduce(lambda x, y: x * y, winning_strategies)


input = input.readlines()
print(get_winning_strategies(read_game_data(input)))
print(get_winning_strategies_2(*read_game_data_2(input)))
