N = int(input())
heights = list(map(int, input().split()))


def can_get_ocean_view(subheights):
    return 1 if max(subheights) == subheights[-1] else 0


def count_hotels_with_ocean_view(heights):
    hotels_with_ocean_view = [can_get_ocean_view(heights[:i]) for i in range(1, len(heights)+1)]
    return sum(hotels_with_ocean_view)


print(count_hotels_with_ocean_view(heights))
