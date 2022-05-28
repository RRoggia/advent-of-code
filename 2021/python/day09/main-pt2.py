inputFile = open("day9.txt", "r")
heightmap = inputFile.read().split( '\n' )

basinId = 0
basins = {}
lastWasHighest = True
for indexRow, row in enumerate(heightmap):
  for indexColumn, column in enumerate(row):
    if column == '9':
      if not lastWasHighest :
        lastWasHighest = True
        basinId += 1
      continue
    lastWasHighest = False

    currentIndex = str(indexRow) + str(indexColumn)

    basins[ currentIndex ] = basins.get( currentIndex, basinId)
    
    below = heightmap[ indexRow + 1  ][ indexColumn ] if indexRow < len(heightmap) -1 else '9'

    if below != '9':
      basins[ str( indexRow + 1 ) + str( indexColumn ) ] = basins[ currentIndex ]
    
    right = heightmap[ indexRow ][ indexColumn + 1 ] if indexColumn < len( row ) -1 else '9'
    if right != '9':
      rightIndex = str( indexRow ) + str( indexColumn + 1 )
      existingBasingId = basins.get( rightIndex, -1 )
      if existingBasingId < 0:
        basins[ rightIndex ] = basins[ currentIndex ]
      else:
        if existingBasingId != basins[ currentIndex ]:
          for i in basins:
            if basins[i] == existingBasingId:
              basins[i] = basins[ currentIndex ]
  break


basins2 = {}

for i in basins:
  basin = basins2.get( basins[i], [] )
  basin.append( i )
  basins2[basins[i]] = basin

# print( basins2[basins['03']])

highest = 0 
second = 0 
third = 0

for i in basins2:
  if len(basins2[i]) >= highest:
    third = second
    second = highest
    highest = len(basins2[i])
  elif len(basins2[i]) >= second:
    third = second
    second = len(basins2[i])
  elif len(basins2[i]) > third:
    third = len(basins2[i])

print( highest, second, third )
print( highest * second * third )
  