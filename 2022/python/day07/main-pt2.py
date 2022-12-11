inputFile = open("day7.txt", "r")
lines = inputFile.read().split('\n')

maxSize = 70000000
installationSize = 30000000

instructions = []
for line in lines:
    instruction = {}
    if line.find("$ ls") >= 0:
        continue
    elif line.find("$ cd") >= 0:
        instruction["moveTo"] = line.split("cd ")[1]
        instruction["instruction"] = "cd"
    elif line.find("dir") >= 0:
        instruction["name"] = line.split("dir ")[1]
        instruction["instruction"] = "dir"
    else:
        instruction["size"] = int(line.split()[0])
        instruction["name"] = line.split()[1]
        instruction["instruction"] = "file"
    instructions.append(instruction)

three = {}
current = ""
history = []
for instruction in instructions:
    if instruction["instruction"] == "cd":
        if instruction["moveTo"] == "..":
            history.pop()
            current = history[-1]
            continue

        current = instruction["moveTo"]
        history.append(current)
        if current not in three:
            key = '/'.join(history)
            three[key] = {}
            three[key]["files"] = {}
            three[key]["folders"] = set()
    else:
      key = '/'.join(history)
      name = '/' + instruction["name"]
      if instruction["instruction"] == "dir":
          three[key]["folders"].add(key+name)
      if instruction["instruction"] == "file":
          three[key]["files"][key+name] = instruction["size"]

def evaluateThree(current, calculated):
    totalFiles = 0
    for f in three[current]["files"].values():
        totalFiles += f

    totalFolders = 0
    for f in three[current]["folders"]:
        totalFolders += evaluateThree(f, calculated)

    total = totalFiles+totalFolders
    calculated[current] = total
    return total


calculated = {}
evaluateThree(instructions[0]["moveTo"], calculated)

requiredSize = installationSize - (maxSize - calculated["/"])
deleteFile = calculated["/"]
for i in calculated.values():
  if i < deleteFile and i >= requiredSize:
    deleteFile = i

print(deleteFile)
