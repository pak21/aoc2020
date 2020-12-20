#!/usr/bin/env python3

import collections
import math
import sys

import numpy as np

SIZE=10

def parse_line(text):
    return list(map(lambda c: c == '#', text))

def parse_tile(text):
    lines = text.split('\n')
    tile_id = int((lines[0].split(' '))[1][:-1])
    cells = np.array(list(map(parse_line, lines[1:])))
    return (tile_id, cells)

with open(sys.argv[1]) as f:
    tiles = dict(map(parse_tile, f.read().strip().split('\n\n')))

first_tile_id, first_cells = list(tiles.items())[0]

tile_locations = {
    (0, 0): first_cells
}

tile_id_locations = {(0, 0): first_tile_id}

def gen_rotations(cells):
    for i in range(4):
        yield cells
        yield np.fliplr(cells)
        cells = np.rot90(cells)

seen = {first_tile_id}
todo = [(0, 0)]

while todo:
    current_loc = todo.pop()
    current_tile = tile_locations[current_loc]

    # Right
    next_loc = (current_loc[0], current_loc[1] + 1)
    edge = current_tile[:,SIZE-1]

    for tid, cells in tiles.items():
        if tid in seen:
            continue
        for new_cells in gen_rotations(cells):
            new_edge = new_cells[:,0]
            if np.all(edge == new_edge):
                tile_locations[next_loc] = new_cells
                tile_id_locations[next_loc] = tid
                seen.add(tid)
                todo.append(next_loc)

    # Up 
    next_loc = (current_loc[0] - 1, current_loc[1])
    edge = current_tile[0,:]

    for tid, cells in tiles.items():
        if tid in seen:
            continue
        for new_cells in gen_rotations(cells):
            new_edge = new_cells[SIZE-1,:]
            if np.all(edge == new_edge):
                tile_locations[next_loc] = new_cells
                tile_id_locations[next_loc] = tid
                seen.add(tid)
                todo.append(next_loc)

    # Left
    next_loc = (current_loc[0], current_loc[1] - 1)
    edge = current_tile[:,0]

    for tid, cells in tiles.items():
        if tid in seen:
            continue
        for new_cells in gen_rotations(cells):
            new_edge = new_cells[:,SIZE-1]
            if np.all(edge == new_edge):
                tile_locations[next_loc] = new_cells
                tile_id_locations[next_loc] = tid
                seen.add(tid)
                todo.append(next_loc)

    # Down
    next_loc = (current_loc[0] + 1, current_loc[1])
    edge = current_tile[SIZE-1,:]

    for tid, cells in tiles.items():
        if tid in seen:
            continue
        for new_cells in gen_rotations(cells):
            new_edge = new_cells[0,:]
            if np.all(edge == new_edge):
                tile_locations[next_loc] = new_cells
                tile_id_locations[next_loc] = tid
                seen.add(tid)
                todo.append(next_loc)

ys = list(map(lambda l: l[0], tile_locations.keys()))
xs = list(map(lambda l: l[1], tile_locations.keys()))

min_y, max_y = min(ys), max(ys)
min_x, max_x = min(xs), max(xs)

top_left = (min_y, min_x)
top_right = (min_y, max_x)
bottom_left = (max_y, min_x)
bottom_right = (max_y, max_x)

y_range = (max_y - min_y + 1)

corners = (top_left, top_right, bottom_left, bottom_right)
corner_ids = list(map(lambda l: tile_id_locations[l], corners))
print(math.prod(corner_ids))

def remove_borders(cells):
    return cells[1:SIZE-1,1:SIZE-1]

without_borders = dict(map(lambda p: ((p[0][0] - min_y, p[0][1] - min_x), remove_borders(p[1])), tile_locations.items()))

image_4d = np.zeros((y_range, y_range, SIZE-2, SIZE-2))
for loc, small_image_2d in without_borders.items():
    image_4d[loc[0],loc[1],:,:] = small_image_2d

image_2d = image_4d.transpose((0,2,1,3)).reshape((y_range * (SIZE-2), y_range * (SIZE-2)))

monster_string = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

monster = np.array(list(map(lambda l: list(map(lambda c: 1 if c == '#' else 0, l)), monster_string.split('\n'))))
monster_sum = np.sum(monster)

def find_monster(image):
    monster_count = 0
    for y0 in range(image.shape[0]-monster.shape[0]+1):
        for x0 in range(image.shape[1]-monster.shape[1]+1):
            section = image[y0:y0+monster.shape[0],x0:x0+monster.shape[1]]
            overlap = np.sum(section * monster)
            if overlap == monster_sum:
                monster_count += 1

    if monster_count > 0:
        roughness = np.sum(image) - monster_count * monster_sum
        print(roughness)

for foo in gen_rotations(image_2d):
    find_monster(foo)
