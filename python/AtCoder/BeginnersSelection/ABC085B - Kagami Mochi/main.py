# -*- coding: utf-8 -*-
N = int(input())
l = [input() for _ in range(N)]


print(len(set(sorted(l))))
