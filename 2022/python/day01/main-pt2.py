inputFile = open("day1.txt", "r")
calories = inputFile.readlines()

highest = 0
top2 = 0
top3 = 0

totalElf = 0
for calory in calories:
    if calory == "\n":
        if totalElf < top3:
            totalElf = 0
            continue

        if totalElf > highest:
            top3 = top2
            top2 = highest
            highest = totalElf
        else:
            if totalElf > top2:
                top3 = top2
                top2 = totalElf
            else:
                top3 = totalElf
        totalElf = 0
        continue

    totalElf += int(calory)

print(highest+top2+top3)
