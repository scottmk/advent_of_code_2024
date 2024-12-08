"""https://adventofcode.com/2024/day/1"""

from functools import reduce
from typing import Counter
from common_main_methods import read_text_file_lines


def _parse_input(input_filepath):
    input_pairs = [line.split() for line in read_text_file_lines(input_filepath)]
    lhs_list, rhs_list = [], []
    for lhs_entry, rhs_entry in input_pairs:
        lhs_list.append(int(lhs_entry))
        rhs_list.append(int(rhs_entry))
    return lhs_list, rhs_list


def get_distance(input_filepath):
    lhs_list, rhs_list = _parse_input(input_filepath)
    
    pairwise_entries = zip(sorted(lhs_list), sorted(rhs_list))
    return sum([abs(entry[0] - entry[1]) for entry in pairwise_entries])


def get_similarity(input_filepath):
    lhs_list, rhs_list = _parse_input(input_filepath)
    
    rhs_counts = Counter(rhs_list)
    return sum([id_ * rhs_counts[id_] for id_ in lhs_list])


if __name__ == '__main__':
    input_filepath = './day_1/input.txt'
    print(f"Distance: {get_distance(input_filepath)}")
    print(f"Similarity: {get_similarity(input_filepath)}")
