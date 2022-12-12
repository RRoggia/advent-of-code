from operator import mul
from functools import reduce
inputFile = open("day8.txt", "r")
lines = inputFile.read().split('\n')

visible = len(lines) *2 + (len(lines)-2)*2
total =0
highest=-1
for row in range(1, len(lines)-1):
  for column in range(1, len(lines[row])-1):
    results = []
    count=0
    for upRow in reversed(range(0, row)):
      count+=1
      if lines[upRow][column] >= lines[row][column]:
        break
    results.append(count)

    count=0
    for leftColumn in reversed(range(0, column)):
      count+=1
      if lines[row][leftColumn] >= lines[row][column]:
        break
    results.append(count)
    
    count=0
    for downRow in range(row+1, len(lines)):
      count+=1
      if lines[downRow][column] >= lines[row][column]:
        break
    results.append(count)
 
    count=0
    for rightColumn in range(column+1, len(lines[row])):
      count+=1
      if lines[row][rightColumn] >= lines[row][column]:
        break
    results.append(count)
    total = reduce( mul, results)
    if total > highest:
      highest=total


print(highest)