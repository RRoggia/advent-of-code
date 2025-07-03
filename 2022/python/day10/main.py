inputFile = open("day10.txt", "r")
lines = inputFile.read().split('\n')

interestedCycle = 20
cycle = 0
values = [1]
totalSum =0
for line in lines:
    word = line.split(" ")
    if word[0] == "noop":
        cycle+=1

        if cycle== interestedCycle:
            value = sum([int(i) for i in values])
            totalSum += value * interestedCycle
            interestedCycle+=40
    else:
        values.append(word[1])
        cycle+=2
        if cycle == interestedCycle or cycle -1 == interestedCycle or cycle -2 == interestedCycle:
            value= sum([int(i) for i in values], -(int(word[1])))
            totalSum +=  value* interestedCycle
            interestedCycle+=40
    if interestedCycle == 260:
        break
        


print(totalSum)

