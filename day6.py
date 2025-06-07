
original_lines = []
lines:list[list[str]] = []
total = 0

# move operations
inc = lambda x: x + 1
dec = lambda x: x - 1
nop = lambda x: x

directions = [
    [nop, dec], # north
    [inc, nop], # east
    [nop, inc], # south
    [dec, nop], # west
]

current_direction = None 
current_position:tuple 
visited = set()
finished = False

def get_position_of(elem):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == elem:
                return (x, y)
    return None


with open("input.txt") as file:
    all_lines = [line.rstrip() for line in file]
    for line in all_lines:
        char_line = list(line)
        original_lines.append(char_line)

def reset():
    global lines
    global current_direction
    global current_position
    global visited
    global finished
    lines = original_lines.copy()
    current_direction = directions[0] # start north
    current_position = get_position_of("^")
    visited = set()
    visited.add(current_position)
    finished = False

reset()

max_x = len(lines[0]) - 1
max_y = len(lines) - 1


def get_next_position() -> tuple:
    x = current_direction[0](current_position[0])
    y = current_direction[1](current_position[1])
    return (x, y)

def rotate():
    global current_direction
    idx = directions.index(current_direction)
    next_idx = idx + 1
    if next_idx >= len(directions):
        next_idx = 0
    current_direction = directions[next_idx]

def get_at(position:tuple) -> str | None:
    x = position[0]
    y = position[1]
    if x < 0 or y < 0:
        return None
    if y > max_y or x > max_x:
        return None
    return lines[y][x]


def print_board():
    for y in range(len(lines)):
        row = ""
        for x in range(len(lines[y])):
            if (x, y) == current_position:
                row += "!"
            else:
                row += lines[y][x]
        print(row)
    print()

def move():
    global finished
    global current_position
    pending_position = get_next_position()
    if get_at(pending_position) == "#":
        rotate()
        return
    if get_at(pending_position) == None:
        finished = True
        return
    current_position = pending_position
    visited.add(current_position)

while not finished:
    move()

total = len(visited)

print(f"part1: {total}")

total_loops = 0

# lol
def brute_force():
    global finished
    global total_loops
    total_positions = len(lines) * len(lines[0])
    position = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            position += 1
            print(f"{position} / {str(total_positions)}")
            reset()
            if get_at((x, y)) == "#":
                continue
            if get_at((x, y)) == "^":
                continue
            lines[y][x] = "#"
            moves = 0
            while not finished:
                move()
                moves += 1
                if moves > 10000:
                    total_loops += 1
                    finished = True

brute_force()

print("part 2: " + str(total_loops))

