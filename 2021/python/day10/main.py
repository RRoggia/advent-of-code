inputFile = open("day10.txt", "r")
chunks = inputFile.read().split( '\n' )

pointsTable = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

openings = []
total = 0
for chunk in chunks:
    for letter in chunk:
        if letter in pairs:
            openings.append( letter )
            continue
        
        lastOpened = openings.pop()
        if letter != pairs[lastOpened]:
            total += pointsTable[ letter ]
            break
        

print( total )
