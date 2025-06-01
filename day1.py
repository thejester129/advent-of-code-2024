list1 = []
list2 = []

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
            split = line.split("   ")
            list1.append(int(split[0]))
            list2.append(int(split[1]))

list1.sort()
list2.sort()

diff = 0

for i in range(len(list1)):
   diff += abs(list1[i] - list2[i])
    
print("part1: " + str(diff))

simularity = 0

for x in list1:
   matches = 0
   for y in list2:
      if x == y:
         matches += 1
   simularity += x * matches

print("part2: " + str(simularity))





