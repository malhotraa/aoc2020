with open('input.txt') as f:
    lines = f.read().split('\n')

def normalize_orientation(theta):
    while theta <= -180:
        theta += 360
    while theta > 180:
        theta -= 360 
    return theta

def part1_manhattan(lines):
    dir_to_xy = {
        'N': (0, -1),
        'S': (0, 1),
        'E': (1, 0),
        'W': (-1, 0),
    }
    orientation_to_xy = {
        0: (1, 0),
        90: (0, -1),
        180: (-1, 0),
        -90: (0, 1),
    }
    rotation_to_theta = {
        'L': 1,
        'R': -1,
    }
    x, y = 0, 0
    theta = 0
    for line in lines:
        action = line[0]
        value = int(line[1:])
        if action == 'F':
            mul_x, mul_y = orientation_to_xy[theta]
            x += mul_x * value
            y += mul_y * value
        elif action in set(['N', 'S', 'E', 'W']):
            mul_x, mul_y = dir_to_xy[action]
            x += mul_x * value
            y += mul_y * value
        elif action in set(['L', 'R']):
            theta += (rotation_to_theta[action] * value)
            theta = normalize_orientation(theta)
    return abs(x) + abs(y)

def rotate_xy(x, y, theta):
    assert -270 <= theta <= 270
    if theta == 90 or theta == -270:
        return y, -x
    elif theta == 180 or theta == -180:
        return -x, -y
    elif theta == 270 or theta == -90:
        return -y, x

def part2_manhattan(lines):
    dir_to_xy = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0),
    }
    rotation_to_theta = {
        'L': -1,
        'R': 1,
    }
    x, y = 0, 0
    way_x, way_y = 10, 1
    for line in lines:
        action = line[0]
        value = int(line[1:])
        if action == 'F':
            x += way_x * value
            y += way_y * value
        elif action in set(['N', 'S', 'E', 'W']):
            mul_x, mul_y = dir_to_xy[action]
            way_x += mul_x * value
            way_y += mul_y * value
        elif action in set(['L', 'R']):
            way_x, way_y = rotate_xy(way_x, way_y, rotation_to_theta[action] * value)
    return abs(x) + abs(y)

print('part1 manhattan: ', part1_manhattan(lines))
print('part2 manhattan: ', part2_manhattan(lines))