with open("day1.txt") as inputFile:
  calories = inputFile.readlines()

  highest = 0
  totalElf=0
  for calory in calories:
    if calory == "\n":
      if highest < totalElf:
        highest = totalElf
      totalElf = 0
      continue
      
    totalElf += int(calory)

  print( highest)
