#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev, total = 0, 0
    for char in roman_string:
        if prev > roman_dict[char]:
            total -= 2 * roman_dict[char]
        total += roman_dict[char]
        prev = roman_dict[char]
    return total
