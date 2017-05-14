import math
import random
import numpy


# Collatz conjecture problem
def cc(n):
    i = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            i += 1
        else:
            n = 3 * n + 1
            i += 1
    return i


print(cc(100))


# Closest pair problem

def generaterandom(n):
    x = [x for x in random.sample(range(n), n)]
    y = [y for y in random.sample(range(n), n)]
    return list(zip(x, y))


a = generaterandom(100)

print(a)


def euld(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5


def brute(x):
    mi = euld(x[0], x[1])
    p1 = x[0]
    p2 = x[1]
    if len(x) == 2:
        return p1, p2, mi
    else:
        for i in range(len(x) - 1):
            for j in range(i + 1, len(x)):
                if i != 0 and j != 1:
                    d = euld(x[i], x[j])
                    if d < mi:
                        mi = d
                        p1, p2 = x[i], x[j]
        return p1, p2, mi


def strip(lisx, lisy, d, p3x, p3y):
    lenx = len(lisx)
    median = int(lenx / 2)
    midpoint = lisx[median][0]
    stripy = [x for x in lisy if midpoint - d <= x[0] <= midpoint + d]
    mind = d
    for i in range(len(stripy) - 1):
        for j in range(i + 1, min(len(stripy), i + 7)):
            distance = euld(stripy[i], stripy[j])
            if distance < mind:
                mind = distance
                p3x = stripy[i]
                p3y = stripy[j]
    return p3x, p3y, mind


def dvc(lisx, lisy):
    if len(lisx) <= 3:
        return brute(lisx)
    else:
        median = int(len(lisx) / 2)
        p1x = lisx[:median]
        p2x = lisx[median:]
        midpoint = lisx[median][0]
        p1y = []
        p2y = []
        for i in lisy:
            if i[0] < midpoint:
                p1y.append(i)
            else:
                p2y.append(i)
        p11, p12, d1 = dvc(p1x, p1y)
        p21, p22, d2 = dvc(p2x, p2y)
        d = min(d1, d2)
        if d == d1:
            p31, p32, d3 = strip(lisx, lisy, d, p1x, p1y)
        else:
            p31, p32, d3 = strip(lisx, lisy, d, p2x, p2y)
        # return the minimum of the strip
        if d3 < d:
            return p31, p32, d3
        elif d1 == 1:
            return p11, p12, d1
        else:
            return p21, p22, d2


ax = sorted(a, key=lambda x: x[0])
ay = sorted(a, key=lambda x: x[1])
p1, p2, mi = dvc(ax, ay)
print('\n')
print(p1, p2, mi)
'test'
