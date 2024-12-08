"""https://adventofcode.com/2024/day/4"""

from typing import Counter
from common_main_methods import read_text_file_lines


def count_xmas_occurrences(input_filepath):
    word_search_lines = read_text_file_lines(input_filepath)
    num_lines = len(word_search_lines)
    possible_words = Counter()
    for row_idx, line in enumerate(word_search_lines):
        line = line.strip()
        line_length = len(line)
        for col_idx, letter in enumerate(line):
            if letter != 'X':
                continue
            # look right, straight
            if col_idx + 3 < line_length:
                possible_words[line[col_idx:col_idx + 4]] += 1
            # look left, straight
            if col_idx - 3 >= 0:
                if col_idx - 3 == 0:
                    possible_words[line[col_idx::-1]] += 1
                else:
                    possible_words[line[col_idx:col_idx - 4:-1]] += 1
            # look up, straight
            if row_idx > 2:
                word = ''
                for i in range(row_idx, row_idx - 4, -1):
                    word += word_search_lines[i][col_idx]
                possible_words[word] += 1
            # look up, diagonal, left
            if row_idx > 2 and col_idx - 3 >= 0:
                word = ''
                col_idx_offset = 0
                for i in range(row_idx, row_idx - 4, -1):
                    word += word_search_lines[i][col_idx - col_idx_offset]
                    col_idx_offset += 1
                possible_words[word] += 1
            # look up, diagonal, right
            if row_idx > 2 and col_idx + 3 < line_length:
                word = ''
                col_idx_offset = 0
                for i in range(row_idx, row_idx - 4, -1):
                    word += word_search_lines[i][col_idx + col_idx_offset]
                    col_idx_offset += 1
                possible_words[word] += 1
            # look down, straight
            if row_idx + 3 < num_lines:
                word = ''
                for i in range(row_idx, row_idx + 4):
                    word += word_search_lines[i][col_idx]
                possible_words[word] += 1
            # look down, diagonal, left
            if row_idx + 3 < num_lines and col_idx - 3 >= 0:
                word = ''
                col_idx_offset = 0
                for i in range(row_idx, row_idx + 4):
                    word += word_search_lines[i][col_idx - col_idx_offset]
                    col_idx_offset += 1
                possible_words[word] += 1
            # look down, diagonal, right
            if row_idx + 3 < num_lines and col_idx + 3 < line_length:
                word = ''
                col_idx_offset = 0
                for i in range(row_idx, row_idx + 4):
                    word += word_search_lines[i][col_idx + col_idx_offset]
                    col_idx_offset += 1
                possible_words[word] += 1
    return possible_words['XMAS']


if __name__ == '__main__':
    input_filepath = './day_4/input.txt'
    print(f"Number of XMAS in search: {count_xmas_occurrences(input_filepath)}")
