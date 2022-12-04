inputFile = open("day4.txt", "r")
sectionsIDs = inputFile.readlines()

count = 0
for section in sectionsIDs:
    firstSection, secondSection = section.split(",")

    beginFirstSection, endFirstSection = firstSection.split("-")
    beginSecondSection, endSecondSection = secondSection.split("-")
    beginFirstSection = int(beginFirstSection)
    endFirstSection = int(endFirstSection)
    beginSecondSection = int(beginSecondSection)
    endSecondSection = int(endSecondSection)

    beginOuter = min(beginFirstSection, beginSecondSection)
    endOuter = max(endFirstSection, endSecondSection)

    if beginOuter == beginFirstSection and endOuter == endFirstSection or beginOuter == beginSecondSection and endOuter == endSecondSection:
        count += 1

print(count)
