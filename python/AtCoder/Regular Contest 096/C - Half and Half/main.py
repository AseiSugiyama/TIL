# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)

A, B, C, X, Y = map(int, input().split())
# A, B, C, X, Y = 1500, 2000, 1600, 3, 2


def calcBestPrice(A, B, C, X, Y):

    if(X > 0 and Y > 0):
        if(A + B > 2 * C):
            return 2 * C + calcBestPrice(A, B, C, X - 1, Y - 1)
        elif(A > 2 * C):
            return 2 * C * X + calcBestPrice(A, B, C, 0, Y)
        elif(B > 2 * C):
            return 2 * C * Y + calcBestPrice(A, B, C, X, 0)
        else:
            return A * X + B * Y
    elif(X == 0):
        if(B > 2 * C):
            return 2 * C * Y
        else:
            return B * Y
    elif(Y == 0):
        if(A > 2 * C):
            return 2 * C * X
        else:
            return A * X


print(calcBestPrice(A, B, C, X, Y))
