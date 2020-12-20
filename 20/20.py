#!/usr/bin/env python3

import collections
import math
import sys

import numpy as np

SIZE=10

def parse_line(text):
    return list(map(lambda c: 1 if c == '#' else 0, text))

def parse_tile(text):
    lines = text.split('\n')
    tile_id = int((lines[0].split(' '))[1][:-1])
    cells = np.array(list(map(parse_line, lines[1:])))
    return (tile_id, cells)

with open(sys.argv[1]) as f:
    tiles = dict(map(parse_tile, f.read().strip().split('\n\n')))

first_tile_id, first_cells = list(tiles.items())[0]

tile_locations = {(0, 0): first_cells}
tile_id_locations = {(0, 0): first_tile_id}

def gen_rotations(cells):
    for i in range(4):
        yield cells
        yield np.fliplr(cells)
        cells = np.rot90(cells)

def check_direction(tiles, current_tile, seen, step, old_edge_fn, new_edge_fn):
    next_loc = (current_loc[0] + step[0], current_loc[1] + step[1])
    edge = old_edge_fn(current_tile)

    for tid, cells in tiles.items():
        if tid in seen:
            continue
        for new_cells in gen_rotations(cells):
            new_edge = new_edge_fn(new_cells)
            if np.all(edge == new_edge):
                tile_locations[next_loc] = new_cells
                tile_id_locations[next_loc] = tid
                seen.add(tid)
                todo.append(next_loc)

seen = {first_tile_id}
todo = [(0, 0)]

while todo:
    current_loc = todo.pop()
    current_tile = tile_locations[current_loc]

    check_direction(tiles, current_tile, seen, (0, 1), lambda c: c[:,SIZE-1], lambda c: c[:,0])
    check_direction(tiles, current_tile, seen, (-1, 0), lambda c: c[0,:], lambda c: c[SIZE-1,:])
    check_direction(tiles, current_tile, seen, (0, -1), lambda c: c[:,0], lambda c: c[:,SIZE-1])
    check_direction(tiles, current_tile, seen, (1, 0), lambda c: c[SIZE-1,:], lambda c: c[0,:])

ys = list(map(lambda l: l[0], tile_locations.keys()))
xs = list(map(lambda l: l[1], tile_locations.keys()))

min_y, max_y = min(ys), max(ys)
min_x, max_x = min(xs), max(xs)

print(math.prod(map(lambda l: tile_id_locations[l], [(min_y, min_x), (min_y, max_x), (max_y, min_x), (max_y, max_x)])))

without_borders = dict(map(lambda p: ((p[0][0] - min_y, p[0][1] - min_x), p[1][1:-1,1:-1]), tile_locations.items()))

y_range = (max_y - min_y + 1)
image_4d = np.zeros((y_range, y_range, SIZE-2, SIZE-2))
for loc, small_image_2d in without_borders.items():
    image_4d[loc[0],loc[1],:,:] = small_image_2d

image_2d = image_4d.transpose((0,2,1,3)).reshape((y_range * (SIZE-2), y_range * (SIZE-2)))

monster_string = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

monster = np.array(list(map(parse_line, monster_string.split('\n'))))
monster_sum = np.sum(monster)

def find_monster(image):
    monster_count = 0
    for y0 in range(image.shape[0]-monster.shape[0]+1):
        for x0 in range(image.shape[1]-monster.shape[1]+1):
            section = image[y0:y0+monster.shape[0],x0:x0+monster.shape[1]]
            overlap = section * monster
            if np.all(overlap == monster):
                monster_count += 1

    return monster_count

print(list(map(lambda mc: np.sum(image_2d) - mc * np.sum(monster), (filter(None, (map(find_monster, gen_rotations(image_2d))))))))
