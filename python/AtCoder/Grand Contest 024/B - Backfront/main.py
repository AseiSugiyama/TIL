# -*- coding: utf-8 -*-
N = int(input())
P = [int(input()) for _ in range(N)]


def calcBackFront(P):
    N = len(P)
    counter = 0
    tmp = P[0]
    for i in range(1, N):
        if P[i] < tmp:
            continue
        elif(tmp + 1 == P[i]):
            counter += 1
        else:
            counter = 0
            tmp = P[i]
    return N - counter


print(calcBackFront(P))
