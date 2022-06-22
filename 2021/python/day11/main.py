inputFile = open("day11.txt", "r")
lines = inputFile.read().split( '\n' )
for idx, line in enumerate(lines):
    lines[idx] = list(map(lambda f: int(f), list(line)))

totalFlashes = 0

def increaseByOne():
    for line in lines:
        for cIdx, column in enumerate(line):
            line[cIdx] = column + 1

def flashToAdjacent(lines, rIdx, cIdx):
    # upper
    if rIdx > 0:
        if lines[rIdx - 1][cIdx] != 'F':
            lines[rIdx - 1][cIdx] = lines[rIdx - 1][cIdx] + 1
        
        ## upperleft
        if cIdx > 0:
            if lines[rIdx - 1][cIdx - 1] != 'F':
                lines[rIdx - 1][cIdx - 1] = lines[rIdx - 1][cIdx -1 ] + 1
        
        ## upperright
        if cIdx < len(line) -1:
            if lines[rIdx - 1][cIdx + 1] != 'F':
                lines[rIdx - 1][cIdx + 1] = lines[rIdx - 1][cIdx + 1 ] + 1

    ## left
    if cIdx > 0:
        if lines[rIdx][cIdx - 1] != 'F':
            lines[rIdx][cIdx - 1] = lines[rIdx][cIdx -1 ] + 1
        
    ## right
    if cIdx < len(line) -1:
        if lines[rIdx][cIdx + 1] != 'F':
            lines[rIdx][cIdx + 1] = lines[rIdx][cIdx + 1 ] + 1

    # lower
    if rIdx < len(lines) -1:
        if lines[rIdx + 1][cIdx] != 'F':
            lines[rIdx + 1][cIdx] = lines[rIdx + 1][cIdx] + 1
        
        ## lowerleft
        if cIdx > 0:
            if lines[rIdx + 1][cIdx - 1] != 'F':
                lines[rIdx + 1][cIdx - 1] = lines[rIdx + 1][cIdx -1 ] + 1
        
        ## lowerright
        if cIdx < len(line) -1:
            if lines[rIdx + 1][cIdx + 1] != 'F':
                lines[rIdx + 1][cIdx + 1] = lines[rIdx + 1][cIdx + 1 ] + 1

def flash():
    flashes = 0 
    while(len(list(filter(lambda c: list(filter(lambda f: f!= 'F' and f > 9, c)), lines))) > 0):
        for rIdx, line in enumerate(lines):
            for cIdx, column in enumerate(line):
                if column == 'F' or column <= 9:
                    continue
                
                flashes+=1
                line[cIdx] = 'F'
                flashToAdjacent(lines, rIdx, cIdx)
    return flashes

def resetFlashed():
    for line in lines:
        for cIdx, column in enumerate(line):
            if column == 'F':
                line[cIdx] = 0

for step in range(100):
    increaseByOne()
    totalFlashes += flash()
    resetFlashed()

print( totalFlashes )