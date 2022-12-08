import numpy as np

with open('8.txt', 'r') as f:
    forest = np.array([[int(i) for i in line.strip()] for line in f.readlines()])


def isVisible(forest: list, t: tuple):
    x, y = t
    treeHeight = forest[y][x]
    if y == forest.shape[0] - 1 or x == forest.shape[1] - 1:
        return True
    return not (
            np.any(treeHeight <= forest[y, x + 1:]) and
            np.any(treeHeight <= forest[y, :x]) and
            np.any(treeHeight <= forest[:y, x]) and
            np.any(treeHeight <= forest[y + 1:, x])
    )


visible = np.zeros(shape=forest.shape)

for i, y in enumerate(forest):
    for j, x in enumerate(y):
        visible[i][j] = isVisible(forest, (j, i))

print(f"{visible.sum():0.0f}")


def scenicScore(forest: list, t: tuple):
    x, y = t
    treeHeight = forest[y][x]
    score = []
    for direction in [
        forest[y, x + 1:],
        forest[y, :x][::-1],
        forest[y + 1:, x],
        forest[:y, x][::-1]
    ]:
        count = 0
        for i, h in enumerate(direction):
            count += 1
            if h >= treeHeight:
                break
        score.append(count)
    return np.product(score)


scenicScores = np.zeros(shape=forest.shape)

for i, y in enumerate(forest):
    for j, x in enumerate(y):
        scenicScores[i][j] = scenicScore(forest, (j, i))

print(f"{scenicScores.max()}")
