import numpy as np


def MinToMax(maxx, x):
    x = list(x)
    ans = [[maxx - e] for e in x]
    return np.array(ans)


def MidToMax(betsx, x):
    x = list(x)
    h = [abs(e - betsx) for e in x]
    M = max(h)
    if M == 0:
        M = 1
    ans = [[1 - e / M] for e in h]
    return np.array(ans)


def RegToMax(lowx, highx, x):
    x = list(x)
    M = max(lowx - min(x), max(x) - highx)
    if M == 0:
        M = 1
    ans = []
    for i in range(len(x)):
        if x[i] < lowx:
            ans.append([(1 - (lowx - x[i]) / M)])
        elif x[i] > highx:
            ans.append([(1 - (x[i] - highx) / M)])
        else:
            ans.append([1])
    return np.array(ans)
