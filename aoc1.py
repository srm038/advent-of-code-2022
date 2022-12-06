with open('aoc1.txt', 'r') as f:
    elvesRaw = f.read().split('\n\n')
elves = [[int(i) for i in item.split('\n')] for elf, item in enumerate(elvesRaw)]
i = elves.index(max(elves, key=lambda calories: sum(calories)))
print(sum(elves[i]))
print(sum(sum(sorted(elves, key=lambda elf: sum(elf), reverse=True)[:3], [])))
