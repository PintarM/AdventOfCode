# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 6

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

    content = [i.split('\n') for i in content.split('\n\n')]

    return content


def any_positive_count(content):
    """Count characters present in ANY answer from group."""
    count = [len(set(''.join(group))) for group in content]
    return sum(count)


def group_intersection(group):
    """Intersection of characters for list of strings."""
    characters = [list(i) for i in group]
    return set.intersection(*[set(x) for x in characters])


def all_positive_count(content):
    """Count characters present in ALL answers from group.."""
    count = []
    for group in content:
        count.append(len(group_intersection(group)))

    return sum(count)


def main():
    """Solution to both parts of AoC Day 6 problem."""
    content = get_input('input/day06.txt')
    part1 = any_positive_count(content)
    part2 = all_positive_count(content)
    print('First answer {}, second answer {}.'.format(part1, part2))


if __name__ == "__main__":
    main()
