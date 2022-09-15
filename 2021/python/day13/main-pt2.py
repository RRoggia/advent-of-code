inputFile = open("day13.txt", "r")
lines = inputFile.read().split( '\n' )

def parseInput( lines ):
    grid = {}
    foldInstructions = []
    for line in lines:
        if line == "" : 
            continue
        if line.startswith("fold"):
            foldInstructions.append( line.split( " " )[2].split("=") )
            continue
        
        x, y  = line.split(",")
        if y not in grid:
            grid[y] = set()        
        
        grid[y].add(x)   
    return grid, foldInstructions

def invertGridAxis( grid ):
    inverted = {}
    for x in grid:
        for y in grid[x]:
            if y not in inverted:
                inverted[y] = set()
            inverted[y].add(x)
    return inverted

grid, foldInstructions = parseInput( lines )

lastFold = 'y'
for fold in foldInstructions:
    position = int(fold[1])
    lastPosition = (position * 2 )

    if lastFold != fold[0]:
        grid = invertGridAxis(grid)

    for i in range(position):
        key = str(i)
        lastKey = str(lastPosition - i)

        if lastKey not in grid or key not in grid and lastKey not in grid:
            continue
        elif key not in grid:
            grid[key] = set()

        grid[key] = grid[key].union(grid.pop(lastKey))

    lastFold = fold[0]

for j in range(6):
    values = grid.get(str(j), {})
    row = ''
    for k in range(40):
        if str(k) in values:
            row += '#'
        else:
            row +=" "
    
    print(row)
