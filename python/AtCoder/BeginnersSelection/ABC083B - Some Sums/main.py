# -*- coding: utf-8 -*-
N, A, B = map(int, input().split())


def sum_base_10(n):
    base_10 = str(n)
    sum = 0
    for char in base_10:
        sum += int(char)
    return sum


def SomeSum(N, A, B):
    result = 0
    for i in range(N + 1):
        sum_10 = sum_base_10(i)
        if A <= sum_10 and sum_10 <= B:
            result += i
    return result


print(SomeSum(N, A, B))
