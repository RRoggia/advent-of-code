import math 
inputFile = open("day6.txt", "r")
lantern_fishes = inputFile.read()
lantern_fishes = lantern_fishes.split( ',' )
lantern_fishes = list(map( lambda f: int(f), lantern_fishes))

for day in range( 0, 80 ):
  willHaveBabies = list( filter( lambda f: f == 0, lantern_fishes ) )
  newDayFishes = list( map( lambda f: 6 if f == 0 else f - 1 , lantern_fishes ) )
  newborns = list(map( lambda f: 8, willHaveBabies ) )
  lantern_fishes = newDayFishes + newborns

print( len( lantern_fishes ) )
  