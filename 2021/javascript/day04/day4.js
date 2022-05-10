const fs = require( 'fs' )
const { config } = require('process')

const [ numbersAsRow, ...bingoRows ] = fs.readFileSync( `${__dirname}/input.txt`, { encoding: 'utf8' } )
  .split( '\n' )
  
function createBingosFromRows( bingoRows ) {
  const EMPTY_LINE = ''
  return bingoRows
    .filter( b => b !== EMPTY_LINE )
    .map( b => b
      .split( ' ' )
      .filter( e => e !== '' )
      .map( e => Number( e ) )
    )
    .reduce( ( bingos, row, index ) => {
      if( ( index + 1 ) % 5 === 0 ) {
        const parsedBingos = bingos.slice( 0, -4 )
        const lastFour = bingos.slice( -4 )
        parsedBingos.push( [ ...lastFour, row ] )
        return parsedBingos
      } else {
        bingos.push( row )
        return bingos
      }
    }, [] )
}

const numbers = numbersAsRow
  .split(',')
  .map( e => Number( e ) )

function part1( numbers, bingos ) {
  let result = -1
  for( let i = 0; i < numbers.length; i++ ) {
    let number = numbers[ i ]
    
    for( let j = 0; j < bingos.length; j++ ) {
      let bingo = bingos[ j ]
      
      for( let k = 0; k < bingo.length; k++ ) {
        let row = bingos[ j ][ k ]
        
        const columnIndex = row.indexOf( number )
        
        if( columnIndex > -1 ) {
          bingos[j][k][columnIndex] = true
          
          if( hasWinner( bingo ) ) {
            result = bingo.reduce( (c, n) => {
              return c + n.reduce( ( d, o ) => {
                return typeof o === 'number' ? d + o : d
              } , 0 )
            }, 0 ) * number
          }
          
          break
        }
      }
      if( result > -1) {
        break
      }
    }
    if( result > -1) {
      break
    }
  }
  console.log( result )
}

function part2( numbers, bingos ) {
  const winners = {}
  let lastWinner
  for( let i = 0; i < numbers.length; i++ ) {
    const number = numbers[ i ]
    
    for( let j = 0; j < bingos.length; j++ ) {
      const bingo = bingos[ j ]

      if( winners[ j ] ) {
        continue
      }
      
      for( let k = 0; k < bingo.length; k++ ) {
        const row = bingos[ j ][ k ]
        
        const columnIndex = row.indexOf( number )
        
        if( columnIndex > -1 ) {
          bingos[j][k][columnIndex] = true
          
          if( hasWinner( bingo ) ) {
            const result = bingo.reduce( (c, n) => {
              return c + n.reduce( ( d, o ) => {
                return typeof o === 'number' ? d + o : d
              } , 0 )
            }, 0 ) * number
            winners[ j ] = true
            lastWinner = result
          }
        }
      }
    }
  }
  console.log( lastWinner )
}

function hasWinner( bingo ) {
  for( let i =0 ; i < 5; i++ ) {
    if( 
      (
        bingo[ 0 ][ i ] === true && 
        bingo[ 1 ][ i ] === true && 
        bingo[ 2 ][ i ] === true && 
        bingo[ 3 ][ i ] === true && 
        bingo[ 4 ][ i ] === true
        )
        || 
        (
          bingo[ i ][ 0 ] === true && 
          bingo[ i ][ 1 ] === true && 
          bingo[ i ][ 2 ] === true && 
          bingo[ i ][ 3 ] === true && 
          bingo[ i ][ 4 ] === true
          )
    ) {
      return true
    }
  }
  return false
}

const bingos = createBingosFromRows( bingoRows )
part1( numbers, bingos )
part2( numbers, bingos )