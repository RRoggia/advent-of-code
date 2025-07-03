import { readFileSync } from 'node:fs'

function toDict(acc, n) {
  acc[n] = true
  return acc
}

function sum(acc, a) {
  return acc + a
}

const rows = String(readFileSync("./input.txt")).split("\n")
const counts = []

for (let i = 0; i < rows.length; i++) {
  let [winners, mine] = rows[i].split(":")[1].split("|")

  winners = winners
    .split(" ")
    .filter(a => a !== "")
    .reduce(toDict, {})

  mine = mine
    .split(" ")
    .filter(a => a !== "")

  let count = mine
    .filter(m => winners[m])
    .reduce((count, _) => {
      return ++count
    }, 0)

  let cardId = i + 1
  counts[cardId] = !(cardId in counts) ? 1 : counts[cardId] + 1

  while (cardId < cardId + count) {
    counts[cardId + count] = !(cardId + count in counts) ? counts[cardId] : counts[cardId] + counts[cardId + count]
    count--;
  }
}
console.log(counts.reduce(sum, 0))


