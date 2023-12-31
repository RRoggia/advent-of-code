import { readFileSync } from 'node:fs'

const rows = String(readFileSync("./input.txt")).split("\n")

let total = 0
for (let i = 0; i < rows.length; i++) {
  const row = rows[i]
  const isFirstRow = i === 0
  const isLastRow = i + 1 === rows.length

  let value = ""
  let hasAdjacent = false
  for (let j = 0; j < row.length; j++) {
    const isFirstChar = j === 0
    const isLastChar = j + 1 === row.length
    let char = row[j]
    if (!isNaN(char)) {
      value += char
    } else {
      hasAdjacent = false
      value = ""
    }

    if (value.length === 0) {
      continue
    }

    if (!hasAdjacent) {
      if (value.length === 1) { //new number
        if (!isFirstChar) {
          const left = rows[i][j - 1]
          hasAdjacent = hasAdjacent || isNaN(left) && left !== "."
          if (!isFirstRow) {
            const upperLeft = rows[i - 1][j - 1]
            hasAdjacent = hasAdjacent || isNaN(upperLeft) && upperLeft !== "."
          }
          if (!isLastRow) {
            const lowerLeft = rows[i + 1][j - 1]
            hasAdjacent = hasAdjacent || isNaN(lowerLeft) && lowerLeft !== "."
          }
        }
      }

      if (!isFirstRow) {
        const upper = rows[i - 1][j]
        hasAdjacent = hasAdjacent || isNaN(upper) && upper !== "."
      }
      if (!isLastRow) {
        const lower = rows[i + 1][j]
        hasAdjacent = hasAdjacent || isNaN(lower) && lower !== "."
      }

      if (!isLastChar && isNaN(row[j + 1])) {
        const right = rows[i][j + 1]
        hasAdjacent = hasAdjacent || isNaN(right) && right !== "."
        if (!isFirstRow) {
          const upperRight = rows[i - 1][j + 1]
          hasAdjacent = hasAdjacent || isNaN(upperRight) && upperRight !== "."
        }
        if (!isLastRow) {
          const lowerRight = rows[i + 1][j + 1]
          hasAdjacent = hasAdjacent || isNaN(lowerRight) && lowerRight !== "."
        }
      }
    }
    // console.log(value, hasAdjacent)


    if (hasAdjacent && (j + 1 === row.length || isNaN(row[j + 1]))) {
      total += Number(value)
    }
  }

}
console.log(total)