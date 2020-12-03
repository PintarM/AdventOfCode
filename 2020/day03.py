# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 3

@author: Matevz
"""

import numpy as np

def get_input(file_name):
    """Process text file to list of lists of strings."""
    try:
        file = open(file_name, 'r')
        content = file.read()
    except IOError:
        print('Cannot read file {}'.format(file_name))
    finally:
        file.close()

    content = [list(i) for i in content.splitlines()]

    return np.array(content)


def replace_characters(content, down_step, right_step):
    """Replace specific characters."""

    matrix = content.copy()
    down_max, right_max = matrix.shape

    for i in range(down_max):
        x = (right_step * i) % right_max
        y = down_step * i
        if y > down_max:
            break

        char = matrix[y, x]
        if char == '#':
            matrix[y, x] = 'X'
        else:
            matrix[y, x] = 'O'

    return matrix


def count_characters(matrix, character):
    """Count specific characters in a matrix."""
    unique, counts = np.unique(matrix, return_counts=True)
    mapping_count = dict(zip(unique, counts))

    return mapping_count[character]


def count_trees(content, down_step=1, right_step=3):
    """Count trees for specific combination of steps."""

    matrix = replace_characters(content, down_step, right_step)

    return count_characters(matrix, 'X')


def main():
    """Solution to both parts of AoC Day 2 problem."""

    content = get_input('day03.txt')
    print('First answer of the puzzle {}.'.format(count_trees(content)))

    settings = [[1,1],[1,3],[1,5],[1,7],[2,1]]
    tree_counts = [count_trees(content, down, right) for down, right in settings]

    print('Second answer of the puzzle {}.'.format(np.prod(tree_counts)))


if __name__ == "__main__":
    main()
