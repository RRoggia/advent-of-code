inputFile = open("day9.txt", "r")
heightmap = inputFile.read().split( '\n' )

risk = 0
for indexRow, row in enumerate(heightmap):
  for indexColumn, column in enumerate(row):
    above = heightmap[ indexRow - 1  ][ indexColumn ] if indexRow > 0 else 9
    below = heightmap[ indexRow + 1  ][ indexColumn ] if indexRow < len(heightmap) -1 else 9
    left = heightmap[ indexRow ][ indexColumn - 1 ] if indexColumn > 0 else 9
    right = heightmap[ indexRow ][ indexColumn + 1 ] if indexColumn < len( row ) -1 else 9

    lower = min( int(above), int(below), int(left), int(right))
    if int(column) < lower:
      risk += (int(column) + 1)

print( risk)