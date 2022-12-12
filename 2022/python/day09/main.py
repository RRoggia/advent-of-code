inputFile = open("day9.txt", "r")
lines = inputFile.read().split('\n')

head = {
  "x":0,
  "y":0
}

tail = {
  "x":0,
  "y":0,
}
results = set()
results.add(str(tail))

axis = {
  "U": "x",
  "D": "x",
  "R": "y",
  "L": "y"
}

reverse = {
  "x": "y",
  "y": "x"
}

operation = {
  "U": 1,
  "D": -1,
  "R": 1,
  "L": -1
}

for line in lines:
  direction, quantity = line.split()
  quantity = int(quantity)
  
  for i in range(quantity):
    head[axis[direction]] += operation[direction]

    adjacent = []
    for i in range(-1,2):
      adjacent.append(str(head["x"]-1) + str(head["y"]+i))
    
    for i in range(-1,2):
      adjacent.append(str(head["x"]) + str(head["y"]+i))

    for i in range(-1,2):
      adjacent.append(str(head["x"]+1) + str(head["y"]+i))

    key = str(tail["x"]) + str(tail["y"])
    if key in adjacent:
      continue
    
    tail[axis[direction]] += operation[direction]
    if not (tail[reverse[axis[direction]]] == head[reverse[axis[direction]]]):
      tail[reverse[axis[direction]]] = head[reverse[axis[direction]]]

    results.add(str(tail))

print(len(results))