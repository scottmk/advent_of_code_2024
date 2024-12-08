"""https://adventofcode.com/2024/day/3"""

import re
from common_main_methods import read_text_file_lines


def get_fixed_mul_ops(input_filepath):
    instruction_lines = read_text_file_lines(input_filepath)
    sum_of_ops = 0
    for instruction_line in instruction_lines:
        mul_ops = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', instruction_line)
        sum_of_ops += sum([int(params[0]) * int(params[1]) for params in mul_ops])
    return sum_of_ops


if __name__ == '__main__':
    input_filepath = './day_3/input.txt'
    print(f"Sum of mul operations: {get_fixed_mul_ops(input_filepath)}")

