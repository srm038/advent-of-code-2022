def isRangeContained(r: range, s: range):
    return (r.start in s and r[-1] in s) or (s.start in r and s[-1] in r)


def isRangeOverlap(r: range, s: range):
    return (r.start in s) or (s.start in r)


with open('aoc4.txt', 'r') as f:
    pairs = []
    for line in f.readlines():
        pairs.append([[int(j) for j in i.split('-')] for i in line.strip().split(',')])

totalContained = 0
for pair in pairs:
    totalContained += isRangeContained(range(pair[0][0], pair[0][1] + 1), range(pair[1][0], pair[1][1] + 1))
print(totalContained)

totalOverlap = 0
for pair in pairs:
    totalOverlap += isRangeOverlap(range(pair[0][0], pair[0][1] + 1), range(pair[1][0], pair[1][1] + 1))
print(totalOverlap)
