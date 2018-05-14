# -*- coding: utf-8 -*-

N = int(input())
numbers = map(int, input().split())


def countSubZeroRange(numbers):
    counter = 0
    for i in range(1, N + 1):  # i : 長さ
        for j in range(N - i + 1):
            if sum(numbers[j:j + i]) == 0:
                counter += 1
    return counter


print(countSubZeroRange(list(numbers)))
