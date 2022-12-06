with open('aoc3.txt', 'r') as f:
    rucksacks = [[
        line.strip()[:len(line.strip()) // 2],
        line.strip()[len(line.strip()) // 2:]
    ] for line in f.readlines()]


def getPriority(char):
    code = ord(char)
    if 65 <= code <= 90:
        return code - ord('A') + 27
    elif 97 <= code <= 122:
        return code - ord('a') + 1


def getDuplicate(rucksack):
    return {i for i in rucksack[0] if i in rucksack[1]}


totalPriority = 0
for rucksack in rucksacks:
    totalPriority += getPriority(next(iter(getDuplicate(rucksack))))
print(totalPriority)


def getBadge(*group):
    return {j for j in {i for i in ''.join(group[0]) if i in ''.join(group[1])} if j in ''.join(group[2])}


totalPriority = 0
for i, rucksack in enumerate(rucksacks):
    if not i % 3:
        totalPriority += getPriority(next(iter(getBadge(*rucksacks[i:i + 3]))))
print(totalPriority)
