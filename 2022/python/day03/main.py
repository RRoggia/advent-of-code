import string

inputFile = open("day3.txt", "r")
rucksacks = inputFile.readlines()

priority = {}
for i in range(len(string.ascii_lowercase)):
    priority[string.ascii_lowercase[i]] = i + 1
    priority[string.ascii_lowercase[i].upper()] = i + 27

total =0
for rucksack in rucksacks:
  half = int(len(rucksack) /2)
  firstCompartment= rucksack[:half]
  secondCompartment = rucksack[half:len(rucksack)]
  
  for item in firstCompartment:
    if item in secondCompartment:
      break
  
  total += priority[item]
  
print(total)