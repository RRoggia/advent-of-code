const initialState2 = {
  "HM":1,
  "LM":1,
  "HG":2,
  "LG":3,
}
const initialState = {
  "POG":1,
  "POM":2,
  "TUG":1,
  "TUM":1,
  "PRG":1,
  "PRM":2,
  "RUG":1,
  "RUM":1,
  "COG":1,
  "COM":1,
  "ELG":1,
  "ELM":1,
  "DIG":1,
  "DIM":1
}

let myFloor = 1
const queue = {
  [createStateKey(initialState, myFloor)]: true
}

createTree(queue, initialState)

function createTree(queue, initialState){
  let allPaths = [{
    state: initialState,
    floor: 1
  }]
  let nextEdge = 0
  let count = 0
  let endOfLayer = 1
  let nextLayer = 0
  while( allPaths[nextEdge] !== undefined) {
//    console.log(allPaths[nextEdge])
    const state = allPaths[nextEdge].state
    const currentFloor = allPaths[nextEdge].floor

//    console.log("my state is", createStateKey(state, currentFloor), "and counting", count, ".")

    if(Object.values(state).filter(f => f===4).length === 14) {
      console.log(">>>>>>>>>>> Latest state with:", count)
      return
    }

    let resources = Object.entries(state)
                      .filter(([resource, floor]) => floor === currentFloor)
                      .map(([r, f]) => r)
    let validStatesUp = []
    let validStatesDown = []

    for(let i=0; i < resources.length; i++){
      const r = resources[i]
      const canGoUp = currentFloor + 1 < 5
      const canGoDown = currentFloor -1 > 0

//      console.log("Process single moves")
//      console.log("might have upper floor states")
      addValidStates(r, state, currentFloor, currentFloor + 1, validStatesUp, canGoUp)

//      console.log("might have lower floor")
      addValidStates(r, state, currentFloor, currentFloor - 1, validStatesDown,  canGoDown)
      
//      console.log("Process double moves")
      for(let j = i+1; j < resources.length; j++){
        const r2 = resources[j] 
//        console.log("might have upper floor states")
        addValidStatesMovingTwo(r, r2, state, currentFloor, currentFloor + 1, validStatesUp, canGoUp)

//        console.log("might have lower floor")
        addValidStatesMovingTwo(r, r2, state, currentFloor, currentFloor - 1, validStatesDown, canGoDown)
      }
    }

    allPaths = allPaths.concat(validStatesUp)
    allPaths = allPaths.concat(validStatesDown)

    endOfLayer--
    nextLayer += validStatesUp.length + validStatesDown.length
    if(endOfLayer === 0){
//      console.log("end of cycle for", count, "next cycle", count +1, "has", nextLayer)
      count++
      endOfLayer = nextLayer
      nextLayer = 0
    }
    nextEdge++
  }

}

function getCounterPart(resource){
  let prefix = resource.substring(0, resource.length - 1)
  return `${prefix}${isGenerator(resource) ? "M" : "G"}`
}

function hasSingleMicroInFloor(state, floor){
  return Object.entries(state) 
    .filter(([r,f]) => f === floor)
    .map(([r,f]) => r)
    .filter(r => state[getCounterPart(r)] !== floor)
    .some(r => !isGenerator(r))
}

function isGenerator(resource){
  return resource[resource.length -1] === "G"
}

function canMove(state, resource ) {
  const sameFloor = state[getCounterPart(resource)] === state[resource]
  
  if(sameFloor) {
    (isGenerator(resource) && !Object.entries(state)
      .some(([r,f]) => r !== resource && f === state[resource] && isGenerator(r)))
  } 

  isGenerator(resource)
}

function isValidState(state) {
 return isValidFloor(Object.entries(state)
    .filter(([r,f]) => f === 1)
    .map(([r,f]) => r)) &&
  isValidFloor(Object.entries(state)
    .filter(([r,f]) => f === 2)
    .map(([r,f]) => r)) &&
  isValidFloor(Object.entries(state)
    .filter(([r,f]) => f === 3)
    .map(([r,f]) => r)) &&
  isValidFloor(Object.entries(state)
    .filter(([r,f]) => f === 4)
    .map(([r,f]) => r))
}

function isValidFloor(floorResources){
  const pool = {}
  
  let hasG = false
  for(let i =0; i < floorResources.length; i++){
    const resource = floorResources[i]
    if(isGenerator(resource)){
      hasG = true
    }
    const key = isGenerator(resource) ? getCounterPart(resource) : resource
    if(key in pool){
      delete pool[key]
    }else{
      pool[key] = resource
    }
 } 
  let hasM = false
  
  for(let v of Object.values(pool)) {
    if(!isGenerator(v)){
      hasM = true
    }
  }
  return !(hasG && hasM)
}


function createStateKey(state, floor) {
  return floor.toString() + JSON.stringify(state)
}

function addValidStates(r, state, currentFloor, nextFloor,  validStates, canGoUpOrDown) {
  if(!canGoUpOrDown) {
    return
  }

  const newState = {...state}
  newState[r] = nextFloor 
  const newStateKey = createStateKey(newState, nextFloor) 
//  console.log(newStateKey)
//  console.log("not in queue", !queue[newStateKey])
//  console.log("isValid", isValidState(newState))
  if(!queue[newStateKey] && isValidState(newState)) {
    queue[newStateKey] = true
//    console.log("add new possible state", newStateKey, " moving", r)
    validStates.push( {
      state: newState,
      floor: nextFloor
    } )
  }
}

function addValidStatesMovingTwo(r, r2, state, currentFloor, nextFloor, validStates, canGoUpOrDown) {
  if(!canGoUpOrDown) {
    return
  }
  const newState = {...state}
  newState[r] = nextFloor
  newState[r2] = nextFloor
  const newStateKey = createStateKey(newState, nextFloor)
//  console.log(newStateKey)
//  console.log("not in queue", !queue[newStateKey])
//  console.log("isValid", isValidState(newState))
  if(!queue[newStateKey] && isValidState(newState)) {
    queue[newStateKey] = true
//    console.log("add new possible state", newStateKey, " moving ", r, r2)
    validStates.push( {
      state: newState,
      floor: nextFloor
    } )
  }
}

