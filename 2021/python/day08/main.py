inputFile = open("day8.txt", "r")
segments = inputFile.read().split( '\n' )

total = 0
for segment in segments:
  outputValues = segment.split( '|' )[1].split()
  for outputValue in outputValues:
    if len(outputValue) in [2, 3, 4, 7 ]:
      total += 1

print( total )


digits = {
  0: 6,
  1: 2, #unique
  2: 5,
  3: 5,
  4: 4, #unique
  5: 5,
  6: 6,
  7: 3, #unique
  8: 7, #unique
  9: 6
}
