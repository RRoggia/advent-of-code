inputFile = open("day6.txt", "r")
lines = inputFile.read().split('\n')

total=0
for letterInd in range(len(list(lines[0]))):
  
  words = set()
  words.add(lines[0][letterInd])
  words.add(lines[0][letterInd+1])
  words.add(lines[0][letterInd+2])
  words.add(lines[0][letterInd+3])
  
  if len(words) == 4:
    total+=4
    break
  else:
    total +=1
  
print(total)