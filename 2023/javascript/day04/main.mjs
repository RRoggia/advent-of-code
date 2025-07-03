import { readFileSync } from 'node:fs'

const rows = String(readFileSync("./input.txt")).split("\n")
let total = 0
for (let row of rows) {
  let [winners, mine] = row.split(":")[1].split("|")
  console.log(winners, mine)
  winners = winners
    .split(" ")
    .filter(a => a !== "")
    .reduce((acc, n) => {
      acc[n] = true
      return acc
    }, {})

  mine = mine
    .split(" ")
    .filter(a => a !== "")

  const count = mine.reduce((count, n) => {
    if (winners[n]) {
      count++
    }
    return count
  }, 0)
  total += count > 0 ? Math.pow(2, count - 1) : 0
}

console.log(total)