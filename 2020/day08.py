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

    content = [i.split() for i in content.splitlines()]
    content = [[key, int(val)] for key, val in content]

    return content


def accumulator_value(rules):
    """Accumulate value until infinite loop starts."""
    counter = 0
    pos = 0
    visited_pos = []
    while pos not in visited_pos:
        rule = rules[pos]
        visited_pos.append(pos)
        if rule[0] == 'acc':
            counter += rule[1]
            pos += 1
        elif rule[0] == 'jmp':
            pos += rule[1]
        else:
            pos += 1

    return counter


def fix_boot_process(rules):
    """Fix one instruction to break infinite loop."""

    possible_pos = [i for i,v in enumerate(rules) if v[0] in ('nop', 'jmp')]

    for try_pos in possible_pos:
        counter = 0
        pos = 0
        visited_pos = []
        finished = False
        while pos not in visited_pos:
            if pos == len(rules):
                finished = True
                break
            instruction, val = rules[pos]
            if pos == try_pos:
                if instruction == 'jmp':
                    instruction = 'nop'
                else:
                    instruction = 'jmp'

            visited_pos.append(pos)
            if instruction == 'acc':
                counter += val
                pos += 1
            elif instruction == 'jmp':
                pos += val
            else:
                pos += 1
        if finished:
            break

    return counter


def main():
    """Solution to both parts of Advent of Code puzzle."""
    content = get_input('input/day08.txt')
    part1 = accumulator_value(content)
    part2 = fix_boot_process(content)
    print('First answer {}, second answer {}.'.format(part1, part2))


if __name__ == "__main__":
    main()
