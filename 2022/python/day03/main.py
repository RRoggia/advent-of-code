inputFile = open("day3.txt", "r")
rucksacks = inputFile.readlines()

letters = "abcdefghijklmnopqrstuvwxyz"
priority = {}
for i in range(len(letters)):
  priority[letters[i]] = i +1
  priority[letters[i].upper()] = i + 27

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