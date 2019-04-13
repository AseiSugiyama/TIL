tiles = list(map(int, input()))
# inputs = "10010010"
# tiles = list(map(int, inputs))


def count_repaint_tiles(tiles):
    if len(tiles) == 0:
        return 0
    counts = 0
    color = tiles[0]
    for tile in tiles[1:]:
        if tile == color:
            counts = counts + 1
        color = 1 - color
    return counts


print(count_repaint_tiles(tiles))
