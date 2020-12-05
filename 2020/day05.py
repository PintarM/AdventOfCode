# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 5

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

    content = content.splitlines()

    return content


def seat_position(boarding_pass):
    """Get seat position from boarding pass code."""
    row_code = boarding_pass[:7].replace('F','0').replace('B','1')
    col_code = boarding_pass[7:].replace('L','0').replace('R','1')
    row = int(row_code,2)
    col = int(col_code,2)
    return {'row': row, 'column': col, 'id': row * 8 + col}


def all_seat_ids(content):
    """All seat id's from list of boarding passes."""
    ids=[]
    for boarding_pass in content:
        ids.append(seat_position(boarding_pass)['id'])

    return ids


def find_my_seat(ids):
    """Find missing id, my seat."""
    id_min = min(ids)
    id_max = max(ids)
    for i in range(id_min, id_max):
        if i not in ids:
            my_id = i
            break
    return my_id


def main():
    """Solution to both parts of AoC Day 5 problem."""
    content = get_input('input/day05.txt')
    ids = all_seat_ids(content)
    my_id = find_my_seat(ids)
    print('First answer {}, second answer {}.'.format(max(ids), my_id))


if __name__ == "__main__":
    main()
