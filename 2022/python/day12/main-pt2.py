inputFile = open("input.txt", "r")
file = inputFile.read()
l = [list(line) for line in file.split("\n")[:-1]]
d = dict()

for r in range(len(l)):
    for p in range(len(l[0])):
        if l[r][p] != "a":
            continue

        starting = [r,p]
        depth = 0
        children = 0
        totalChildren = 1
        stack = [[starting]]
        s = set()
        lookForE = True

        while lookForE:
            [x, y] = stack[depth][children]
            val = l[x][y]
            val = "a" if val == "S" else val
            key = f'{x}{y}'
            s.add(key)


            if val == "E":
                lookForE = False
                break

            toLook = []
            if x-1 >=0:
                tmp = l[x-1][y]
                childrenVal = ord("z" if tmp == "E" else tmp)
                if childrenVal - ord(val) <= 1: 
                    key = f'{x-1}{y}'
                    if key not in s:
                        s.add(key)
                        toLook.append([x-1, y])
            if x+1 < len(l):
                tmp = l[x+1][y]
                childrenVal = ord("z" if tmp == "E" else tmp)
                if childrenVal - ord(val)<= 1:
                    key = f'{x+1}{y}'
                    if key not in s:
                        s.add(key)
                        toLook.append([x+1, y])
            
            if y-1 >=0:
                tmp = l[x][y-1]
                childrenVal = ord("z" if tmp == "E" else tmp)
                if childrenVal - ord(val) <=1:
                    key = f'{x}{y-1}'
                    if key not in s:
                        s.add(key)
                        toLook.append([x, y-1])

            if y+1 < len(l[x]):
                tmp = l[x][y+1]
                childrenVal = ord("z" if tmp == "E" else tmp)
                if childrenVal - ord(val) <=1:
                    key = f'{x}{y+1}'
                    if key not in s:
                        s.add(key)
                        toLook.append([x, y+1])

            if depth == len(stack) -1:
                stack.append(toLook)
            else:
                stack[-1] += toLook
            
            children+=1
            if totalChildren == children:
                depth+=1
                totalChildren = len(stack[depth])
                children =0
         
        d[f'rp']= depth

print(d)
            
