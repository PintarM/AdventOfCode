# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 7

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


def count_outer_bags(rules, start_color):
    """Count outer bags."""
    relevant_rules = []
    colors_current = [start_color]
    count_previous = -1
    while len(relevant_rules) != count_previous:
        count_previous = len(relevant_rules)
        colors_next = []
        for rule in rules:
            for color in colors_current:
                if (color in rule) & (not rule.startswith(color)):
                    rule_color = ' '.join(rule.split()[:2])
                    if rule not in relevant_rules:
                        relevant_rules.append(rule)
                    colors_next.append(rule_color)
        colors_current = colors_next

    return len(relevant_rules)


def process_content(content):
    """Create dictionary with repeated strings (color names)."""
    rules = defaultdict(lambda: [])
    for string in content:
        bags = []
        for number, color in re.findall(r"(\d+) (\w+ \w+)", string):
            bags = bags + ([color] * int(number))
            key = re.match(r"^(\w+ \w+) bags contain", string).groups()[0]
            rules[key] = bags
    return rules


def count_inner_bags(content, start_color):
    """Count inner bags"""
    rules = process_content(content)
    bags = rules[start_color]
    count = len(bags)

    while len(bags) != 0:
        new_bags = []
        for bag in bags:
            count += len(rules[bag])
            new_bags += rules[bag]
        bags = new_bags

    return count


def main():
    """Solution to both parts of Advent of Code puzzle."""
    content = get_input('input/day07.txt')
    part1 = count_outer_bags(content, 'shiny gold')
    part2 = count_inner_bags(content, 'shiny gold')
    print('First answer {}, second answer {}.'.format(part1, part2))


if __name__ == "__main__":
    main()
