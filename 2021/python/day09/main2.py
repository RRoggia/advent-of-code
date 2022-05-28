inputFile = open("day9.txt", "r")
heightmap = inputFile.read().split( '\n' )

risk = 0
for indexRow, row in enumerate(heightmap):
  word = ''
  for indexColumn, column in enumerate(row):
    word += column if column != '9' else ' '
  print(word)