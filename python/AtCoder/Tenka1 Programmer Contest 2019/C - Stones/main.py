import numpy as np
N = int(input())
stones = np.array([0 if stone == "." else 1 for stone in input()])
# stones = np.array([0 if stone == "." else 1 for stone in ".#....."])


def count_painted_stones_by_cumsum(stones, length):
    left_black_stones = np.roll(np.cumsum(stones), 1)
    left_black_stones[0] = 0
    right_white_stones = np.roll(np.cumsum(1 - stones[::-1]), 1)
    right_white_stones[0] = 0

    return np.min(left_black_stones + right_white_stones[::-1])


print(count_painted_stones_by_cumsum(stones, len(stones)))
