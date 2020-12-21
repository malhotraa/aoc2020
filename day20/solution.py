from collections import defaultdict
import numpy as np
import re
import sys

np.set_printoptions(threshold=sys.maxsize)

opposite_orientation = {
    'top': 'bottom',
    'bottom': 'top',
    'left': 'right',
    'right': 'left',
}

class Tile:
    def __init__(self, tile_str):
        lines = tile_str.split('\n')
        self.tile_id = int(re.match(r"Tile (\d+):", lines[0]).group(1))
        layout = lines[1:]
        self.layout = np.zeros((len(layout), len(layout[0])), dtype=np.int32)
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == '#':
                    self.layout[i][j] = 1
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

    def rot90(self, k = 1):
        self.layout = np.rot90(self.layout, k)

    def fliplr(self):
        self.layout = np.fliplr(self.layout)

    def flipud(self):
        self.layout = np.flipud(self.layout)

    def __repr__(self):
        return "Tile {}:\n{}\nup:{} down:{} left:{} right:{}".format(self.tile_id, self.layout, self.top, self.bottom, self.left, self.right)

    def edges(self):
        return {
            'top': self.layout[0,:],
            'bottom': self.layout[-1,:],
            'left': self.layout[:,0],
            'right': self.layout[:,-1]
        }

    def common_edge(self, o_tile):
        for o1, e1 in self.edges().items():
            for o2, e2 in o_tile.edges().items():
                if (e1 == e2).all() or (e1 == np.flip(e2, 0)).all():
                    return o1, e1
        raise Exception("No commond edge between {} and {}".format(self.tile_id, o_tile.tile_id))

    def flip_to_orientation(self, edge, orientation):
        assert orientation in ['top', 'bottom', 'left', 'right']

        if (self.edges()[orientation] == edge).all():
            return

        done = False
        for r in [1, 2, 3, 4]:
            self.rot90(r)
            if (self.edges()[orientation] == edge).all():
                    done = True
                    break
            self.rot90(4-r)
        if done:
            return

        for r in [1, 2, 3, 4]:
            for flip in ['fliplr', 'flipud']:
                self.rot90(r)
                getattr(self, flip)()

                if (self.edges()[orientation] == edge).all():
                    done = True
                    break

                getattr(self, flip)()
                self.rot90(4-r)
            if done:
                break
        assert done == True

with open("input.txt") as f:
    tiles = f.read().split('\n\n')
    tiles = list(map(lambda x: Tile(x), tiles))
    tiles = dict([(tile.tile_id, tile) for tile in tiles])

def create_neigbhor_map(tiles):
    neighbor_map = defaultdict(set)
    for _, tile1 in tiles.items():
        for _, tile2 in tiles.items():
            if tile1.tile_id == tile2.tile_id:
                continue
            for _, e1 in tile1.edges().items():
                for _, e2 in tile2.edges().items():
                    if (e1 == e2).all() or (e1 == np.flip(e2, 0)).all():
                        neighbor_map[tile1.tile_id].add(tile2.tile_id)
                        neighbor_map[tile2.tile_id].add(tile1.tile_id)
    return neighbor_map

def create_image(neighbor_map, tiles):
    corners = list(filter(lambda x: len(x[1]) == 2, neighbor_map.items()))
    corner_id = corners[0][0]

    placed = set()
    unplaced = [corner_id]
    num_placed = 0
    while len(unplaced) > 0:
        tile_id = unplaced.pop(0)
        if tile_id in placed:
            continue
        placed.add(tile_id)
        neighbors = []
        for n in neighbor_map[tile_id]:
            if n not in placed:
                neighbors.append(n)

        assert len(neighbors) <= 2, "A tile cannot have more than 2 unplaced neighbors"
    
        for n in neighbors:
            orientation, edge = tiles[tile_id].common_edge(tiles[n])
            tiles[n].flip_to_orientation(edge, opposite_orientation[orientation])
            setattr(tiles[tile_id], orientation, n)
            setattr(tiles[n], opposite_orientation[orientation], tile_id)
        unplaced.extend(neighbors)
    
    top_left_id = None
    for tile_id, tile in tiles.items():
        if tile.top is None and tile.left is None:
            top_left_id = tile_id

    tile_len = 8
    image = np.full((12 * tile_len, 12 * tile_len), -1, dtype=np.int32)
    row = top_left_id
    x, y = 0, 0
    while row is not None:
        curr = row
        y = 0
        while curr is not None:
            image[x*tile_len:x*tile_len+tile_len, y*tile_len:y*tile_len+tile_len] = tiles[curr].layout[1:-1, 1:-1]
            curr = tiles[curr].right
            y += 1
        row = tiles[row].bottom
        x += 1

    assert (image != -1).all()
    return image

def build_kernel():
    kernel_str = """..................#.
#....##....##....###
.#..#..#..#..#..#..."""
    return np.array([[ch == '#' for ch in row] for row in kernel_str.split('\n')], dtype=np.int32)

def part1(tiles):
    neighbor_map = create_neigbhor_map(tiles)
    product = 1
    for tile_id, neighbors in neighbor_map.items():
        if len(neighbors) == 2:
            product *= tile_id
    return product

def convovle2d(image, kernel):
    output = image.copy()
    k_h, k_w = kernel.shape
    count = 0
    for i in range(image.shape[0] - k_h):
        for j in range(image.shape[1] - k_w):
            if np.equal(image[i:i+k_h, j:j+k_w] & kernel, kernel).all():
                count += 1
                output[i:i+k_h, j:j+k_w] &= ~kernel
    return output, count

def part2(tiles):
    neighbor_map = create_neigbhor_map(tiles)
    image = create_image(neighbor_map, tiles)

    kernel = build_kernel()
    out, cnt = convovle2d(image, kernel)
    for r in range(4):
        image = np.rot90(image)
        out, cnt = convovle2d(image, kernel)
        if cnt > 0:
            return np.sum(out)
    
    for r in range(4):
        image = np.rot90(image, r)
        image = np.flipud(image)
        out, cnt = convovle2d(image, kernel)
        if cnt > 0:
            return np.sum(out)

        image = np.flipud(image)
        image = np.rot90(image, 4-r)


print('part1:', part1(tiles))
print('part2:', part2(tiles))

