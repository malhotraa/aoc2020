with open('input.txt') as f:
    lines = f.read().split("\n")

def num_trees_for_slope(lines, slope_x, slope_y):
    x, y = 0, 0
    limit_x, limit_y = len(lines[0]), len(lines)
    num_trees = 0
    while y < limit_y:
        if lines[y][x] == '#':
            num_trees += 1
        x = (x + slope_x) % limit_x
        y = y + slope_y
    return num_trees


print(num_trees_for_slope(lines, 1, 1) *
        num_trees_for_slope(lines, 3, 1) *
        num_trees_for_slope(lines, 5, 1) *
        num_trees_for_slope(lines, 7, 1) *
        num_trees_for_slope(lines, 1, 2))
