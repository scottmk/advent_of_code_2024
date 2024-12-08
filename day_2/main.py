"""https://adventofcode.com/2024/day/2"""

from itertools import pairwise
from math import copysign
from common_main_methods import read_text_file_lines


def is_report_safe(report):
    is_safe = True
    last_diff = None
    for leftLevel, rightLevel in pairwise(report):
         diff = leftLevel - rightLevel
         if not last_diff:
             last_diff = diff
         is_safe &= 1 <= abs(diff) <= 3
         is_safe &= copysign(1, diff) == copysign(1, last_diff)
         last_diff = diff
    return is_safe


def get_safe_report_count(input_filepath):
    report_lines = read_text_file_lines(input_filepath)
    reports = [[int(level) for level in report.split()] for report in report_lines]
    
    return sum([1 if is_report_safe(report) else 0 for report in reports])


if __name__ == '__main__':
    input_filepath = './day_2/input.txt'
    print(f"Number of Safe Reports: {get_safe_report_count(input_filepath)}")
