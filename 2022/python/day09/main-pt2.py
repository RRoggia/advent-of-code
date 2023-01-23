inputFile = open("day9.txt", "r")
lines = inputFile.read().split('\n')

ropeBody = [ {
  "x":0,
  "y":0
} for _ in range(10)]

results = set()
results.add(str(ropeBody[9]))

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

moves =0
for line in lines:
  direction, quantity = line.split()
  quantity = int(quantity)
  
  for i in range(quantity):
    first = ropeBody[0]
    second = ropeBody[0]
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