import {merge} from './main-pt2.mjs'

test( "a", () => {
	const mapA = [
		[ 52, 50, 48 ]
	]

	const mapB = [
		[ 0, 15, 37 ],
		[ 37, 52, 2 ],
	]

	const result = merge(mapA, mapB)
	console.log(result)
	expect(result).toEqual([
		[37,50, 2],
		[54,52,46 ],
	])

})

test( "b", () => {
	const mapA = [
		[ 52, 50, 48 ],
		[ 50, 98, 2]
	]

	const mapB = [
		[ 0, 15, 37 ],
		[ 37, 52, 2 ],
		[ 39, 0, 15]
	]

	const result = merge(mapA, mapB)
	console.log(result)
	expect(result).toEqual([
		[37,50, 2],
		[54,52,46 ],
		[35,98,2],
		[39,0,15],
		[0,15,35]
	])

})

