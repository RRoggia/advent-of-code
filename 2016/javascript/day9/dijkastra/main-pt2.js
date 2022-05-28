const fs = require('fs')

const file = fs.readFileSync(`${__dirname}/input.txt`, {
  encoding: 'utf8'
})

const values = []
const operators = []
let total = 0
let count = 0
let mountValue1 = false
let mountValue2 = false
let value1 = ''
let value2 = ''
let ignore = 0

for( letter of file ) {
  switch( letter ) {
    case '(':
      if( count > 0 ) {
        values.push( count )
        operators.push( "+" )  
        count = 0
      }
      mountValue1 = true
      continue;
    case 'x':
      mountValue1 = false
      mountValue2 = true
      continue
    case ')':
      mountValue2 = false
      total += parseInt( value1 ) * parseInt( value2 )
      ignore = parseInt( value1 )
      value1 = ''
      value2 = ''
      continue
  }

  if( ignore > 0 ) {
    ignore--
    continue
  }
  
  if( mountValue1 ) {
    value1 += letter
  } else if( mountValue2 ) {
    value2 += letter
  } else {
      count++
  }
}
console.log( total )
