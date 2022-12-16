import math
import re


def loadData():
    monkeys = [{}]
    with open('aoc11.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                monkeys.append({})
            if line.startswith('Starting items: '):
                items = line.replace('Starting items: ', '').split(', ')
                monkeys[-1].update({'items': [int(i) for i in items]})
                monkeys[-1].update({'count': 0})
            if line.startswith('Test: '):
                test = int(line.split(' by ')[1])
                monkeys[-1].update({'test': test})
            if line.find('true') != -1:
                throw = int(line.split(' monkey ')[1])
                monkeys[-1].update({True: throw})
            if line.find('false') != -1:
                throw = int(line.split(' monkey ')[1])
                monkeys[-1].update({False: throw})
            if line.startswith('Operation: '):
                operationRaw = line.split('new = ')[1]
                operands = re.split(' . ', operationRaw)
                operation = re.findall(' [\+\*] ', operationRaw)[0].strip()
                monkeys[-1].update({'operation': (operation, operands)})
    return monkeys


def keepAway(monkeys: dict, rounds: int, manage: int, partTwo:bool=False):
    for _ in range(rounds):
        print(_, monkeys)
        for monkey in monkeys:
            for item in monkey['items']:
                newWorry = changeWorry(item, monkey['operation'], manage, partTwo=True)
                newMonkey = monkey[testItem(newWorry, monkey['test'])]
                monkeys[newMonkey]['items'].append(newWorry)
                monkey['count'] += 1
            monkey['items'].clear()
    print(_ + 1, monkeys)

    return monkeys


def changeWorry(worry: int, operation: tuple[str, list[str]], manage: int, partTwo=False) -> int:
    operands = [worry if operand == 'old' else int(operand) for operand in operation[1]]
    newWorry = {'*': math.prod(operands), '+': math.fsum(operands)}[operation[0]]
    if partTwo:
        return newWorry * math.lcm(*[monkey['test'] for monkey in monkeys])
    else:
        return math.floor(newWorry / manage)


def testItem(worry: int, test: int) -> bool:
    return not worry % test


def monkeyBusiness(monkeys: list[dict]) -> int:
    counts = sorted(monkeys, key=lambda monkey: monkey['count'], reverse=True)[:2]
    return math.prod([monkey['count'] for monkey in counts])


monkeys = loadData()
monkeys = keepAway(monkeys, 20, 3)
print(monkeyBusiness(monkeys))

monkeys = loadData()
monkeys = keepAway(monkeys, 10000, 1, partTwo=True)
print(monkeyBusiness(monkeys))
