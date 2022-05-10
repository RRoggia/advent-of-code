from functools import reduce

inputFile = open("day5.txt", "r")
lines = inputFile.read().split( '\n' )

size = 989
grid = {}

def increaseCountForCellsInLine( element1, element2, calculateIndex ):
  higher = max( element1, element2 )
  lower = min( element1, element2 )

  for a in range( lower, higher + 1):
    index = calculateIndex( a )
    grid[ index ] = grid.get( index, 0 ) + 1  

for line in lines:
  one = line.replace( ' -> ', ',' ).split(',')
  c1, r1, c2, r2 = map( lambda item: int(item) ,one )

  if r1 == r2:
    increaseCountForCellsInLine( c1, c2, lambda columnIndex: r1 * size + columnIndex ) 
    
  if c1 == c2:
    increaseCountForCellsInLine( r1, r2, lambda rowIndex: rowIndex * size + c1 )  

  
count = 0 
for value in grid.values():
  if value > 1:
    count +=1

print( count )
