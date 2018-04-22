# -*- coding: utf-8 -*-

N = int(input())
transitions = [input().split() for _ in range(N)]


def is_reachable(start, end):
    t_start = int(start[0])
    x_start = int(start[1])
    y_start = int(start[2])

    t_end = int(end[0])
    x_end = int(end[1])
    y_end = int(end[2])

    dt = t_end - t_start
    dx = x_end - x_start
    dy = y_end - y_start

    if(dt < dx + dy):
        return False
    else:
        return(dt + dx + dy) % 2 == 0


def is_travelable(transitions):
    start = ['0', '0', '0']
    end = transitions[0]
    if not is_reachable(start, end):
        return False
    for i in range(1, N):
        start = end
        end = transitions[i]
        if not is_reachable(start, end):
            return False
    return True


if is_travelable(transitions):
    print("Yes")
else:
    print("No")
