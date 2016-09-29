"""
Author: Rafeh Qazi
Program: Minion Game (Hackerrank Challenge)
Modified: September 13
Submit this code at: https://www.hackerrank.com/challenges/the-minion-game
"""


def match(text, pattern):
    """
    >>> match('banana', 'ana')
    2
    """
    return sum([1 for i in range(len(text)) if text[i:i + len(pattern)] == pattern])


def substrings(word):
    """
    >>> substrings('hello')
    ['h', 'he', 'hel', 'hell', 'hello']
    """
    return [word[:i + 1] for i in reversed(range(len(word)))]


def all_substrings(word):
    """
    >>> all_substrings('hel')
    [['h', 'he', 'hel'], ['e', 'el'], ['l']]
    """
    all_subs = []
    for i in range(len(word)):
        all_subs += substrings(word[i:])
    return set(all_subs)


def minion(word):
    stuart = 0
    kevin = 0
    consonants = 'bcdfghjklmnpqrstvwxyz' + 'bcdfghjklmnpqrstvwxyz'.upper()
    vowels = 'aeiou' + 'aeiou'.upper()

    for string in all_substrings(word):
        if string[0] in consonants:
            stuart += match(word, string)

        elif string[0] in vowels:
            kevin += match(word, string)

    if stuart > kevin:
        return 'Stuart {}'.format(stuart)
    elif stuart < kevin:
        return 'Kevin {}'.format(kevin)
    else:
        return 'Draw'


print(minion(input()))
