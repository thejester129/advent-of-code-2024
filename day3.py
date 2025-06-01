import re

input = ""
total = 0
should_mul = True

def get_mul_answer(mul):
    # mul(x,y)
    mul = mul[4:]
    spl = mul.split(",")
    x = int(spl[0])
    y = int(spl[1][:-1])
    return x * y

def get_next_mul():
    global input
    return re.search("mul\([0-9]+,[0-9]+\)", input)

def apply_next_token():
    mul = get_next_mul()
    global total
    total += get_mul_answer(mul.group())
    global input
    input = input[mul.end():]

def apply_next_token_2():
    global input
    global should_mul
    global total
    mul = get_next_mul()
    do = re.search("do\(\)", input)
    dont = re.search("don't\(\)", input)

    mul_start = mul.start() if mul else float('inf')
    do_start = do.start() if do else float('inf')
    dont_start = dont.start() if dont else float('inf')

    if do is not None and do_start < mul_start and do_start < dont_start:
        should_mul = True
        input = input[do.end():]
        return
    if dont is not None and dont_start < mul_start and dont_start < do_start:
        should_mul = False
        input = input[dont.end():]
        return
    if mul is not None and mul_start < do_start and mul_start < dont_start:
        if should_mul:
            total += get_mul_answer(mul.group())
        input = input[mul.end():]
        return

total = 0
with open("input.txt") as file:
    input = file.read().rstrip()

while get_next_mul() is not None:
    apply_next_token()

print("part1: " + str(total))

total = 0
with open("input.txt") as file:
    input = file.read().rstrip()

while get_next_mul() is not None:
    apply_next_token_2()

print("part2: " + str(total))