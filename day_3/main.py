"""https://adventofcode.com/2024/day/3"""

import re
from common_main_methods import read_text_file, read_text_file_lines


def get_fixed_mul_ops(input_filepath, with_conditionals=False):
    # Match group 1 is a do()
    # Match group 2 is a don't()
    # Match group 3 is the LHS of a mul
    # Match group 4 is the RHS of a mul
    ops = re.findall(r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)', read_text_file(input_filepath))

    sum_of_ops = 0
    do_op = True
    for op in ops:
        # item 1 in the tuple is do(); item 2 in the tuple is don't()
        if op[0] or op[1]:
            do_op = (op[0] and not op[1]) or not with_conditionals
            continue

        # item 2 in the tuple is the LHS of mul; item 3 is the RHS
        if do_op:
            sum_of_ops += int(op[2]) * int(op[3])
    return sum_of_ops


if __name__ == '__main__':
    input_filepath = './day_3/input.txt'
    print(f"Sum of mul operations: {get_fixed_mul_ops(input_filepath)}")
    print(f"Sum of mul operations (with conditionals): {get_fixed_mul_ops(input_filepath, with_conditionals=True)}")
