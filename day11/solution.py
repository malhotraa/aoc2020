with open('input.txt') as f:
    lines = f.read().split('\n')

def num_neighbors_occupied(grid, i, j):
    occupied = 0
    for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if 0 <= i+x < len(grid) and 0 <= j+y < len(grid[0]) and grid[i+x][j+y] == '#':
            occupied += 1
    return occupied

def num_neighbors_occupied_seen(grid, i, j):
    occupied = 0
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        x, y = i, j
        while 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]):
            if grid[x+dx][y+dy] == '#':
                occupied +=1
                break
            elif grid[x+dx][y+dy] == 'L':
                break
            x = x+dx
            y = y+dy
    return occupied

def num_seats_occupied_part1(grid):
    change = True
    while change:
        new_grid = []
        for i in range(len(grid)):
            new_row = []
            for j in range(len(grid[0])):
                num_occupied = num_neighbors_occupied(grid, i, j)
                if grid[i][j] == 'L' and num_occupied == 0:
                    new_row.append('#')
                elif grid[i][j] == '#' and num_occupied >= 4:
                    new_row.append('L')
                else:
                    new_row.append(grid[i][j])
            new_grid.append(''.join(new_row))
        
        change = any([grid[i] != new_grid[i] for i in range(len(grid))])
        grid = new_grid
    assert change is False

    total_occupied = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                total_occupied +=1

    return total_occupied

def num_seats_occupied_part2(grid):
    change = True
    while change:
        new_grid = []
        for i in range(len(grid)):
            new_row = []
            for j in range(len(grid[0])):
                num_occupied = num_neighbors_occupied_seen(grid, i, j)
                if grid[i][j] == 'L' and num_occupied == 0:
                    new_row.append('#')
                elif grid[i][j] == '#' and num_occupied >= 5:
                    new_row.append('L')
                else:
                    new_row.append(grid[i][j])
            new_grid.append(''.join(new_row))
        
        change = any([grid[i] != new_grid[i] for i in range(len(grid))])
        grid = new_grid
    assert change is False

    total_occupied = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                total_occupied +=1

    return total_occupied
print('num_seats_occupied_part1:', num_seats_occupied_part1(lines))
print('num_seats_occupied_part2:', num_seats_occupied_part2(lines))

