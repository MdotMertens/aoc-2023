LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def update_map_with_minimal_values(amount, color, color_map):
    if amount > color_map.get(color, 0):
        color_map[color] = amount
    return color_map


def is_draw_valid(amount, color, limits):
    if amount > limits[color]:
        return False
    return True


def parse_game_1(line: str) -> int:
    game_data, draw_data = line.split(":")
    game_number = int(game_data.split(" ")[1])

    for draw in draw_data.split(";"):
        color_data = [info.strip() for info in draw.split(",")]
        for data in color_data:
            amount, color = data.split(" ")
            if not is_draw_valid(int(amount), color, LIMITS):
                return 0

    return game_number


def parse_game_2(line: str) -> int:
    _, draw_data = line.split(":")
    color_map = {}
    sum = 1

    for draw in draw_data.split(";"):
        color_data = [info.strip() for info in draw.split(",")]
        for data in color_data:
            amount, color = data.split(" ")
            color_map = update_map_with_minimal_values(int(amount), color, color_map)
    for amount in color_map.values():
        sum *= amount
    return sum


if __name__ == "__main__":
    input = open("input.txt")
    lines = input.readlines()
    sum_part_1 = 0
    sum_part_2 = 0

    for line in lines:
        sum_part_1 += parse_game_1(line)

    for line in lines:
        sum_part_2 += parse_game_2(line)

    print(sum_part_1)
    print(sum_part_2)
