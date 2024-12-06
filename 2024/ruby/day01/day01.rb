file = File.read "input.txt"

firstList = []
secondList = []

rows = file
  .split("\n")
  .map { |row| row.split("   ")}
  .each { |row| 
    firstList << row[0].to_i
    secondList << row[1].to_i
  }

firstList = firstList.sort
secondList = secondList.sort

diff = [*0...firstList.length].reduce(0) { |sum, num| sum + (firstList[num] - secondList[num]).abs}

puts diff

