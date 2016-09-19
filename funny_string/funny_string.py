"""
Suppose you have some string S having length N that is indexed from 0 to N−1.
You also have some string R that is the reverse of string S.
S is funny if the condition | S[j]−S[j−1] |=| R[j]−R[j−1] | is true for every j from 1 to N−1.

Note: For some string S, S[j] denotes the ASCII value of the jth zero-indexed character in S.
The absolute value of some integer x is written as | x |.

Input Format

The first line contains an integer, T (the number of test cases).
The T subsequent lines each contain a string, where the ith line is string Si.

Constraints
1≤T≤10
0≤i≤T−1
2≤length of Si≤10000

Output Format
For each Si, print Funny or Not Funny on a new line.
"""
from math import fabs


T = input()

def funny_or_not(string, string_reverse):
    result_of_s = []
    result_of_r = []
    for idx, letter in enumerate(string[1:]):
        result_of_s.append(fabs(ord(letter) - ord(string[idx])))

    for idx, letter in enumerate(string_reverse[1:]):
        result_of_r.append(fabs(ord(letter) - ord(string_reverse[idx])))

    if result_of_r == result_of_s:
        return "Funny"
    return "Not Funny"

