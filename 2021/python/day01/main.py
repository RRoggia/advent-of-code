inputFile = open("day1.txt", "r")
measurements = inputFile.read().split()

def calculateMeasurementsIncrements( measurements ):
  totalIncrements = 0

  for index, measurement, in enumerate( measurements ):
    if index + 1 >= len( measurements ):
      break

    if int( measurement ) < int( measurements[ index + 1 ] ):
      totalIncrements = totalIncrements + 1

  return totalIncrements

print( calculateMeasurementsIncrements( measurements ) )
