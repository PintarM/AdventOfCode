# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 14

@author: Matevz
"""

import re
from collections import defaultdict


def get_input(file_name):
    """Process input text file."""
    try:
        file = open(file_name, 'r')
        content = file.read()
    except IOError:
        print('Cannot read file {}'.format(file_name))
    finally:
        file.close()

    return content.splitlines()


def get_bin(x, n=0):
    """Binary representation of x, padded to length n"""
    return format(x, 'b').zfill(n)


def apply_mask(binary_value, mask):
    """Apply binary mask to value."""
    new = [v if m == 'X' else m for v, m in zip(list(binary_value), list(mask))]
    return ''.join(new)


def docking_data(content):
    """Sum of memory."""
    memory = defaultdict(lambda: [])
    for line in content:
        if line.startswith('mask'):
            mask = line[7:]
        else:
            address = int(re.findall(r'\[(.*?)\]', line)[0])
            value = int(re.findall(r'(?<= = )[\w+.-]+', line)[0])
            binary_value = get_bin(value, 36)
            new_value = int(apply_mask(binary_value, mask), 2)
            memory[address] = new_value

    return memory


def apply_mask_version_2(binary_value, mask):
    """Version 2"""
    new = []
    for v, m in zip(list(binary_value), list(mask)):
        if m == '0':
            new.append(v)
        elif m == '1':
            new.append('1')
        else:
            new.append('X')

    return ''.join(new)


def find_all_addresses(floating_address):
    """Find all binary adresses from floating address."""
    address = list(floating_address)
    pos = [i for i, val in enumerate(address) if val == 'X']
    n = len(pos)
    subsets = [list(get_bin(i, n)) for i in range(2**n)]
    all_addresses = []
    for sub in subsets:
        for i, val in zip(pos, sub):
            address[i] = val
        all_addresses.append(''.join(address))

    return all_addresses


def docking_data_version_2(content):
    """All memory, version 2."""
    memory = defaultdict(lambda: [])
    for line in content:
        if line.startswith('mask'):
            mask = line[7:]
        else:
            address = int(re.findall(r'\[(.*?)\]', line)[0])
            value = int(re.findall(r'(?<= = )[\w+.-]+', line)[0])
            binary_address = get_bin(address, 36)
            floating_address = apply_mask_version_2(binary_address, mask)
            all_addresses = find_all_addresses(floating_address)
            for a in all_addresses:
                memory[int(a)] = value

    return memory


def main():
    """Solution to both parts of Advent of Code puzzle."""
    content = get_input('input/day14.txt')
    part1 = sum(docking_data(content).values())
    part2 = sum(docking_data_version_2(content).values())
    print('First answer {}, second answer {}.'.format(part1, part2))


if __name__ == "__main__":
    main()
