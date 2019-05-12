N = int(input())
S = [input() for _ in range(N)]
# S = ["ABCA", "XBAZ", "BAD"]
# S = ["BEWPVCRWH", "ZZNQYIJX", "BAVREA", "PA", "HJMYITEOX", "BCJHMRMNK", "BP", "QVFABZ", "PRGKSPUNA"]
# S = ["RABYBBE","JOZ","BMHQUVA","BPA","ISU","MCMABAOBHZ","SZMEHMA"]


def calc_maximum_AB_sub_string(S):
    base_AB_counts = map(lambda x : x.count("AB"), S)
    base = sum(base_AB_counts)

    clipped = list(map(lambda x: x[0] + x[-1], S))
    bonus1 = len(list(filter(lambda x: x == 'BA', clipped)))
    filtered = list(filter(lambda x: x != 'BA', clipped))
    bonus2 = sum(map(lambda x: 1 if x[1] == 'A' else 0, filtered))
    bonus3 = sum(map(lambda x: 1 if x[0] == 'B' else 0, filtered))

    return base + max(bonus1 - 1, 0) + min(bonus2, bonus3) + (1 if bonus2 != bonus3 else 0)


if __name__ == "__main__":
    print(calc_maximum_AB_sub_string(S))
