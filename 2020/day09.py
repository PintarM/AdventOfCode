# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 7

@author: Matevz
"""


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

    return content


def possible_sums(interval):
    """All sums of two numbers in list where numbers are not equal."""
    return {i+j for i in interval for j in interval if i!=j}


def find_first_weakness(content, preamble):
    """First weakness in XMAS code."""

    is_found = False
    count = 0
    while not is_found:
        interval = content[count : preamble + count]
        number = content[preamble + count]
        sums  = possible_sums(interval)
        if number not in sums:
            is_found=True
        count +=1

    return number


def possible_contigious_sequence(interval, max_num):
    """All possible contigous subsequences of a list up to max length."""
    subsequence = []
    for num in range(2, max_num + 1):
        subsequence += [interval[i:i + num] for i in range(0, len(interval))][:(-(num-1))]
    return subsequence


def find_second_weakness(content, preamble):
    """Second weakness in XMAS code."""
    weakness = find_first_weakness(content, preamble)
    position =  [i for i,x in enumerate(content) if x == weakness][0]
    interval = content[:position]
    all_sub = possible_contigious_sequence(interval, 20)

    weak_sub = []
    for i in all_sub:
        if sum(i)==weakness:
            weak_sub = i

    return min(weak_sub) + max(weak_sub)


def main():
    """Solution to both parts of Advent of Code puzzle."""
    content = get_input('input/day09.txt')
    part1 = find_first_weakness(content, 25)
    part2 = find_second_weakness(content, 25)
    print('First answer {}, second answer {}.'.format(part1, part2))


if __name__ == "__main__":
    main()
