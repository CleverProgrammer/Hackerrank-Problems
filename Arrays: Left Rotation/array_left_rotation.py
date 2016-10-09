"""
Author: Rafeh Qazi
Program: Array Left Rotation (Hackerrank Challenge)
Modified: October 2016
Submit this code at: https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""


def new_index_value_pairs(int_list, shift):
    """
    Create a list of shifted index and value tuples.
    :param int_list: list
    :param shift: int
    :return: list

    Worst Case Complexity: O(N)

    >>> new_index_value_pairs([10, 20, 30], 1)
    [(2, 10), (0, 20), (1, 30)]
    """
    return [((index - shift) % len(int_list), value) for index, value in enumerate(int_list)]


def replace_int_list(int_list, pairs):
    """
    Map the the shifted index value pairs onto the original int_list.
    :param int_list: list
    :param pairs: list

    Worst Case Complexity: O(N)

    >>> int_list = [10, 20, 30]
    >>> replace_int_list(int_list, [(0, 20), (1, 30), (2, 10)])
    >>> int_list
    [20, 30, 10]
    """
    for index, value in pairs:
        int_list[index] = value


def array_left_rotation(int_list, shift):
    """
    Given an array of n integers and a number, d, perform d left rotations on the array.
    Then print the updated array as a single line of space-separated integers.
    :param int_list: list
    :param shift: int

    Worst Case Complexity: O(2N)

    >>> array_left_rotation([1, 2, 3, 4, 5], 1)
    2 3 4 5 1

    >>> array_left_rotation([2, 3, 4, 5, 1], 3)
    5 1 2 3 4
    """
    pairs = new_index_value_pairs(int_list, shift)
    replace_int_list(int_list, pairs)
    print(*int_list, sep=' ')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    n, d = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    array_left_rotation(a, d)
