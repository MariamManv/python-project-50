#!/usr/bin/env python3
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(
        prog='gendiff',
        description='''Compares two configuration files and
shows a difference.''',
        usage='%(prog)s [-h] first_file second_file'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
