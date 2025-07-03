import math

inputFile = open("test-input.txt", "r")
lines = inputFile.read().split("\n")
monkeys = []
def main():
    md = dict.fromkeys(range(8), 0)
    monkey = []
    for line in lines:
        if line.startswith('Monkey'):
            monkey.append(line.split(" ")[1][0])
        elif line.startswith('  Starting items:'):
            monkey.append(line.split(": ")[1].split(", "))
        elif line.startswith('  Operation:'):
            monkey.append(line.split("old ")[1].split(" "))
        elif line.startswith('  Test:'):
            monkey.append(int(line.split("by ")[-1]))
        elif line.startswith('    If true:'):
            monkey.append(int(line.split("monkey ")[-1]))
        elif line.startswith('    If false:'):
            monkey.append(int(line.split("monkey ")[-1]))
        else:
            monkeys.append(monkey)
            monkey = []

    for round in range(10):
        print(f'Starting round {round}')
        for m in monkeys:
            id, items, [op, val], div, pos, neg = m
            print(f'  Starting monkey {id}')
            md[int(id)] += len(items)
            for item in items:
                it = int(item)
                print(f'    inspects {it}')
                n_val = it if val == "old" else val
                n_worry = it * int(n_val) if op == "*" else it + int(n_val)
                print(f'    new worry {n_worry}')
                if n_worry %div == 0:
                    print(f'      new worry is div by {div} send item {n_worry} to monkey {pos}')
                    monkeys[pos][1].append(n_worry)
                else:
                    print(f'      new worry not div by {div} send item {n_worry} to monkey {neg}')
                    monkeys[neg][1].append(n_worry)
            m[1].clear()

    print(md)

if __name__ == "__main__":
    main()
