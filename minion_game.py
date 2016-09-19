"""
Author: Rafeh Qazi
Program: Minion Game (Hackerrank Challenge)
Modified: September 13
"""
from itertools import permutations
from collections import namedtuple


def count_occurrence(text='', pattern=''):
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


print(count_occurrence('banana', 'b'))


def perms_with_consonant(word):
    word_scores = []
    Consonant = namedtuple('Consonant', ['position', 'letter'])
    word = word.lower()
    consonants = [Consonant(index, letter) for index, letter in enumerate(word) if
                  letter not in ('a', 'e', 'i', 'o', 'u')]
    print(consonants)
    for consonant in consonants:
        print(consonant.position, consonant.letter)
        if not consonant.position == len(word) - 1:
            # Skip the letter
            new_word = word[:consonant.position] + word[consonant.position + 1:]
            perms = permutations(new_word)
            for perm in perms:
                print(''.join(perm))
                found = count_occurrence(word, ''.join(perm))
                print(found)
                if found:
                    word_scores.append((''.join(perm), found))
            print(new_word)
        else:
            new_word = word[:-1]
            print(new_word)
    # results = []
    #
    # for perm in perms:
    #     results.append(consonants[0] + ''.join(perm))

    # return results
    print(word_scores)


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


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    print(all_length_perms('OBIAS'))
