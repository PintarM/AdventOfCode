# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 10

@author: Matevz
"""

test_1 = [16,10,15,5,1,11,7,19,6,12,4]
test_2 = [1,2,3,4,7,8,9,10,11,14,17,18,19,20,23,24,25,28,31,32,33,34,35,38,39,42,45,46,47,48,49]


def get_input(file_name):
    """Process input text file."""
    try:
        file = open(file_name, 'r')
        content = file.read()
    except IOError:
        print('Cannot read file {}'.format(file_name))
    finally:
        file.close()

    content = [int(i) for i in content.splitlines()]

    return sorted(content)


def jolt_differences(content):
    """Differeces of integer list."""

    jolts = sorted(content)
    jolts.insert(0, 0)
    jolts.append(jolts[-1] + 3)
    diff = [j-i for i, j in zip(jolts[:-1], jolts[1:])]

    return diff


def differences_product(diff):
    """Product of count of differences 1 and 3."""
    return diff.count(1) * diff.count(3)


# https://codereview.stackexchange.com/a/215329
def count_subsequence(needle, haystack):
    """Count subsequences."""
    bool_list = [
        haystack[i:i+len(needle)] == needle
        for i in range(len(haystack) - len(needle) + 1)
    ]
    return bool_list.count(True)


def adapter_sequence_count(content):
    """All possible subsequence count."""
    jolts = sorted(content)
    jolts.insert(0, 0)
    jolts.append(jolts[-1] + 3)
    diff = [j-i for i, j in zip(jolts[:-1], jolts[1:])]
    diff.insert(0,3)
    counter=dict()
    for i in range(2,5):
        sub = [3] + i*[1] + [3]
        counter[i]=count_subsequence(sub, diff)

    product = 2**counter[2] * 4**counter[3] * 7**counter[4]
    return product


def main():
    """Solution to both parts of Advent of Code puzzle."""
    content = get_input('input/day10.txt')
    part1 = differences_product(jolt_differences(content))
    part2 = adapter_sequence_count(content)
    print('First answer {}, second answer {}.'.format(part1, part2))


if __name__ == "__main__":
    main()
