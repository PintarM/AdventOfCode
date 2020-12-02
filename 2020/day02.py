# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 2

@author: Matevz
"""

def get_input(file_name):
    """Process text file to list of lists of strings."""
    try:
        file = open(file_name, 'r')
        content = file.read()
    except IOError:
        print('Cannot read file {}'.format(file_name))
    finally:
        file.close()

    content = [i.replace('-',' ').replace(':', '').split() for i in content.splitlines()]

    return content


def count_valid_passwords(content):
    """Count passwords where character count is in expected interval."""
    n=0
    for lo, hi, char, password in content:
        counter = password.count(char)
        if int(lo) <= counter <= int(hi):
            n+=1

    return n


def count_valid_passwords_new_policy(content):
    """Count passwords where character appears on expected positions."""
    n=0
    for lo, hi, char, password in content:
        if bool(password[int(lo)-1] == char) ^ bool(password[int(hi)-1] == char):
            n+=1

    return n


def main():
    """Solution to both parts of AoC Day 2 problem."""

    content = get_input('day02.txt')

    n1 = count_valid_passwords(content)
    print('Solution to the first part of puzzle is {}'.format(n1))

    n2 = count_valid_passwords_new_policy(content)
    print('Solution to the second part of puzzle is {}'.format(n2))


if __name__ == "__main__":
    main()
