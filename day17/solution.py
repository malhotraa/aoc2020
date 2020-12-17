import numpy as np

with open('input.txt') as f:
    lines = f.read().split('\n')

def num_neighbors_active(space, z, x, y):
    num_active = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                x_, y_, z_ = x+dx, y+dy, z+dz
                if x_ == x and y_ == y and z_ == z:
                    continue
                if 0 <= z_ < space.shape[0] and 0 <= x_ < space.shape[1] and 0 <= y_ < space.shape[2]:
                    num_active += space[z_][x_][y_]
    return num_active

def run_sim(space):
    space_ = space.copy()
    for z in range(space.shape[0]):
        for x in range(space.shape[1]):
            for y in range(space.shape[2]):
                active_neighbors = num_neighbors_active(space, z, x, y)
                if space[z][x][y] == 1 and active_neighbors not in [2, 3]:
                    space_[z][x][y] = 0
                elif space[z][x][y] == 0 and active_neighbors == 3:
                    space_[z][x][y] = 1
    return space_

def num_active_after_six_cycles(lines):
    space = np.zeros((12, len(lines) * 4, len(lines[0]) * 4), dtype=np.int)
    
    z = space.shape[0] // 2
    offset_x = (space.shape[1] // 2) - (len(lines) // 2)
    offset_y = (space.shape[2] // 2) - (len(lines[0]) // 2)
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == '#':
                space[z][x+offset_x][y+offset_y] = 1

    for n in range(6):
        space = run_sim(space)
    
    return np.sum(space)

print('num_active_after_six_cycles: ', num_active_after_six_cycles(lines))