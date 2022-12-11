inputFile = open("day8.txt", "r")
lines = inputFile.read().split('\n')

visible = len(lines) *2 + (len(lines)-2)*2

for row in range(1, len(lines)-1):
  for column in range(1, len(lines[row])-1):
    result = []
    isVisible=True
    for upRow in range(0, row):
      if lines[upRow][column] >= lines[row][column]:
        isVisible=False
    result.append(isVisible)
    
    isVisible=True
    for downRow in range(row+1, len(lines)):
      if lines[downRow][column] >= lines[row][column]:
        isVisible=False
    result.append(isVisible)
    
    isVisible=True
    for leftColumn in range(0, column):
      if lines[row][leftColumn] >= lines[row][column]:
        isVisible=False
    result.append(isVisible)
 
    isVisible=True
    for rightColumn in range(column+1, len(lines[row])):
      if lines[row][rightColumn] >= lines[row][column]:
        isVisible=False
    result.append(isVisible)


    if True in result:
      visible+=1

print(visible)