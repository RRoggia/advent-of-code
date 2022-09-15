def extractPairInsertion( list ):
	pairInsertion = {}
	for line in lines:
		r = line.split(" -> ")
		key = r[0]
		value = r[1]

		pairInsertion[key] = key[0] + value + key[1]
	return pairInsertion

def replaceInsertionPairInPolymerTemplate( polymerTemplate, pairInsertion):
	if polymerTemplate in pairInsertion:
		return pairInsertion[ polymerTemplate ]
	
	size = len(polymerTemplate)
	output = ""
	if size == 3:
		firstTemplate = polymerTemplate[0:2]
		last = polymerTemplate[2]
		outputFirstTemplate = replaceInsertionPairInPolymerTemplate( firstTemplate, pairInsertion )

		output = outputFirstTemplate
		result = pairInsertion[outputFirstTemplate[-1] + last]
		output += result[1:]
	else:
		midIndex = int(size / 2)
		isOdd = size % 2 != 0
		mid = ""
		
		firstTemplate = polymerTemplate[:midIndex]

		if isOdd:
			mid = polymerTemplate[midIndex]
			midIndex += 1
		
		secondTemplate = polymerTemplate[midIndex:]	

		outputFirstTemplate = replaceInsertionPairInPolymerTemplate( firstTemplate, pairInsertion )
		outputSecondTemplate = replaceInsertionPairInPolymerTemplate( secondTemplate, pairInsertion )

		if isOdd:
			output = outputFirstTemplate
			result = pairInsertion[outputFirstTemplate[-1] + mid]
			output += result[1:]

			result = pairInsertion[mid + outputSecondTemplate[0]]
			output += result[1:2]
			output += outputSecondTemplate
		else:
			output = outputFirstTemplate
			result = pairInsertion[outputFirstTemplate[-1] + outputSecondTemplate[0]]
			output += result[1:2]
			output += outputSecondTemplate

	pairInsertion[polymerTemplate] = output
	return output

inputFile = open("day14.txt", "r")
lines = inputFile.read().split( '\n' )

polymerTemplate = lines.pop(0)
lines.pop(0) # empty line

pairInsertion = extractPairInsertion( lines )

# increase size n-1
steps = 10
for step in range(steps):
	polymerTemplate = replaceInsertionPairInPolymerTemplate( polymerTemplate, pairInsertion )

occurences = {}
for letter in polymerTemplate:
	times = occurences.get(letter, 0)
	occurences[letter] = times + 1

times = list(occurences.values())
print(max(times)-min(times))
