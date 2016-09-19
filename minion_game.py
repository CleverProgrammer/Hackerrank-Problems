"""
Author: Rafeh Qazi
Program: Minion Game (Hackerrank Challenge)
Modified: September 13
"""
from itertools import permutations


def count_occurrence(text='', pattern=''):
    """
    Count how many times a pattern is found inside of a text.
    :param text: str
    :param pattern: str
    :return: int

    >>> count_occurrence('banana', 'b')
    1
    >>> count_occurrence('banana', 'ana')
    2
    >>> count_occurrence('banana', 'a')
    3
    """
    match = 0
    for i in range(len(text)):
        for j in range(len(pattern)):
            if i + j < len(text):
                if text[i + j] != pattern[j]:
                    break
                elif j == len(pattern) - 1:
                    match += 1
                    break
    return match


def all_length_perms(word):
    """
    Given a word, generate all length permutations.
    :param word: str
    :return: list

    >>> all_length_perms('ab')
    ['a', 'b', 'ab', 'ba']
    """
    perms = []
    for i in range(1, len(word) + 1):
        perms += [''.join(perm) for perm in permutations(word, i)]
    return perms


def minion(word):
    """
    Create all permutations of the given word starting with its consonants.
    Give 1 point for each permutation found as a substring in the given word.
    Return score for player 1 and score for player 2. Player 1 is Stuart and
    Player 2 is Kevin. Stuart has the consonants and Kevin the vowels
    :param word: str
    :return: tuple

    >>> minion('banana')
    'Stuart 12'

    >>> minion('aaa')
    'Kevin 6'

    >>> minion('ab')
    'Kevin 2'
    """
    consonant = set('bcdfghjklmnpqrstvwxyz')
    vowels = set('aeiou')
    assert len(consonant.union(vowels)) == 26
    perms = set(all_length_perms(word))

    all_perms = set()

    for perm in perms:
        found = count_occurrence(word, perm)
        if found and perm[0] in consonant:
            all_perms.add((perm, found, 'consonant'))
        elif found and perm[0] in vowels:
            all_perms.add((perm, found, 'vowel'))

    consonant_score = sum([score for _, score, type in all_perms if type == 'consonant'])
    vowel_score = sum([score for _, score, type in all_perms if type == 'vowel'])

    if consonant_score > vowel_score:
        return 'Stuart {}'.format(consonant_score)
    return 'Kevin {}'.format(vowel_score)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
