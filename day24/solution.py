import copy

with open('input.txt') as f:
    lines = f.read().split('\n')

class Hex:
    NORTH_SOUTH_OFFSET = 17 # Random value to keep all ops in integer domain instead of using sqrt(3)
    DIRECTION_TO_OFFSET = {
        'e': (2, 0),
        'w': (-2, 0),
        'ne': (1, NORTH_SOUTH_OFFSET),
        'sw': (-1, -NORTH_SOUTH_OFFSET),
        'nw': (-1, NORTH_SOUTH_OFFSET),
        'se': (1, -NORTH_SOUTH_OFFSET),
    }
    def __init__(self, e, n):
        self.e = e
        self.n = n

    @staticmethod
    def create_from_directions(dirs):
        h = Hex(0, 0)
        i = 0
        while i < len(dirs):
            if i+2 <= len(dirs) and dirs[i:i+2] in ['ne', 'nw', 'se', 'sw']:
                h.move(dirs[i:i+2])
                i+=2
            elif dirs[i] in ['e', 'w']:
                h.move(dirs[i])
                i+=1
            else:
                raise Exception("Unknown direction in input {} at idx {}".format(line, i))
        return h

    def move(self, dir_):
        offset = self.DIRECTION_TO_OFFSET[dir_]
        self.e += offset[0]
        self.n += offset[1]
    
    def neighbors(self):
        n = []
        for dx, dy in self.DIRECTION_TO_OFFSET.values():
            n.append(Hex(self.e + dx, self.n + dy))
        return n

    def __repr__(self):
        return "Hex({},{})".format(self.e, self.n)
    
    def __eq__(self, other):
        return self.e == other.e and self.n == other.n
    
    def __hash__(self):
        return hash(self.e) ^ hash(self.n)

def exec_input(lines):
    flipped_once = set()
    for line in lines:
        h = Hex.create_from_directions(line)
        if h in flipped_once:
            flipped_once.remove(h)
        else:
            flipped_once.add(h)
    return flipped_once

def part1(lines):
    return len(exec_input(lines))

def part2(lines):
    black_tiles = copy.copy(exec_input(lines))
    for _ in range(100):
        new_black_tiles = set()
        for tile in black_tiles:
            neighbors = tile.neighbors()
            num_black = len(list(filter(lambda x: x in black_tiles, neighbors)))
            if num_black == 0 or num_black > 2:
                pass # This tile flipped to white
            else:
                new_black_tiles.add(tile)
            
            for n in neighbors:
                if n in black_tiles: # skip if tile is black
                    continue
                num_black = len(list(filter(lambda x: x in black_tiles, n.neighbors())))
                if num_black == 2:
                    new_black_tiles.add(n)

        black_tiles = new_black_tiles

    return len(black_tiles)
    
            
print('part1:', part1(lines))
print('part2:', part2(lines))