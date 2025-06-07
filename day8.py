lines = []

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

max_x = len(lines[0]) - 1
max_y = len(lines) - 1

def get_at(pos:tuple[int]) -> str:
    x = pos[0]
    y = pos[1]
    if x < 0 or y < 0:
        return None
    if y > max_y or x > max_x:
        return None
    return lines[y][x]

def find_all_locations(symbol) -> list[tuple[int]]:
    locations = []
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if(get_at((x, y)) == symbol):
                locations.append((x, y))
    return locations

def find_antinodes(pos:tuple[int]) -> list[tuple[int]]:
    antinodes = set()
    symbol = get_at(pos)
    other_positions = filter(lambda x: x != pos, find_all_locations(symbol))

    for other in other_positions:
        diffX = other[0] - pos[0]
        diffY = other[1] - pos[1]
        currentNegative = pos
        # part 2
        while get_at(currentNegative) != None:
            antinodes.add(currentNegative)
            currentNegative = (currentNegative[0] - diffX, currentNegative[1] - diffY)

        # part 2
        currentPositive = other
        while get_at(currentPositive) != None:
            antinodes.add(currentPositive)
            currentPositive = (currentPositive[0] + diffX, currentPositive[1] + diffY)

    return list(antinodes)


def check_locations() -> set[tuple[int]]:
    locations = set()
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if get_at((x, y)) != ".":
                matches = find_antinodes((x, y))
                for match in matches:
                    locations.add(match)
    return locations

locations = check_locations()

print("answer: " + str(len(locations)))

