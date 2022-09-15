def extractPairInsertion( lines ):
	pairInsertion = {}
	for line in lines:
		r = line.split(" -> ")
		key = r[0]
		value = r[1]

		pairInsertion[key] = value
	return pairInsertion

def processPolymerTemplate( polymerTemplate, steps, pairInsertion):
	for i in range(steps):
		newPolymerTemplate = {}
		for key in polymerTemplate:
			r = newPolymerTemplate.get( key[0] + pairInsertion[key], 0 )
			newPolymerTemplate[key[0] + pairInsertion[key]] = r + polymerTemplate[key]

			r = newPolymerTemplate.get( pairInsertion[key] + key[1], 0 )
			newPolymerTemplate[pairInsertion[key] + key[1]] = r + polymerTemplate[key]

		polymerTemplate = newPolymerTemplate

	return polymerTemplate

inputFile = open("day14.txt", "r")
lines = inputFile.read().split( '\n' )

polymerTemplate = lines.pop(0)
lines.pop(0) # empty line

pairInsertion = extractPairInsertion( lines )
steps = 40

polymerCount = {}
for i in range(len(polymerTemplate) - 1):
	key = polymerTemplate[i] + polymerTemplate[i+1]
	r = polymerCount.get(key, 0)
	polymerCount[key] = r + 1

initialPolymerCount = polymerCount
polymerCount = processPolymerTemplate( polymerCount, steps, pairInsertion)

occurrences = {}
for key in polymerCount:
	r = occurrences.get(key[0], 0)
	occurrences[key[0]] = r + polymerCount[key]

r = occurrences.get(polymerTemplate[-1], 0 )
occurrences[polymerTemplate[-1]] = r + 1

times = list(occurrences.values())
print(max(times)-min(times))