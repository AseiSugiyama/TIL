# -*- coding: utf-8 -*-
s = input()
K = int(input())


def substring(s, K):
    substrings = []
    length = len(s)
    for i in range(length):
        for j in range(1, K+1):
            if i + j > length:
                break
            substrings.append(s[i:i + j])
    unique_substrings = list(set(substrings))
    unique_substrings.sort()
    return unique_substrings[K - 1]


print(substring(s, K))
