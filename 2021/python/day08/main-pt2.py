inputFile = open("day8.txt", "r")
segments = inputFile.read().split( '\n' )

def stringToDigitalClockNumber( string, letters_to_index ):
  key = list('0000000')

  for i in string:
    key[letters_to_index[i]] = '1'

  digitalClock = {
    '1110111': '0',
    '0010010': '1',
    '1011101': '2',
    '1011011': '3',
    '0111010': '4',
    '1101011': '5',
    '1101111': '6',
    '1010010': '7',
    '1111111': '8',
    '1111011': '9'
  }
  return digitalClock[ "".join(key) ]

total = 0 
for segment in segments:
  [ uniqueValues, outputValues ] = segment.split( '|' )
  uniqueValues = uniqueValues.split()
  outputValues = outputValues.split()

  # Considering the original position, you can figure out b, e and f 
  # to render the 10 digits you will require the sum of the following digits
  # a:8
  # b:6
  # c:8
  # d:7
  # e:4
  # f:9
  # g:7
  # Also consider the length to render
  # digits = {
  #   0: 6,
  #   1: 2, #unique
  #   2: 5,
  #   3: 5,
  #   4: 4, #unique
  #   5: 5,
  #   6: 6,
  #   7: 3, #unique
  #   8: 7, #unique
  #   9: 6
  # }

  total_letters = {}
  for value in uniqueValues:
    for letter in value:
      total_letters[letter] = total_letters.get(letter, 0 )+ 1

  # finds 1, 4 and 5th position
  letters_to_index = {}
  for a in total_letters :
    if total_letters[ a ] == 6:
      letters_to_index[ a ] = 1

    if total_letters[ a ] == 4:
      letters_to_index[ a ] = 4

    if total_letters[ a ] == 9:
      letters_to_index[ a ] = 5
  
  # the 2nd position is the missing digit to render one
  one = list(filter( lambda u: len(u) == 2 , uniqueValues ) )[0]
  for letter in one:
    if letters_to_index.get( letter, -1 ) < 0:
      letters_to_index[ letter ] = 2

  # the 0 position is the only digit that is not contained in one
  seven = list(filter( lambda u: len(u) == 3 , uniqueValues ) )[0]
  for letter in seven:
    if letter not in list(one):
      letters_to_index[ letter ] = 0
      break

  # the 3rd position we can get from the four
  four = list(filter( lambda u: len(u) == 4 , uniqueValues ) )[0]
  for letter in four:
    if letters_to_index.get( letter, -1 ) < 0:
      letters_to_index[ letter ] = 3

  # the 6 position we can get from the eight
  eight = list(filter( lambda u: len(u) == 7 , uniqueValues ) )[0]
  for letter in eight:
    if letters_to_index.get( letter, -1 ) < 0:
      letters_to_index[ letter ] = 6

  finalOutput = ''
  for output in outputValues:
    finalOutput += stringToDigitalClockNumber( output, letters_to_index )
  
  total += int(finalOutput)

print( total )
