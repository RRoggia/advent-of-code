inputFile = open("day15.txt", "r")
lines = inputFile.read().split( '\n' )

for i in range(len(lines)):
	print(lines[i])
	lines[i] = list(lines[i])

print( lines )