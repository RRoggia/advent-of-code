import { readFileSync } from 'node:fs'

const rows = String(readFileSync("./input.txt")).split("\n")

const findLeft = (i, arr) => {
  let ascendent = []
  while (i >= 0 && !isNaN(arr[i])) {
    ascendent.push(arr[i])
    i--
  }
  return ascendent.reverse().join("")
}

const findRight = (i, arr) => {
  let ascendent = ""
  while (i < arr.length && !isNaN(arr[i])) {
    ascendent += arr[i]
    i++
  }
  return ascendent
}

const findNumbers = (i, arr) => {
  const nums = []
  const left = findLeft(i - 1, arr)
  const right = findRight(i + 1, arr)

  if (isNaN(arr[i])) {
    nums.push(left, right)
  } else {
    nums.push(left + arr[i] + right)
  }
  return nums
    .filter(n => "" !== n)
    .map(n => Number(n))
}

let nums = []
for (let i = 0; i < rows.length; i++) {
  const row = rows[i]
  const isFirstRow = i === 0
  const isLastRow = i + 1 === rows.length

  for (let j = 0; j < row.length; j++) {
    if (!isNaN(row[j]) || "." === row[j]) {
      continue
    }

    if (!isFirstRow) {
      nums.push(...findNumbers(j, rows[i - 1]))
    }

    nums.push(...findNumbers(j, row))

    if (!isLastRow) {
      nums.push(...findNumbers(j, rows[i + 1]))
    }
  }
}
console.log(nums.reduce((acc, a ) => acc + a, 0))