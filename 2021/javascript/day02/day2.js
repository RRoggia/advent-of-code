const fs = require( 'fs' )

const coordinates = fs.readFileSync( `${__dirname}/input.txt`, { encoding: 'utf8' } )
  .split( '\n' )

function part1( coordinates ) {
  const res = coordinates.reduce( (curr, next ) => {
    const [ dir, num ] = next.split( ' ' )

    switch( dir ) {
      case 'forward':
        curr.hor += Number( num )
        break
      case 'down':
        curr.dep += Number( num )
        break
      case 'up':
        curr.dep -= Number( num )
        break
    }

    return curr
  }, { hor: 0, dep: 0 } )

  console.log( JSON.stringify( res ) )
  console.log( `PT 1 - horizontal times depth ${ res.hor * res.dep }`)
}


function part2( coordinates ) {
  const res = coordinates.reduce( (curr, next ) => {
    const [ dir, num ] = next.split( ' ' )

    switch( dir ) {
      case 'forward':
        curr.hor += Number( num )
        curr.dep += Number( num ) * curr.aim
        break
      case 'down':
        curr.aim += Number( num )
        break
      case 'up':
        curr.aim -= Number( num )
        break
    }

    return curr
  }, { hor: 0, dep: 0, aim: 0 } )

  console.log( JSON.stringify( res ) )
  console.log( `PT 2 - horizontal times depth ${ res.hor * res.dep }`)
}

part1( coordinates )
part2( coordinates )