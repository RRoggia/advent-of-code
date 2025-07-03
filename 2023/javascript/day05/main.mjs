import { readFileSync } from 'node:fs'

const rows = String(readFileSync("./input.txt")).split("\n")

const [seedsString, ...maps] = rows

const seeds = seedsString
	.split(":")[1]
	.trim()
	.split(" ")
	.map(n => Number(n))


const allMaps = maps
	.filter( m => m !== "")
	.reduce((acc, a) => {
		if( a.includes(":")) {
			const key = a.split(" map:")[0]
			acc[0] = key
			acc[1][key] = []
		}else {
			acc[1][acc[0]].push(a)
		}
		return acc
	}, ["key",{}])[1]


Object.keys(allMaps)
	.forEach(k => {
		allMaps[k] = allMaps[k].map(i => { 
			return i.split(" ")
				.filter(el => "" !== el)
				.map( el => Number(el))
		})
	})

function getLocation(map, x) {
	const location = map
		.find(l => l[1] <= x && x < l[1]+l[2])
	
	if(location) {
		return location[0] + x - location[1]
	}
	console.log(x)
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

const result = seeds.reduce((lower, seed) => {
	const location = mappingOrder.reduce((acc, k) => getLocation(allMaps[k],acc), seed)
	return Math.min(lower, location) 
}, Number.MAX_SAFE_INTEGER)

console.log(result)
