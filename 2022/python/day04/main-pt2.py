inputFile = open("day4.txt", "r")
sectionsIDs = inputFile.readlines()


# 5-7,7-9, 2-8,3-7, 6-6,4-6
# ....567..
# ......789

# .2345678.
# ..34567..

# .....6...
# ...456...

count = 0
for section in sectionsIDs:
    firstSection, secondSection = section.split(",")

    beginFirstSection, endFirstSection = firstSection.split("-")
    beginSecondSection, endSecondSection = secondSection.split("-")
    beginFirstSection = int(beginFirstSection)
    endFirstSection = int(endFirstSection)
    beginSecondSection = int(beginSecondSection)
    endSecondSection = int(endSecondSection)

    beginOverlap = max(beginFirstSection, beginSecondSection)
    endOverlap = min(endFirstSection, endSecondSection)
    
    if endOverlap>= beginOverlap:
        count+=1

print(count)
