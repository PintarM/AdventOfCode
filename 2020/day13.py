# -*- coding: utf-8 -*-
"""Advent Of Code 2020,  Day 13

@author: Matevz
"""

from sympy.ntheory.modular import crt


def get_input(file_name):
    """Process input text file."""
    try:
        file = open(file_name, 'r')
        content = file.read()
    except IOError:
        print('Cannot read file {}'.format(file_name))
    finally:
        file.close()

    timestamp, lines = content.splitlines()
    lines = [int(i) if i != 'x' else i for i in lines.split(',')]

    return [int(timestamp), lines]


def waiting_time(timestamp, bus):
    """Bus waiting time."""
    before = (timestamp // bus) * bus
    return (before + bus) - timestamp


def earliest_bus_product(timestamp, lines):
    """Product of earliest bus time and line number."""
    buses = [int(i) for i in lines if i != 'x' ]
    times = [waiting_time(timestamp, bus) for bus in buses]
    min_time = min(times)
    bus_no = buses[times.index(min_time)]

    return min_time * bus_no


def buses_delays(timestamp, lines):
    """Bus delay for certain timestamp."""
    return [((timestamp + i) % int(v)) for i,v in enumerate(lines) if v != 'x']


def earliest_consecutive_timestamp_naive(lines, start_at=0):
    """Naive implementation of earliest consecutive timestamo."""
    increment = int(lines[0])
    timestamp = (start_at // increment) * increment

    while sum(buses_delays(timestamp, lines)) != 0:
        timestamp += increment

    return timestamp

# https://www.geeksforgeeks.org/python-sympy-crt-method/
def earliest_consecutive_timestamp(lines):
    """Earliest consecutive timestamp using Chinese Remainder Theorem."""
    data = {v: (v - i) % v for i,v in enumerate(lines) if v != 'x'}
    moduli = data.keys()
    remainders = data.values()

    return crt(moduli, remainders)[0]


def main():
    """Solution to both parts of Advent of Code puzzle."""
    timestamp, lines = get_input('input/day13.txt')
    part1 = earliest_bus_product(timestamp, lines)
    part2 = earliest_consecutive_timestamp(lines)
    print('First answer {}, second answer {}.'.format(part1, part2))


if __name__ == "__main__":
    main()
