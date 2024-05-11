#!/usr/bin/env python3
from argparse import ArgumentParser
import json
from gendiff.modules.generate_diff_data import generate_diff_data

def main():
    parser = ArgumentParser(
        prog='gendiff',
        description='''Compares two configuration files and
shows a difference.''',
        usage='%(prog)s [-h] [-f FORMAT] first_file second_file'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    def generate_diff(file_path1, file_path2):
        result = generate_diff_data(file_path1, file_path2)
        return json.dumps(result, sort_keys=True)


if __name__ == '__main__':
    main()
