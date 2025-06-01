lines = []
total = 0

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

max_x = len(lines[0]) - 1
max_y = len(lines) - 1

def get_at(x, y):
    if x < 0 or y < 0:
        return None
    if y > max_y or x > max_x:
        return None
    return lines[y][x]

def try_direction(x, y, x_fn, y_fn, acc, number) -> list[str]:
    if number == 0:
        return acc
    x = x_fn(x)
    y = y_fn(y)
    next = get_at(x, y)
    result = acc
    result.append(next)
    a = try_direction(x, y, x_fn, y_fn, result, number - 1)
    return a

# move operations
inc = lambda x: x + 1
dec = lambda x: x - 1
nop = lambda x: x

all_permutations = [
    [nop, dec], # north
    [inc, dec],
    [inc, nop], # east
    [inc, inc], 
    [nop, inc], # south
    [dec, inc], 
    [dec, nop], # west
    [dec, dec], 
]

cross_permutations = [
    [inc, dec],
    [inc, inc], 
    [dec, inc], 
    [dec, dec], 
]

def try_xmas(x, y):
    global total
    match = ["M", "A", "S"]

    for perm in all_permutations:
        res = try_direction(x, y, perm[0], perm[1], [], 3)
        if res == match:
            total += 1
    return

for x in range(max_x + 1):
    for y in range(max_y + 1):
        if get_at(x, y) == "X":
            try_xmas(x, y)

print("part 1: " + str(total))

a_locations = []
total_mas = 0

def find_mas(x, y):
    global total_mas
    match = ["A", "S"]

    for perm in cross_permutations:
        res = try_direction(x, y, perm[0], perm[1], [], 2)
        if res == match:
            a_location = perm[0](x), perm[1](y)
            if a_location in a_locations:
                a_locations.remove(a_location)
                total_mas += 1
            else:
                a_locations.append(a_location)
            
    return
   
for x in range(max_x + 1):
    for y in range(max_y + 1):
        if get_at(x, y) == "M":
            find_mas(x, y)

print("part 2: " + str(total_mas))