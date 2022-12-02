inputFile = open("day2.txt", "r")
rounds = inputFile.readlines()

winnerCombinations = ["AY", "BZ", "CX"]
loserCombinations = ["AZ", "BX", "CY"]

shapeValue = {
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3  # scissor
}

total = 0
for round in rounds:
    opponent, me = round.split()

    combination = opponent + me
    total += shapeValue[me]
    if combination in winnerCombinations:
        total += 6
        continue

    if combination in loserCombinations:
        continue

    total += 3

print(total)