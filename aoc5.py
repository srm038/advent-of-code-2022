import re

with open('aoc5_diagram.txt', 'r') as f:
    stacks = {}
    for line in f.readlines()[:-1][::-1]:
        crates = [line.rstrip()[i:i + 4].strip() for i in range(0, len(line), 4)]
        for c, crate in enumerate(crates):
            if crate:
                stacks.setdefault(c + 1, [])
                stacks[c + 1].append(crate.strip().replace('[', '').replace(']', ''))

with open('aoc5_instructions.txt', 'r') as f:
    instructions = []
    for line in f.readlines():
        instructions.append([int(i) for i in re.split('move | from | to ', line.strip())[1:]])


def moveCrate9000(n: int, initial: int, final: int):
    for _ in range(n):
        crate = stacks[initial].pop()
        stacks[final].append(crate)


for step in instructions:
    moveCrate9000(*step)
    print(stacks)
print(''.join(stacks[i + 1][-1] for i in range(len(stacks))))


def moveCrate9001(n: int, initial: int, final: int):
    crates = stacks[initial][-n:]
    del stacks[initial][-n:]
    stacks[final].extend(crates)


for step in instructions:
    print(stacks)
    moveCrate9001(*step)
print(stacks)
print(''.join(stacks[i + 1][-1] for i in range(len(stacks)) if stacks[i + 1]))
