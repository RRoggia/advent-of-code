import { readFileSync } from 'node:fs'

const rows = String(readFileSync("./input.txt")).split("\n")

const [seedsString, ...maps] = rows

const seeds = seedsString
  .split(":")[1]
  .trim()
  .split(" ")
  .map(n => Number(n))

const allMaps = maps
  .filter(m => m !== "")
  .reduce((acc, a) => {
    if (a.includes(":")) {
      const key = a.split(" map:")[0]
      acc[0] = key
      acc[1][key] = []
    } else {
      acc[1][acc[0]].push(a)
    }
    return acc
  }, ["key", {}])[1]


Object.keys(allMaps)
  .forEach(k => {
    allMaps[k] = allMaps[k].map(i => {
      return i.split(" ")
        .filter(el => "" !== el)
        .map(el => Number(el))
    })
  })

function getLocation(map, x) {
  const location = map
    .find(l => l[1] <= x && x < l[1] + l[2])

  if (location) {
    console.log(`found location ${location}`)
    return location[0] + x - location[1]
  }
  return x
}

const mappingOrder = [
  "seed-to-soil",
  "soil-to-fertilizer",
  "fertilizer-to-water",
  "water-to-light",
  "light-to-temperature",
  "temperature-to-humidity",
  "humidity-to-location"
]
const b = seeds.reduce((acc, a) => {
  if (acc[acc.length - 1].length < 2) {
    acc[acc.length - 1].push(a)
  } else {
    acc.push([a])
  }
  return acc
}, [[]])
/*
const next = allMaps['soil-to-fertilizer']
for (let m of allMaps['seed-to-soil']) {
  m[0] + m[2]
  const interval = next.find(l=> l[1] <= m[0] && m[0] <l[1]+l[2])
	
  const newInterval = [ m[0], Math.min(m[0]+m[2]-1, interval[1]+interval[2]-1)]
 
  console.log("init seed interval", m[0])
  console.log("init soil", interval)
  console.log("seed-to-soil", newInterval)
  console.log("skip in seed", newInterval[1]-newInterval[0])
 
}*/

export function merge(mapA, mapB) {
  const aToC = []
  for (let entry of mapA) {
    let [destB, sourceA, rangeA] = entry

    let isSubset = true
    while(isSubset) {

	  console.log("sourceA is", sourceA, " destB is ", destB)

    const conflict = mapB.find(([destC, sourceB, rangeB]) => sourceB <= destB && destB < sourceB + rangeB)
    if(!conflict) {
	const newA = [destB, sourceA, rangeA	]
      aToC.push(newA)
	    isSubset=false
    }else {
      const [destC, sourceB, rangeB] = conflict
      console.log("conflict with rangeB", conflict)
      const lowerEnd = Math.min(rangeA, sourceB + rangeB - destB)
      console.log("rangeA", rangeA)
      console.log(sourceB+rangeB-destB)
      console.log("add atoc", sourceA, lowerEnd)
      aToC.push([destC + destB - sourceB, sourceA, lowerEnd ])

      if(destB+rangeA > sourceB+rangeB){
	destB +=lowerEnd
	sourceA+=lowerEnd
	rangeA-=lowerEnd
      }else{
	isSubset=false
      }

	//se b is subset of a, a has more intervals
	//se b is superset of a, entry is finished
    }

  	}
  }

  console.log(aToC)
  return aToC
}
//merge(allMaps['seed-to-soil'], allMaps['soil-to-fertilizer'])

/*
const a ={
  'seed-to-soil': {
    'next': 'soil-to-fertilizer',
    'ranges': {
      'start': [next.ranges]
    }
  }
}*/


/*
const result = b.reduce((lowerLocation, seedRange)=> {
  const [start,end] = seedRange
  console.log(seedRange)
  let rangeLocation=Number.MAX_SAFE_INTEGER
  for(let seed = start; seed < start +end; seed++){
    console.log(`starting with seed ${seed}`)
    rangeLocation = Math.min(rangeLocation,  mappingOrder.reduce((acc, k) => {
      const map = allMaps[k]

      const loc = map
        .find(l => l[1] <= acc && acc < l[1]+l[2])
	
      if(loc) {
        console.log(`found loc ${loc}`)
        return loc[0] + acc - loc[1]
      }

      console.log(`for keys ${k} found ${acc}`)
      return acc

    }, seed))
  }
  return Math.min(lowerLocation, rangeLocation)	
}, Number.MAX_SAFE_INTEGER)

console.log(result)
*/
