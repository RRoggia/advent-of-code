import { readFileSync } from 'node:fs';

const file = readFileSync("./input.txt")
const lines = String(file).split("\n")
let count = 0 // complexity 
let sum = 0;

for (let line of lines) {
  let value = "";

  for (let si = 0; si < line.length; si++) {
    count++
    const letter = line.charAt(si)
    if (!isNaN(Number(letter))) {
      value += letter;
      break
    }
  }

  for (let ei = line.length - 1; ei >= 0; ei--) {
    count++

    const letter = line.charAt(ei)
    if (!isNaN(Number(letter))) {
      value += letter;
      break
    }

  }
  sum += Number(value)
}
console.log(count)
console.log(sum)

