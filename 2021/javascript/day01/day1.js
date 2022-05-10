const fs = require( 'fs' )

const measurements = fs.readFileSync( `${__dirname}/input.txt`, { encoding: 'utf8' } ).split( '\n' ).map( e => Number(e) )

function part1( measurements ) {
  let sum = 0
  for( let i =0; i < measurements.length; i++ ) {
    if( i + 1 >= measurements.length ) {
      break
    }
  
    if( measurements[ i ] < measurements[ i + 1] ) {
      console.log( measurements[ i ], '<', measurements[ i + 1])
      sum++
    }
  }
  console.log( `PT1 - The total times is ${ sum }` )
}

function part2( measurements ) {
  let sum = 0
  for( let i =0; i < measurements.length; i++ ) {
    if( i + 3 >= measurements.length ) {
      break
    }
  
    if( measurements[ i ] + measurements[ i + 1 ] + measurements[ i + 2 ] < measurements[ i + 1] + measurements[ i + 2 ] + measurements[ i + 3 ] ) {
      sum++
    }
  }
  console.log( `PT2 - The total times is ${ sum }` )
}

part1( measurements )
part2( measurements )