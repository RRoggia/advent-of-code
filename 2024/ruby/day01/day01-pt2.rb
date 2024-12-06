file = File.read "input.txt"
#file = File.read "test-input.txt"

firstColumn = []
secondColumn = {}

rows = file
  .split("\n")
  .map { |row| row.split("   ")}
  .each { |column| 
    firstColumn << column[0].to_i
    secondColumn[column[1].to_i] = secondColumn.key?(column[1].to_i) ? secondColumn[column[1].to_i] + 1  : 1 
  }

diff = firstColumn.reduce(0) { |sum, num| 
  sum + (!secondColumn.key?(num) ? 0 : num * secondColumn[num]) }

puts diff
