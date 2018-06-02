# -*- coding: utf-8 -*-
N = int(input())
S = input()


def calcCountUnion(X, Y):
    counter = 0
    for key in X.keys():
        if key in Y.keys():
            counter += 1
    return counter


def str2dict(S):
    X = {}
    Y = {}
    for a in S:
        X[a] = X[a] + 1 if (a in X.keys()) else 1
    return X, Y


def calcMaxCutCount(S):
    X, Y = str2dict(S)
    maxCutCount = 0
    for a in S:
        X[a] = X[a] - 1
        Y[a] = X[a] + 1 if (a in X.keys()) else 1
        if X[a] <= 0:
            X.pop(a)
        tmp = calcCountUnion(X, Y)
        maxCutCount = max((tmp, maxCutCount))
    return maxCutCount


print(calcMaxCutCount(S))
