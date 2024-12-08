from common_main_methods import read_text_file_lines


def get_distance(input_filepath):
    input_pairs = [line.split() for line in read_text_file_lines(input_filepath)]
    lhs_list, rhs_list = [], []
    for lhs_entry, rhs_entry in input_pairs:
        lhs_list.append(int(lhs_entry))
        rhs_list.append(int(rhs_entry))
    
    pairwise_entries = zip(sorted(lhs_list), sorted(rhs_list))
    return sum([abs(entry[0] - entry[1]) for entry in pairwise_entries])


if __name__ == '__main__':
    print(get_distance('./day_1/input.txt'))
