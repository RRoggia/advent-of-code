inputFile = open("day13.txt", "r")
lines = inputFile.read().split( '\n' )

def parseInput( lines ):
    grid = {}
    firstFoldInstruction = ""
    for line in lines:
        if line == "" : 
            continue
        if line.startswith("fold"):
            firstFoldInstruction = line
            break
        
        x, y  = line.split(",")
        if x not in grid:
            grid[x] = set()        
        
        grid[x].add(y)   
    return grid, firstFoldInstruction.split( " " )[2].split("=")

grid, fold = parseInput( lines )

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

total = 0
for x in grid:
    if int(x) >= times:
        continue
    total += len(grid[x])

print (total)


# if y i j = y*2 -1, fold (y *2 -1) - i

