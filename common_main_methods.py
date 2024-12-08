import sys


def read_text_file(text_file_path):
    """
    Read the text file at the given file path and return it in str form
    :param text_file_path: The path of the file to read
    :return: The contents of the file in utf-8-encoded str form
    """
    try:
        with open(text_file_path, mode='r', encoding='utf-8') as text_file:
            return "".join(text_file.readlines())
    except IOError:
        sys.stderr.write(f"Text file <{text_file_path}> is not valid\n")
        sys.exit(1)


def read_text_file_lines(text_file_path):
    """
    Read the text file at the given file path and return it as list of str representing each line
    :param text_file_path: The path of the file to read
    :return: The contents of the file in utf-8-encoded str form list of str representing each line
    """
    try:
        with open(text_file_path, mode='r', encoding='utf-8') as text_file:
            return text_file.readlines()
    except IOError:
        sys.stderr.write(f"Text file <{text_file_path}> is not valid\n")
        sys.exit(1)
