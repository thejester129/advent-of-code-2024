from functools import reduce

input = []

with open("input.txt") as file:
    all_lines = [line.rstrip() for line in file]
    for line in all_lines:
        answer = int(line.split(":")[0])
        str_operands = line.split(":")[1].split(" ")[1:]
        operands = list(map(int, str_operands))
        input.append((answer, operands))

class Node:
    def __init__(self, operator, operand, children = []):
        self.operator = operator
        self.operand = operand
        self.children = children

    def evaluate(self, acc):
        return self.operator(acc, self.operand)

def plus(x, y):
    return x + y

def multiply(x, y):
    return x * y

def combine(x, y):
    return int(str(x) + str(y))

def make_children(values) -> list[Node]:
    if len(values) == 0:
        return []
    return [
        Node(plus, values[0], make_children(values[1:])),
        Node(multiply, values[0], make_children(values[1:])),
        Node(combine, values[0], make_children(values[1:])), # part 2
    ]

def evaluate_tree(node:Node, acc:int, solutions:list[int]) -> int:
    acc = node.evaluate(acc)
    if len(node.children) == 0:
        solutions.append(acc) # finished
        return acc
    return reduce(lambda x, y: x + y, list(map(lambda c: evaluate_tree(c, acc, solutions), node.children)))

def can_make(answer, values) -> bool:
    start_node = Node(plus, values[0])
    start_node.children = make_children(values[1:])

    solutions = []
    evaluate_tree(start_node, 0, solutions)

    return answer in solutions

total = 0
for input_line in input:
    if can_make(input_line[0], input_line[1]):
        total = total + input_line[0]

print("part1: " + str(total))



    