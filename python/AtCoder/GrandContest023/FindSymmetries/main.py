# -*- coding: utf-8 -*-
N = int(input())
S = [str(input()) for _ in range(N)]


def isGoodTable(table, A, B):
    for i in range(N):
        for j in range(i, N):
            if table[i][j] != table[j][i]:
                return False
    return True


def shiftTable(table, A, B):
    shifted = []
    for i in range(N):
        shifted.append([])
        for j in range(N):
            shifted[i].append(table[(i + A) % N][(j + B) % N])
    return shifted


def countGoodShift(table):
    count = 0
    for a in range(N):
        shifted = shiftTable(table, a, 0)
        if isGoodTable(shifted, a, 0):
            count += 1
    return count * N


print(countGoodShift(S))
