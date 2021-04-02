# -*- coding: utf-8 -*-
"""Advent Of Code 2020,  Day 17

@author: Matevz
"""

import itertools
import numpy as np

def create_test_input():
    arr2d = np.array(
        [['.', '#', '.'],
          ['.', '.', '#'],
          ['#', '#', '#']]
        )
    return arr2d[:, :, np.newaxis]


def get_input(file_name):
    """Process input text file."""
    try:
        file = open(file_name, 'r')
        content = file.read()
    except IOError:
        print('Cannot read file {}'.format(file_name))
    finally:
        file.close()

    content = [list(i) for i in content.splitlines()]
    content = np.array(content)

    return np.array(content)


#%% Direct neighbours

# https://stackoverflow.com/questions/26363579/how-to-find-neighbors-of-a-2d-list-in-python
def direct_neighbours(i, j, k):
    """Positions of neighbours (includes out of bounds but excludes cell itself)."""
    neighbours = list(itertools.product(range(i-1, i+2), range(j-1, j+2), range(k-1, k+2)))
    neighbours.remove((i, j, k))
    return neighbours


def count_active_neighbours(matrix, i, j, k):
    rows, cols, slices = matrix.shape
    neighbours = direct_neighbours(i, j, k)
    neighbours = [[x,y,z] for x,y,z in neighbours if (-1 < x < rows and -1 < y < cols and -1 < z < slices)]
    values = [matrix[x,y,z] for x,y,z in neighbours]
    return values.count('#')

def simulate_one_cycle(matrix):
    """Return transformad matrix according to direct neighbours rules."""
    rows, cols, slices = matrix.shape
    old = matrix.copy()
    new = matrix.copy()
    for i in range(rows):
        for j in range(cols):
            for k in range(slices):
                active = count_active_neighbours(old, i, j, k)
                if old[i, j, k] == '#':
                    if active in (2,3):
                        new[i,j,k] = '#'
                    else:
                        new[i,j,k] = '.'
                else:
                    if active == 3:
                        new[i,j,k] = '#'
                    else:
                        new[i,j,k] = '.'

    return new


#%% Distant neighbours

def count_occupied_distant_neighbours(matrix, i, j):
    """Count occupied seats from i,j seat."""
    directions = [[1, 0], [1, -1], [0, -1], [-1, -1],
                  [-1, 0], [-1, 1], [0, 1], [1, 1]]
    rows, cols = matrix.shape
    count = 0

    if matrix[i, j] != '.':
        for y_step, x_step in directions:
            x = i + x_step
            y = j + y_step
            while (-1 < x < rows and -1 < y < cols):
                if matrix[x,y] == '#':
                    count += 1
                    break
                elif matrix[x,y] == 'L':
                    break
                else:
                    x += x_step
                    y += y_step

    return count


def new_seating_distant_neighbours(matrix):
    """Return transformad matrix according to distant neighbours rules."""
    rows, cols = matrix.shape
    old = matrix.copy()
    new = matrix.copy()
    for i in range(rows):
        for j in range(cols):
            if old[i, j] == '.':
                new[i,j] = old[i,j]
            else:
                neighbour_count = count_occupied_distant_neighbours(old, i, j)
                if (old[i,j] == 'L') and (neighbour_count == 0):
                    new[i,j] = '#'
                elif (old[i,j] == '#') and (neighbour_count >= 5):
                    new[i,j] = 'L'
                else:
                    new[i,j] = old[i,j]

    return new


#%% Simulate seating

def simulate_seating_area(matrix, direct_method=True):
    """Return converged number of occupied seats according to rules."""

    old = matrix.copy()
    new = matrix.copy()
    occupied = 0
    occupied_old = -1
    while occupied != occupied_old:
        occupied_old = occupied
        if direct_method:
            new = new_seating_direct_neighbours(old)
        else:
            new = new_seating_distant_neighbours(old)


        occupied = np.count_nonzero(new == '#')
        old = new.copy()

    return occupied


#%% Get puzzle answers

def main():
    """Solution to both parts of Advent of Code puzzle."""
    content = get_input('input/day11.txt')
    part1 = simulate_seating_area(content, direct_method=True)
    part2 = simulate_seating_area(content, direct_method=False)
    print('First answer {}, second answer {}.'.format(part1, part2))


# if __name__ == "__main__":
#     main()
