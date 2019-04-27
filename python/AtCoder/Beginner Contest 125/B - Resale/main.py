N = map(int, input().split())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))
# N = 3
# values = [10, 2, 5]
# costs = [6, 3, 4]
# N = 4
# values = [13, 21, 6, 19]
# costs = [11, 30, 6, 15]
# N = 1
# values = [1,]
# costs = [50,]


def calculate_maximum_gain(values, costs):
    gain = 0
    for value, cost in zip(values, costs):
        if value - cost > 0:
            gain = gain + value - cost
    
    return gain


print(calculate_maximum_gain(values, costs))
