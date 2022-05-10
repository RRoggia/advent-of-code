const fs = require( 'fs' )

const diagnosticReport = fs.readFileSync( `${__dirname}/input.txt`, { encoding: 'utf8' } )
  .split( '\n' )

function part1( diagnosticReport ) {

  const total = {}
  for( let i = 0; i < diagnosticReport.length; i++ ) { 
    for( let j = 0; j < diagnosticReport[ i ].length; j++) {
      if( !total[ j ] ) {
        total[ j ] = 0
      }
      
      if( diagnosticReport[ i ][ j ] === '1' ) {
        total[ j ] += 1
      }
    }
  }
  
  let gammaRate = ''
  let epsilonRate = ''
  
  Object.keys( total ).forEach( e => {
    if( total[ e ] > diagnosticReport.length / 2 ) {
      gammaRate = `${gammaRate}1`
      epsilonRate = `${epsilonRate}0`
    } else {
      gammaRate = `${gammaRate}0`
      epsilonRate = `${epsilonRate}1`
    }
    console.log( total[ e ] )
  } )
  console.log( gammaRate, epsilonRate)
  
  console.log( `PT 1 - Power consumption is ${ parseInt(gammaRate, 2) * parseInt(epsilonRate, 2) }`)
}

function part2( diagnosticReport, columnIndex ) {
  if( columnIndex >= diagnosticReport[0].length || diagnosticReport.length === 1 ) {
    return ''
  }
  
  const total = {}
  let zeros = []
  let ones = []

  for( let i = 0; i < diagnosticReport.length; i++ ) { 
    if( diagnosticReport[ i ][ columnIndex ] === '1' ) {
      ones.push( diagnosticReport[ i ] )
    } else {
      zeros.push( diagnosticReport[ i ] )
    }
  }

  
  console.log( ones.length, zeros.length)
  // if( zeros.length <= ones.length  ) {
  if( zeros.length > ones.length  ) {
    console.log( zeros )
    return `0${part2( zeros, columnIndex + 1 )}`
  } else {
    console.log( ones )
    return `1${part2( ones, columnIndex + 1 )}`
  }
}

  part1( diagnosticReport )
  // console.log( part2( diagnosticReport, 0 ) ) //110111111111 011001000001
  console.log( parseInt('110111111111', 2) * parseInt('011001000001', 2))