import { readFileSync } from "node:fs"

const file = readFileSync("./input.txt")
const games = String(file).split("\n")

const values = {
  "red": 12,
  "green": 13,
  "blue": 14
}

let total = 0
for (let game of games) {
  const [id, played] = game.split(": ")
  const gameId = id.split(" ")[1]
  const cubes = played.split(new RegExp("[;,]")).map(e => e.trim())
  
  let isValid = true
  for (let cube of cubes) {
    const [amount, color] = cube.split(" ")
    if (values[color] < Number(amount)) {
      isValid = false
      break
    }
  }

  if (isValid) {
    total += Number(gameId)
  }
}

console.log(total)