inputFile = open("day2.txt", "r")
rounds = inputFile.readlines()

# x loses
# y draw
# z win

combinations = {
    "X": {
        "A": "C",
        "B": "A",
        "C": "B"
    },
    "Z": {
        "A": "B",
        "B": "C",
        "C": "A"
    }
}

outcomeValue = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

shapeValue = {
    "A": 1,  # rock
    "B": 2,  # paper
    "C": 3  # scissor
}

total = 0
for round in rounds:
    opponent, outcome = round.split()

    if outcome == "Y":
        total += (outcomeValue[outcome] + shapeValue[opponent])
    else:
        total += (outcomeValue[outcome] + shapeValue[combinations[outcome][opponent]])

print(total)
