import numpy as np


def loadData():
    with open('aoc10.txt', 'r') as f:
        data = []
        for line in f.readlines():
            signal = line.strip().split(' ')
            if 'noop' in signal:
                data.append(signal)
            elif 'addx' in signal:
                data.append([signal[0], int(signal[1])])
    return data


def processSignals(signals: list) -> list[int]:
    register = [1]
    for signal in signals:
        n = {'noop': 1, 'addx': 2}[signal[0]]
        for _ in range(n):
            register.append(register[-1])
        if signal[0] == 'addx':
            register[-1] += signal[1]
    return register


def partOne(register: list[int]) -> int:
    total = 0
    for i in range(20, len(register), 40):
        total += register[i - 1] * i
    return total


def partTwo(register: list[int]):
    crt = np.zeros(240)
    for pixel in range(240):
        x = register[pixel - 1]
        if x - 1 <= pixel % 40 - 1 <= x + 1:
            crt[pixel] = 1
    return crt


def displayCRT(crt):
    for j, pix in enumerate(crt):
        print('\N{FULL BLOCK}' if pix else ' ', end='' if (j + 1) % 40 else '\n')


signals = loadData()
register = processSignals(signals)
print(partOne(register))
crt = partTwo(register)
displayCRT(crt)
