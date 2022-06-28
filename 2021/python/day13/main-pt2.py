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
        if x not in grid:
            grid[x] = set()        
        
        grid[x].add(y)   
    return grid, foldInstructions

grid, foldInstructions = parseInput( lines )

print( foldInstructions)
for fold in foldInstructions:

    times = int(fold[1])
    last = (times * 2 )
    for i in range(times):
        key = str(i)
        lastKey = str(last - i)

        if fold[0] == "x":
            if key not in grid and lastKey not in grid:
                continue
            elif key not in grid:
                grid[key] = set()
            elif lastKey not in grid: 
                grid[lastKey] = set()

            grid[key] = grid[key].union(grid[lastKey])


print (total)
