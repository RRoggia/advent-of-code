inputFile = open("day10.txt", "r")
chunks = inputFile.read().split( '\n' )

pointsTable = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

totals = []
for chunk in chunks:
    openings = []
    total = 0
    corrupted = False
    for letter in chunk:
        if letter in pairs:
            openings.append( letter )
            continue
        
        lastOpened = openings.pop()
        if letter != pairs[lastOpened]:
            corrupted = True
            break
    
    if not corrupted:
        for _ in range(0, len(openings)):
            total *= 5
            total += pointsTable[pairs[openings.pop()]]
        totals.append(total)

for i in range(0, len(totals)):

    minorIndex = i
    for j in range(i + 1, len(totals)):
        if totals[j] < totals[minorIndex]:
            minorIndex = j
    
    temp = totals[i]
    totals[i] = totals[minorIndex]
    totals[minorIndex] = temp

print( totals[int((len(totals) / 2 ))])
