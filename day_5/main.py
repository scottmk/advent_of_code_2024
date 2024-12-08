"""https://adventofcode.com/2024/day/5"""

from collections import defaultdict
from functools import cmp_to_key
from common_main_methods import read_text_file_lines


def parse_input(input_filepath):
    input_lines = read_text_file_lines(input_filepath)
    rules = defaultdict(set)
    last_idx = -1
    for idx, line in enumerate(input_lines):
        if line == '\n':
            last_idx = idx
            break
        lhs, rhs = tuple(line.strip().split('|'))
        rules[int(lhs)].add(int(rhs))
    
    updates = [[int(page_num) for page_num in line.strip().split(',')] for line in input_lines[last_idx + 1:]]
    return rules, updates


def determine_correct_updates(input_filepath, should_fix=False):
    rules, updates = parse_input(input_filepath)
    valid_updates = []
    invalid_updates = []
    for update in updates:
        is_valid_update = True
        for update_idx, page_num in enumerate(update):
            if update_idx == 0:
                continue
            # every page in this set must be _after_ the current page
            rule = rules[page_num]
            previous_pages = set(update[:update_idx])
            if len(rule & previous_pages) > 0:
                is_valid_update = False
                break
        if is_valid_update:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    
    if should_fix:
        fixed_update_sum = 0
        for update in invalid_updates:
            fixed_update = sorted(
                update, 
                key=cmp_to_key(lambda first, second: compare_pages(first, second, rules))
            )
            fixed_update_sum += fixed_update[int(len(update)/2)]
            
        return fixed_update_sum
    else:
        return sum([update[int(len(update)/2)] for update in valid_updates])


def compare_pages(first, second, rules):
    if second in rules[first]:
        return -1
    else:
        return 1


if __name__ == '__main__':
    input_filepath = './day_5/input.txt'
    print(f"Sum of middle page numbers in correct updates: {determine_correct_updates(input_filepath)}")
    print(f"Sum of middle page numbers in corrected updates: {determine_correct_updates(input_filepath, should_fix=True)}")
    