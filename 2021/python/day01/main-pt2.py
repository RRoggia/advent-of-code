inputFile = open("day1.txt", "r")
measurements = inputFile.read().split()

def calculateMeasurementsIncrements( measurements ):
  totalIncrements = 0
  sizeOfMeasurements = 3
  for index, measurement in enumerate( measurements ):
    
    if index + sizeOfMeasurements >= len( measurements ):
      break

    measureA = int( measurements[ index ] ) 
    measureB = int( measurements[ index + 3 ] )
    if measureA < measureB:
      totalIncrements += 1

  return totalIncrements

print( calculateMeasurementsIncrements( measurements ) )