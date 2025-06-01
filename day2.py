reports = []

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
            split = line.split(" ")
            int_split = list(map(int, split))
            reports.append(list(map(int, split)))

def is_asc(x, y):
    return x < y

def is_step_safe(curr, next, asc):
    diff = abs(curr - next)
    if diff < 1 or diff > 3:
        return False
    if asc != is_asc(curr, next):
        return False
    return True

def is_report_safe(report):
    asc = is_asc(report[0], report[1])
    for i in range(len(report) - 1):
        curr = report[i]
        next = report[i + 1]
        if (not is_step_safe(curr, next, asc)):
            return False
    return True
        

safe = list(filter(is_report_safe, reports))

print("part1: " + str(len(safe)))

safe_reports = 0

for report in reports:
    for i in range(len(report)):
        variation = report.copy()
        del variation[i]
        if is_report_safe(variation):
            safe_reports += 1
            break

print("part2: " + str(safe_reports))






