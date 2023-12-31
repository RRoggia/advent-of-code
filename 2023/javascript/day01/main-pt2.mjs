import { readFileSync } from 'node:fs';

const file = readFileSync("./input.txt")
const lines = String(file).split("\n")
let count = 0
let sum = 0;

const digits = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}
for (let line of lines) {
  let value = "";

  for (let si = 0; si < line.length; si++) {
    count++
    const letter = line.charAt(si)
    if (!isNaN(Number(letter))) {
      value += letter;
      break
    }

    const threeLetter = line.substring(si, si + 3)
    if (digits[threeLetter]) {
      value += digits[threeLetter]
      break
    }
    const fourLetter = line.substring(si, si + 4)
    if (digits[fourLetter]) {
      value += digits[fourLetter]
      break
    }
    const fiveLetter = line.substring(si, si + 5)
    if (digits[fiveLetter]) {
      value += digits[fiveLetter]
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

    const threeLetter = line.substring(ei - 2, ei + 1)
    if (digits[threeLetter]) {
      value += digits[threeLetter]
      break
    }
    const fourLetter = line.substring(ei - 3, ei + 1)
    if (digits[fourLetter]) {
      value += digits[fourLetter]
      break
    }
    const fiveLetter = line.substring(ei - 4, ei + 1)
    if (digits[fiveLetter]) {
      value += digits[fiveLetter]
      break
    }
  }
  sum += Number(value)
}

console.log(count)
console.log(sum)

