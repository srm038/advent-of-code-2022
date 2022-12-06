scores = {'X': 1, 'Y': 2, 'Z': 3}
wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
losses = {'A': 'Z', 'B': 'X', 'C': 'Y'}
ties = {'A': 'X', 'B': 'Y', 'C': 'Z'}


def scoreRound(a, b):
    tie = ties[a] == b
    win = not tie and wins[a] == b
    return scores[b] + 3 * tie + 6 * win


with open('aoc2.txt', 'r') as f:
    guide = [line.strip().split(' ') for line in f.readlines()]

totalScore = 0
for a, b in guide:
    totalScore += scoreRound(a, b)
print(totalScore)


def strategyRound(a, b):
    play = {'X': losses, 'Y': ties, 'Z': wins}[b][a]
    return scores[play] + 3 * (b == 'Y') + 6 * (b == 'Z')


totalScore = 0
for a, b in guide:
    totalScore += strategyRound(a, b)
print(totalScore)
