  const initialState = {
    "HM":1,
    "LM":1,
    "HG":2,
    "LG":3,
  }
  const initialState2 = {
    "POG":1,
    "POM":2,
    "TUG":1,
    "TUM":1,
    "PRG":1,
    "PRM":2,
    "RUG":1,
    "RUM":1,
    "COG":1,
    "COM":1
  }

  let myFloor = 1
  const queue = {
    [createStateKey(initialState, myFloor)]: true
  }
  createTree(initialState, myFloor, queue,  0)

function createTree(state, currentFloor, queue, count){
  if(Object.values(state).filter(f => f===4).length === 4) {
    console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    console.log(count)
    return
  }
  console.log("my state is", createStateKey(state, currentFloor), "and counting", count, ".")
  let resources = Object.entries(state)
                    .filter(([resource, floor]) => floor === currentFloor)
                    .map(([r, f]) => r)

  let validStatesUp = []
  let validStatesDown = []

  for(let i=0; i < resources.length; i++){
    const r = resources[i]
    console.log("processing", r)

    addValidUpperStates(r, state, currentFloor, validStatesUp)
    addValidLowerStates(r, state, currentFloor, validStatesDown)

    for(let j = i+1; j < resources.length; j++){
      const r2 = resources[j] 
      addValidUpperStatesMovingTwo(r, r2, state, currentFloor, validStatesUp)
      addValidLowerStatesMovingTwo(r, r2, state, currentFloor, validStatesDown)
      }
    }

  console.log("---------------") 

  for (let vs of validStatesUp) {
    createTree(vs, currentFloor + 1, queue, count + 1)
  }

  for (let vs of validStatesDown) {
    createTree(vs, currentFloor - 1, queue, count + 1)
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
  //console.log("validate state", state)
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
  //console.log(floorResources)
  const pool = {}
  
  for(let i =0; i < floorResources.length; i++){
    const resource = floorResources[i]
    const key = isGenerator(resource) ? getCounterPart(resource) : resource
    //console.log("key", key)
    if(key in pool){
      delete pool[key]
      //console.log("found, delte it", key)
    }else{
      pool[key] = resource
      //console.log("missing, add", key)
    }
 } 
  //console.log(pool)
  let hasG = false
  let hasM = false
  
  for(let v of Object.values(pool)) {
    if(isGenerator(v)){
       hasG = true
    } else {
      hasM = true
    }
  }
  //console.log("isvalid floor", !(hasG && hasM))
  return !(hasG && hasM)
}


function createStateKey(state, floor) {
  return floor.toString() + JSON.stringify(state)
}

function addValidUpperStates(r, state, currentFloor, validStates) {
  if( currentFloor + 1 < 5) {
    console.log("might have upper floor")
    const newState = {...state}
    newState[r] = currentFloor + 1 
    const newStateKey = createStateKey(newState, currentFloor + 1)
    console.log(newStateKey)
    console.log("not in queue", !queue[newStateKey])
    console.log("isValid", isValidState(newState))
    if(!queue[newStateKey] && isValidState(newState)) {
        queue[newStateKey] = true
        console.log("add new possible state", newStateKey, " moving up", r)
        validStates.push(newState)
    }
  }
}

function addValidLowerStates(r, state, currentFloor, validStates) {
  if(currentFloor - 1 > 0) {
    console.log("might have lower floor")
    const newState = {...state}
    newState[r] = currentFloor - 1 
    const newStateKey = createStateKey(newState, currentFloor - 1)
    console.log(newStateKey)
    console.log("not in queue", !queue[newStateKey])
    console.log("isValid", isValidState(newState))
    if(!queue[newStateKey] && isValidState(newState)) {
      queue[newStateKey] = true
      console.log("add new possible state", newStateKey, " moving down", r)
      validStates.push(newState)
    }
  }
}

function addValidUpperStatesMovingTwo(r, r2, state, currentFloor, validStates) {
  if( currentFloor + 1 < 5) {
    const newState = {...state}
    newState[r] = currentFloor + 1 
    newState[r2] = currentFloor + 1
    const newStateKey = createStateKey(newState, currentFloor + 1)
    console.log(newStateKey)
    console.log("not in queue", !queue[newStateKey])
    console.log("isValid", isValidState(newState))
    if(!queue[newStateKey] && isValidState(newState)) {
      queue[newStateKey] = true
      console.log("add new possible state", newStateKey, " moving up", r, r2)
      validStates.push(newState)
    }
  }
}

function addValidLowerStatesMovingTwo(r, r2, state, currentFloor, validStates) {
  if(currentFloor - 1 > 0) {
    const newState = {...state}
    newState[r] = currentFloor - 1 
    newState[r2] = currentFloor - 1 
    const newStateKey = createStateKey(newState, currentFloor - 1)
    console.log(newStateKey)
    console.log("not in queue", !queue[newStateKey])
    console.log("isValid", isValidState(newState))
    if(!queue[newStateKey] && isValidState(newState)) {
      queue[newStateKey] = true
      console.log("add new possible state", newStateKey, " moving down", r, r2)
      validStates.push(newState)
    }
  }
}

// generator
// if alone
// counterpart || no single micro
// if together
// duo is micro || no micro
//
// micro
// if alone
// counterpart || no generator
// if together
// duo is generator || no generator
//
//
// generator
//
// can I move?
// if alone
//  counterpart || no single micro in nextfloor 
// if together
// no single micro in nextfloor && no generator in currentfloor
//
//
// all floors
// dont have generators pairing with micro
