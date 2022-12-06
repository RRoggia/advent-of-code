import re

inputFile = open("day5.txt", "r")
lines = inputFile.read().split('\n')
crates = []
movements = []
for line in range(len(lines)):
    if lines[line] == "":
        movements = lines[line+1:]
        break
    crates.append(lines[line])

createsNumber = crates.pop()

cratesMap = {}

for i in range(int(createsNumber[-2])):
    position = 1 + i * 4
    cratesMap[i+1] = []
    for create in reversed(range(len(crates))):
        if crates[create][position] == " ":
            break

        cratesMap[i+1].append(crates[create][position])

movements = [re.findall("\d+", line) for line in movements]
for movement in movements:
    movement = [int(mov) for mov in movement]
    print(movement)

    cratesMap[movement[2]] = cratesMap[movement[2]] + cratesMap[movement[1]][len(cratesMap[movement[1]]) - movement[0]:]
    cratesMap[movement[1]] = cratesMap[movement[1]][:len(cratesMap[movement[1]]) - movement[0]]

response = ""
for k in cratesMap:
  response += cratesMap[k][-1]

print(response)