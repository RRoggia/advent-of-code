def extractPairInsertion( list ):
	pairInsertion = {}
	for line in lines:
		r = line.split(" -> ")
		key = r[0]
		value = r[1]

		pairInsertion[key] = value
	return pairInsertion

def replaceInsertionPairInPolymerTemplate( polymerTemplate, pairInsertion):
	output = polymerTemplate[0]

	for i in range(len(polymerTemplate) - 1):
		key = polymerTemplate[i] + polymerTemplate[i +1]

		output += pairInsertion[key]
		output += polymerTemplate[i+1]
	
	return output

inputFile = open("day14.txt", "r")
lines = inputFile.read().split( '\n' )

polymerTemplate = lines.pop(0)
lines.pop(0) # empty line

pairInsertion = extractPairInsertion( lines )

steps = 10
for step in range(steps):
	polymerTemplate = replaceInsertionPairInPolymerTemplate( polymerTemplate, pairInsertion )

occurences = {}
for letter in polymerTemplate:
	times = occurences.get(letter, 0)
	occurences[letter] = times + 1

print(occurences)
times = list(occurences.values())
print(max(times)-min(times))