# -*- coding: utf-8 -*-
"""
Advent Of Code 2020,  Day 4

@author: Matevz
"""


def string_to_dict(string):
    mydict = dict((x.strip(), y.strip())
                  for x, y in (element.split(':') for element in string.split()))

    return mydict


def get_input(file_name):
    try:
        file = open(file_name, 'r')
        content = file.read()
    except IOError:
        print('Cannot read file {}'.format(file_name))
    finally:
        file.close()

    content = [i.replace('\n',' ') for i in content.split("\n\n")]

    return [string_to_dict(string) for string in content]


def intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


def is_valid_passport_basic(passport):
    # 'cid' is removed
    mandatory_fields = ['eyr', 'hgt', 'pid', 'hcl', 'byr', 'ecl', 'iyr']
    existing_fields= list(passport.keys())
    inter = intersection(existing_fields, mandatory_fields)
    return len(inter) == 7


def is_valid_byr(passport):
    return 1920 <= int(passport['byr']) <= 2002


def is_valid_iyr(passport):
    return 2010 <= int(passport['iyr']) <= 2020


def is_valid_eyr(passport):
    return 2020 <= int(passport['eyr']) <= 2030


def is_valid_hgt(passport):
    string = passport['hgt']
    if string.endswith('cm'):
        is_valid = 150 <= int(string[:-2]) <= 193
    elif string.endswith('in'):
        is_valid = 59 <= int(string[:-2]) <= 76
    else:
        is_valid = False

    return is_valid


def is_valid_hcl(passport):
    string = passport['hcl']
    hexdigits = '0123456789abcdefABCDEF'
    return (string.startswith('#')) & all(c in hexdigits for c in string[1:])


def is_valid_ecl(passport):
    return passport['ecl'] in ['amb','blu','brn', 'gry', 'grn', 'hzl', 'oth']


def is_valid_pid(passport):
    string = passport['pid']
    digits = '0123456789'
    return (len(string) == 9) & all(c in digits for c in string)


def is_valid_passport_strict(passport):
    checks = [
        is_valid_byr(passport),
        is_valid_iyr(passport),
        is_valid_eyr(passport),
        is_valid_hgt(passport),
        is_valid_hcl(passport),
        is_valid_ecl(passport),
        is_valid_pid(passport)
    ]
    return all(checks)


def count_valid_passports(content):

    count = 0
    count_strict = 0
    for passport in content:
        if is_valid_passport_basic(passport):
            count += 1
            if is_valid_passport_strict(passport):
                count_strict += 1

    return [count, count_strict]


def main():
    """Solution to both parts of AoC Day 4 problem."""
    content = get_input('input/day04.txt')
    basic, strict = count_valid_passports(content)
    print('First answer {}, second answer {}.'.format(basic, strict))


if __name__ == "__main__":
    main()
