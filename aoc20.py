import numpy as np


def loadData(e=1):
    with open('aoc20.txt', 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]
    return [(i, x * e) for i, x in enumerate(data)]


def numberShift(toShift, i, x):
    oldIndex = toShift.index((i, x))
    newIndex = (oldIndex + x + len(toShift) - 1) % (len(toShift) - 1)
    toShift.remove((i, x))
    toShift.insert(newIndex, (i, x))
    return toShift


data = loadData()
shifted = loadData()
for i, x in data:
    shifted = numberShift(shifted, i, x)
idx0 = shifted.index((-1, 0))
print(sum([
    shifted[(1000 + idx0) % len(shifted)][1],
    shifted[(2000 + idx0) % len(shifted)][1],
    shifted[(3000 + idx0) % len(shifted)][1]
]))


data = loadData(e=811589153)
shifted = loadData(e=811589153)
for _ in range(10):
    for i, x in data:
        shifted = numberShift(shifted, i, x)
idx0 = shifted.index(([i for i, x in shifted if x == 0][0], 0))
print(sum([
    shifted[(1000 + idx0) % len(shifted)][1],
    shifted[(2000 + idx0) % len(shifted)][1],
    shifted[(3000 + idx0) % len(shifted)][1]
]))

