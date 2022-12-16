import numpy as np


def loadData() -> tuple[tuple[int, int], tuple[int, int], np.array]:
    elevation = []
    with open('aoc12.txt', 'r') as f:
        for line in f.readlines():
            elevation.append([i for i in line.strip()])
    elevation = np.array(elevation, dtype='<U1')
    start = tuple(np.asarray(np.where(elevation == 'S')).T[0])
    end = tuple(np.asarray(np.where(elevation == 'E')).T[0])
    elevation[start] = 'a'
    elevation[end] = 'z'
    return start, end, elevation.view(dtype='int32') - 97


def neighbors(elevation: np.array, point: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = point
    neighbors = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]
    return [n for n in neighbors if
            (np.array([0, 0]) <= np.array(n)).all() and (np.array(n) < np.array(elevation.shape)).all()]


def djikstra(elevation: np.array, start: tuple[int, int], ends: list[tuple[int, int]], blocker) -> list[
    tuple[int, int]]:
    openList = neighbors(elevation, start)
    closedList = [start]
    came_from = {o: start for o in openList}

    def g(current, s=None):
        path = [current]
        while path[-1] != start:
            try:
                path.append(came_from.get(path[-1], s))
            except KeyError:
                pass
        path = path[::-1]

        return len(path)

    def h(current):
        return min(np.linalg.norm(np.array(end) - np.array(current)) for end in ends)

    def f(current):
        return round(g(current) + h(current), 3)

    while openList:
        s = sorted(openList, key=lambda h: f(h))[0]
        openList.remove(s)
        closedList.append(s)
        if s in ends:
            break
        for t in neighbors(elevation, s):
            if blocker(s, t):
                continue
            if t not in closedList:
                if t not in openList:
                    openList.append(t)
                came_from.update({t: s})
        closedList = list(set(closedList))
        print(f(s), closedList, openList, [f(s) for s in openList])

    path = [s]
    while path[-1:][0] != start:
        try:
            path.append(came_from[path[-1:][0]])
        except KeyError:
            return
    return path[::-1]


start, end, elevation = loadData()
path = djikstra(elevation, start, [end], blocker=lambda s, t: elevation[t] - elevation[s] > 1)
print(len(path) - 1)
path = djikstra(elevation, end, [tuple(i) for i in np.asarray(np.where(elevation == 0)).T], blocker=lambda s, t: elevation[s] - elevation[t] > 1)
print(len(path) - 1)
