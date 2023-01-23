import string

inputFile = open("day3.txt", "r")
rucksacks = inputFile.readlines()

priority = {}
for i in range(len(string.ascii_lowercase)):
    priority[string.ascii_lowercase[i]] = i + 1
    priority[string.ascii_lowercase[i].upper()] = i + 27

total = 0
for groups in range(int(len(rucksacks) / 3)):
    firstCompartiment = rucksacks[groups*3]
    secondCompartiment = rucksacks[groups*3 + 1]
    thirdCompartiment = rucksacks[groups*3 + 2]
    
    for item in firstCompartiment:
      if item in secondCompartiment and item in thirdCompartiment:
        break

    total+= priority[item]

print(total)
