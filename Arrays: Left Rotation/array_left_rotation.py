"""
Author: Rafeh Qazi
Program: Array Left Rotation (Hackerrank Challenge)
Modified: October 2016
Submit this code at: https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""

def array_left_rotation(int_list, shift):
    """
    Given an array of  integers and a number, perform left rotations on the array.
    Then print the updated array as a single line of space-separated integers.

    :param int_list:
    :param shift:

    >>> array_left_rotation([1, 2, 3, 4, 5], 1)
    '2 3 4 5 1'

    >>> array_left_rotation([2, 3, 4, 5, 1], 3)
    '5 1 2 3 4'
    """
    pairs = new_index_value_pairs(int_list, shift)
    replace_int_list(int_list, pairs)
    print(*replace_int_list, sep=' ')

if __name__ == '__main__':
    array_left_rotation()