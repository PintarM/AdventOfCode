# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 12

@author: Matevz
"""

import math
import numpy as np


def get_input(file_name):
    """Process input text file."""
    try:
        file = open(file_name, 'r')
        content = file.read()
    except IOError:
        print('Cannot read file {}'.format(file_name))
    finally:
        file.close()

    content = [[i[0], int(i[1:])] for i in content.splitlines()]

    return content


def rotate(l, n):
    """Rotate list for n steps."""
    return l[n:] + l[:n]


def ship_position_naive(content):
    """Ship position according to naive interpretation of rules."""

    rules = {'N': np.array([0,1]), 'S': np.array([0,-1]),
             'E': np.array([1,0]), 'W': np.array([-1,0])}
    orientations = ['E', 'S', 'W', 'N']
    pos = np.array([0,0])

    for instruction, distance in content:
        if instruction in ['N', 'S', 'E', 'W']:
            step = distance * rules[instruction]
        elif instruction in ['R', 'L']:
            rotation_step = (distance // 90) * ({'R': 1, 'L': -1}[instruction])
            orientations = rotate(orientations, rotation_step)
            step = np.array([0, 0])
        else:
            step = distance * rules[orientations[0]]

        pos += step

    return pos


# https://stackoverflow.com/a/34374437
def rotate_point(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return np.array([qx, qy])


def ship_position_waypoint(content):
    """Ship position acco"""

    move_waypoint = {'N': np.array([0.,1.]), 'S': np.array([0.,-1.]),
             'E': np.array([1.,0.]), 'W': np.array([-1.,0.])}
    pos = np.array([0.,0.])
    waypoint = np.array([10.,1.])

    for instruction, value in content:
        if instruction in ['N', 'S', 'E', 'W']:
            waypoint += value * move_waypoint[instruction]
            step = np.array([0.,0.])
        elif instruction in ['R', 'L']:
            sign = -1 if instruction == 'R' else 1
            waypoint = rotate_point([0.,0.], waypoint, sign * math.radians(value))
            step = np.array([0.,0.])
        else:
            step = value * waypoint

        pos += step

    return pos


def main():
    """Solution to both parts of Advent of Code puzzle."""
    content = get_input('input/day12.txt')
    part1 = sum(abs( ship_position_naive(content) ))
    part2 = sum(abs( ship_position_waypoint(content) )).round()
    print('First answer {}, second answer {}.'.format(part1, int(part2)))


if __name__ == "__main__":
    main()
