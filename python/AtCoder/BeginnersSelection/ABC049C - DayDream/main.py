# -*- coding: utf-8 -*-
# S = input()

S = "dreameraser"

T = (S.replace("eraser", "")
        .replace("dreameraser", "")
        .replace("erase", "")
        .replace("dreamer", "")
        .replace("dream", ""))

if(len(T) == 0):
    print("YES")
else:
    print("NO")

