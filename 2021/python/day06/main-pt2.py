import math 
inputFile = open("day6.txt", "r")
lantern_fishes = inputFile.read()
lantern_fishes = lantern_fishes.split( ',' )
lantern_fishes = list(map( lambda f: int(f), lantern_fishes))

ones  = list( filter( lambda f: f == 1, lantern_fishes ) )
twos = list( filter( lambda f: f == 2, lantern_fishes ) )
threes = list( filter( lambda f: f == 3, lantern_fishes ) )
fours = list( filter( lambda f: f == 4, lantern_fishes ) )
fives  = list( filter( lambda f: f == 5, lantern_fishes ) )

cycle = {}
cycle[ 1 ] = len( ones )
cycle[ 2 ] = len( twos )
cycle[ 3 ] = len( threes )
cycle[ 4 ] = len( fours )
cycle[ 5 ] = len( fives )

newborns = 0
for day in range( 1, 256 ):
  count = cycle.get( day, 0 )
  cycle[ day + 7 ] = cycle.get( day + 7, 0 ) + count
  cycle[ day + 9 ] = cycle.get( day + 10, 0 ) + count
  newborns += count

print( newborns + len( lantern_fishes ) )
