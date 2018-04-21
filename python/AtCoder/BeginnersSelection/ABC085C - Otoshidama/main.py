# -*- coding: utf-8 -*-
N, Y = map(int, input().split())


def calcBillsPair(N, Y):
    n = Y // 1000
    for a in range(N + 1):
        if n - 10 * a < 0:
            break
        b, c = calcSubBillsPair(N - a, n - 10 * a)
        if b != -1 and c != -1:
            return (a, b, c)
    return (-1, -1, -1)


def calcSubBillsPair(N, n):
    for b in range(N + 1):
        c = N - b
        if c < 0:
            break
        if 5 * b + c == n:
            return (b, c)
    return(-1, -1)


a, b, c = calcBillsPair(N, Y)
print("{} {} {}".format(a, b, c))
