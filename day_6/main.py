"""https://adventofcode.com/2024/day/6"""

import pprint
from common_main_methods import read_text_file_lines

def count_guard_positions(input_filepath):
    map_grid = [list(row.strip()) for row in read_text_file_lines(input_filepath)]
    for row_idx, row in enumerate(map_grid):
        for col_idx, cell in enumerate(row):
            if cell == '^' or cell == '>' or cell == '<' or cell == 'v':
                starting_pos = (row_idx, col_idx)
                starting_dir = cell
    
    curr_pos, curr_dir = starting_pos, starting_dir
    pos_count = 0
    while True:
        pos_count += change_cell_and_count(map_grid, curr_pos, 'X')
        new_pos = move(curr_pos, curr_dir)
        if is_out_of_bounds(map_grid, new_pos):
            break
        if get_cell(map_grid, new_pos) == '#':
            curr_dir = rotate(curr_dir)
            continue
        curr_pos = new_pos
            
    return pos_count


def get_cell(map_grid, pos):
    return map_grid[pos[0]][pos[1]]


def change_cell_and_count(map_grid, pos, new_value):
    if map_grid[pos[0]][pos[1]] == 'X':
        return 0
    map_grid[pos[0]][pos[1]] = new_value
    return 1


def move(curr_pos, direction):
    if direction == '^':
        return tuple(item1 + item2 for item1, item2 in zip(curr_pos, (-1, 0)))
    elif direction == 'v':
        return tuple(item1 + item2 for item1, item2 in zip(curr_pos, (1, 0)))
    elif direction == '>':
        return tuple(item1 + item2 for item1, item2 in zip(curr_pos, (0, 1)))
    elif direction == '<':
        return tuple(item1 + item2 for item1, item2 in zip(curr_pos, (0, -1)))


def rotate(curr_dir):
    if curr_dir == '^':
        return '>'
    elif curr_dir == 'v':
        return '<'
    elif curr_dir == '>':
        return 'v'
    elif curr_dir == '<':
        return '^'
    

def is_out_of_bounds(map_grid, pos):
    return not (0 <= pos[0] < len(map_grid) and 0 <= pos[1] < len(map_grid[0]))


if __name__ == '__main__':
    input_filepath = './day_6/input.txt'
    print(f"Number of positions guard will occupy: {count_guard_positions(input_filepath)}")
    