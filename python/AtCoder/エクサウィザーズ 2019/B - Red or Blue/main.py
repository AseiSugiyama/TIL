N = int(input())
transitions = [input().split() for _ in range(N)]
# N = 4
# transitions = [char for char in "RRBR"]


def is_more_reds_than_blues(transitions):
    reds = len([hat for hat in transitions if hat == "R"])
    blues = len(transitions) - reds
    return reds > blues


def print_more_reds_than_blues(transitions):
    if (is_more_reds_than_blues(transitions)):
        print("Yes")
    else:
        print("No")


print_more_reds_than_blues(transitions)
