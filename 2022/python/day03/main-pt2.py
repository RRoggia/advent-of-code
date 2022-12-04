inputFile = open("day3.txt", "r")
rucksacks = inputFile.readlines()

letters = "abcdefghijklmnopqrstuvwxyz"
priority = {}
for i in range(len(letters)):
    priority[letters[i]] = i + 1
    priority[letters[i].upper()] = i + 27

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
