import math

import numpy as np

move = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}


def loadData() -> tuple[list, int, int, int, int]:
    with open('aoc9.txt', 'r') as f:
        directions = []
        for line in f.readlines():
            d, i = line.split(" ")
            directions.append((d, int(i)))

    x, y = 1, 1
    maxX, maxY = 1, 1
    minX, minY = 1, 1

    for d, i in directions:
        x += i * move[d][0]
        y -= i * move[d][1]
        maxX, maxY = max(x, maxX), max(y, maxY)
        minX, minY = min(x, minX), min(y, minY)

    return directions, minX, minY, maxX, maxY


def distance(a: tuple[int, int], b) -> float:
    return math.hypot(b[1] - a[1], b[0] - a[0])


def tailMove(headB: tuple[int, int], tailA: tuple[int, int]) -> tuple[int, int]:
    if distance(tailA, headB) < 2:
        return tailA
    AB = np.array(headB) - np.array(tailA)
    if AB[0] and not AB[1]:
        tailB = tuple(np.array(tailA) + np.array((1, 0)) * np.sign(AB[0]))
    elif not AB[0] and AB[1]:
        tailB = tuple(np.array(tailA) + np.array((0, 1)) * np.sign(AB[1]))
    else:
        tailB = tuple(np.array(tailA) + np.array((1, 1)) * np.sign(AB))
    return tailB


def headMove(head: np.ndarray, tail: np.ndarray, d: str, i: int, headA: tuple[int, int], tailA: tuple[int, int]) -> \
        tuple[np.ndarray, np.ndarray, tuple[int, int], tuple[int, int]]:
    for _ in range(i):
        headB = headA[0] + move[d][1], headA[1] + move[d][0]
        tailB = tailMove(headB, tailA)
        head[headB] = 1
        tail[tailB] = 1
        headA = headB
        tailA = tailB
    return head, tail, headB, tailB


def ropeMove(head: np.ndarray, tail: np.ndarray, d: str, i: int, rope: list[tuple[int, int]]) -> \
        tuple[np.ndarray, np.ndarray, list[tuple[int, int]]]:
    x, y = move[d]
    for _ in range(i):
        for j, r in enumerate(rope):
            if j == 0:
                headB = r[0] + y, r[1] + x
                rope[0] = headB
                continue
            rope[j] = tailMove(rope[j - 1], r)
        head[rope[0]] = 1
        tail[rope[-1]] = 1
    return head, tail, rope


def followInstructionsPartOne(directions: list, minX: int, minY: int, maxX: int, maxY: int) -> \
        tuple[np.ndarray, np.ndarray]:
    head = np.zeros((maxY - minY + 1, maxX - minX + 1))
    tail = np.zeros((maxY - minY + 1, maxX - minX + 1))

    headA = minY + 1, - minX + 1
    tailA = headA
    head[headA] = 1
    tail[headA] = 1

    for d, i in directions:
        head, tail, headB, tailB = headMove(head, tail, d, i, headA, tailA)
        headA, tailA = headB, tailB
    return head, tail


def followInstructionsPartTwo(directions: list, minX: int, minY: int, maxX: int, maxY: int) -> \
        tuple[np.ndarray, np.ndarray]:
    head = np.zeros((maxY - minY + 1, maxX - minX + 1))
    tail = np.zeros((maxY - minY + 1, maxX - minX + 1))

    rope = [(minY - 1, - minX + 1)] * 10
    head[rope[0]] = 1
    tail[rope[-1]] = 1

    for d, i in directions:
        head, tail, rope = ropeMove(head, tail, d, i, rope)
    return head, tail


directions, minX, minY, maxX, maxY = loadData()
head, tail = followInstructionsPartOne(directions, minX, minY, maxX, maxY)

print(f"{tail.sum():.0f}")

directions, minX, minY, maxX, maxY = loadData()
head, tail = followInstructionsPartTwo(directions, minX, minY, maxX, maxY)

print(f"{tail.sum():.0f}")
