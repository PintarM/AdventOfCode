# -*- coding: utf-8 -*-
"""Advent Of Code 2020,  Day 15

@author: Matevz
"""

from collections import defaultdict


def final_number_spoken(start_list, final_number):
    """text"""
    # dict with form {value: last_pos}
    memory = defaultdict(lambda: -1)

    for pos, val in enumerate(start_list[:-1]):
        memory[val] = pos

    spoken_last = start_list[-1]
    for i in range(len(start_list), final_number):
        pos_last = memory[spoken_last]
        if pos_last == -1:
            spoken_now = 0
        else:
            spoken_now = ((i-1) - pos_last)
        memory[spoken_last] = (i-1)
        spoken_last = spoken_now

    return spoken_now


def main():
    """Solution to both parts of Advent of Code puzzle."""
    content = [15,5,1,4,7,0]
    part1 = final_number_spoken(content, 2020)
    part2 = final_number_spoken(content, 30000000)
    print('First answer {}, second answer {}.'.format(part1, part2))


if __name__ == "__main__":
    main()
