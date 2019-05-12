R, G, B, N = map(int, input().split())
# R, G, B, N = 1, 2, 3, 4
# R, G, B, N = 13, 1, 4, 3000


def count_r_ball_patterns(R, N_a):
    return 1 if N_a % R == 0 else 0


def count_rg_ball_patterns(R, G, B, N_b):
    max_g = N_b // G
    result = 0
    for g in range(max_g + 1):
        result = result + count_r_ball_patterns(R, N_b - G * g)
    return result


def count_rgb_ball_patterns(R, G, B, N):
    # count (r, g, b) satisties R * r + G * g + B * b = N
    R, G, B = sorted([R, G, B])
    max_b = N // B
    result = 0
    for b in range(max_b + 1):
        result = result + count_rg_ball_patterns(R, G, B, N - B * b)
    return result


if __name__ == "__main__":
    print(count_rgb_ball_patterns(R, G, B, N))
