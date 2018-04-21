# -*- coding: utf-8 -*-
A = int(input())  # Number of 500 yen coins
B = int(input())  # Number of 100 yen coins
C = int(input())  # Number of 50 yen coins
X = int(input())  # Target Value


def calcSubPaymentPairs(B, C, X):
    n = X // 50
    counter = 0
    for b in range(B + 1):
        c = n - 2 * b
        if c < 0:
            break
        elif c <= C:
            counter += 1
    return counter


def calcPaymentPairs(A, B, C, X):
    counter = 0
    for a in range(A + 1):
        Y = X - 500 * a
        counter += calcSubPaymentPairs(B, C, Y)
    return counter


print(calcPaymentPairs(A, B, C, X))
