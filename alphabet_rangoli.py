__author__ = 'Rafeh Qazi'

"""
Hackerrank submission link:
https://www.hackerrank.com/contests/pythonist3/challenges/alphabet-rangoli/submissions/code/4241896
date: 11/20/2015
"""


# noinspection PyPep8Naming
def rangoli():
    """
    Takes a user input as size for the designed rangoli.
    :prints: rangoli patterns
    """
    # remove the string in START_INDEX to pass on hackerrank
    START_INDEX = int(input('Please pick a number between 0 and 27: ')) - 1
    MID_INDEX = 2 * START_INDEX
    START_CHARACTER = chr(97 + START_INDEX)
    ALPHABET = [chr(pos) for pos in range(97, 97 + 26)]
    line = list('-' * MID_INDEX + START_CHARACTER + '-' * MID_INDEX)
    stack = []
    for index, _ in enumerate(range((START_INDEX + 1))):
        stack.append(''.join(line))
        print(stack[-1])
        line[MID_INDEX] = chr(97 + START_INDEX - (index + 1))
        mid_ch_pos = ord(line[MID_INDEX])
        mid_to_outer = 0
        character_index = 0
        if line[MID_INDEX] not in ALPHABET:
            break
        for _ in range(index + 1):
            mid_to_outer += 2
            character_index += 1
            line[MID_INDEX + mid_to_outer] = chr(mid_ch_pos + character_index)
            line[MID_INDEX - mid_to_outer] = chr(mid_ch_pos + character_index)
    stack.pop()
    for _ in range(START_INDEX):
        print(stack.pop())

# uncomment the line below to pass on hackerrank
# rangoli()
