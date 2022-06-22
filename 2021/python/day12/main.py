inputFile = open("day12.txt", "r")
lines = inputFile.read().split( '\n' )

caves = {}
for line in lines:
    fromDestination, toDestination = line.split("-")
    if fromDestination not in caves:
        caves[fromDestination] = set()
    if toDestination not in caves:
        caves[toDestination] = set()
    
    caves[fromDestination].add(toDestination)
    caves[toDestination].add(fromDestination)

print(caves)