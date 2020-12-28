# -*- coding: utf-8 -*-
"""Advent Of Code 2020,  Day 16

@author: Matevz
"""

from collections import defaultdict

import numpy as np

def string_to_range(string):
    """Convert string to range of integers."""
    a = int(string[1:3])
    b = int(string[4:7])
    c = int(string[11:14])
    d = int(string[15:18])

    return list(range(a,b+1)) + list(range(c,d+1))


def get_input(file_name):
    """Process input text file."""
    try:
        file = open(file_name, 'r')
        content = file.read()
    except IOError:
        print('Cannot read file {}'.format(file_name))
    finally:
        file.close()

    rules, ticket, other = content.split('\n\n')

    rules = [line.split(':') for line in rules.splitlines()]
    rules = {k: string_to_range(v) for k,v in rules}

    ticket = ticket.splitlines()[1]
    ticket = [int(i) for i in ticket.split(',')]

    other = [line.split(',') for line in other.splitlines()[1:]]
    other = [list(map(int, line)) for line in other]

    return rules, ticket, other


def field_valid_values(rules):
    valid_values = []
    for val in rules.values():
        valid_values.extend(val)

    return set(valid_values)


def ticket_scanning_error_rate(rules, other):
    """Sum of invalid ticket fields."""
    valid_values = field_valid_values(rules)
    invalid_values = []
    for ticket in other:
        for i in ticket:
            if i not in valid_values:
                invalid_values.append(i)

    return sum(invalid_values)


def difference(li1, li2):
    """Difference of two lists."""
    return list(list(set(li1)-set(li2)) + list(set(li2)-set(li1)))


def get_field_order(rules, other):
    """Field order on tickets."""
    all_valid_values = field_valid_values(rules)
    valid_tickets = [ticket for ticket in other if set(ticket).issubset(all_valid_values)]
    possible_order = defaultdict(lambda: [])
    for pos in range(20):
        ticket_values = [ticket[pos] for ticket in valid_tickets]
        for field_name, field_values in rules.items():
            if set(ticket_values).issubset(field_values):
                possible_order[field_name].append(pos)

    final_order = {}
    found = []
    for i in range(1,21):
        for name, values in possible_order.items():
            if len(values) == i:
                known_position  = difference(found, values)[0]

                found.append(known_position)
                final_order[name] = known_position

    return final_order


def get_departure_field_values(rules, ticket, other):
    """Position of all fields staritng with word 'departure'."""
    order = get_field_order(rules, other)
    return [ticket[v] for k,v in order.items() if k.startswith('departure')]


def main():
    """Solution to both parts of Advent of Code puzzle."""
    rules, ticket, other = get_input('input/day16.txt')
    part1 = ticket_scanning_error_rate(rules, other)
    # Beware of owerflow!
    part2 = np.prod(get_departure_field_values(rules, ticket, other), dtype=np.int64)
    print('First answer {}, second answer {}.'.format(part1, part2))


if __name__ == "__main__":
    main()
