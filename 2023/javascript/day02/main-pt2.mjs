import { readFileSync } from "node:fs"

const file = readFileSync("./input.txt")
const games = String(file).split("\n")

let total = 0
for (let game of games) {
  const [_, played] = game.split(": ")
  const cubes = played.split(new RegExp("[;,]")).map(e => e.trim())

  const minCubes = {
    "red": 1,
    "green": 1,
    "blue": 1
  }

  for (let cube of cubes) {
    const [amount, color] = cube.split(" ")
    const amountCubes = Number(amount)
    if (minCubes[color] < amountCubes) {
      minCubes[color] = amountCubes
    }
  }

  total += minCubes["red"] * minCubes["green"] * minCubes["blue"]
}

console.log(total)