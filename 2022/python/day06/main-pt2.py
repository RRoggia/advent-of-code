inputFile = open("day6.txt", "r")
lines = inputFile.read().split('\n')

total = 0
for letterInd in range(len(list(lines[0]))):
    words = set()
    for i in range(letterInd, letterInd+14):
      words.add(lines[0][i])

    if len(words) == 14:
        total += 14
        break
    else:
        total += 1

print(total)
