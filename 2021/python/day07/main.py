inputFile = open("day7.txt", "r")
crab_positions = inputFile.read()
crab_positions = crab_positions.split( ',' )

lower_fuel = 999999999999
for (index, to_position) in enumerate( crab_positions ):
  temp_lower_fuel = 0
  for from_position in crab_positions:
    temp_lower_fuel += abs( int(to_position) - int(from_position) )
  
  if temp_lower_fuel < lower_fuel:
    lower_fuel = temp_lower_fuel

print(lower_fuel)
  