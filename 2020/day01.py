# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 1

@author: Matevz
"""

from itertools import combinations
import numpy as np


def get_input(file_name):
    """List of integers from text file."""
    try:
        file = open(file_name, 'r')
        content = file.read()
    except IOError:
        print('Cannot read file {}'.format(file_name))
    finally:
        file.close()

    content = [int(i) for i in content.splitlines()]

    return content


def product_of_combination(expense, n):
    """Product of the first combination of n entries which sum up to 2020."""

    comb = combinations(expense, n)

    for c in list(comb):
        if sum(c) == 2020:
            print('Product of {} is {}'.format(c, np.prod(c)))
            break

def main():
    """Solution to both parts of AoC Day 1 problem."""
    expense = get_input('input/day01.txt')
    product_of_combination(expense, 2)
    product_of_combination(expense, 3)


if __name__ == "__main__":
    main()
