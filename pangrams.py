"""
A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

Example

The string contains all letters in the English alphabet, so return pangram.

Function Description

Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

pangrams has the following parameter(s):

string s: a string to test
Returns

string: either pangram or not pangram
"""


def pangrams(s):
    # Write your code here
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    lowers_s = str.lower(s)
    print(lowers_s)
    for char in alphabets:
        if char not in str.lower(s):
            return "not pangram"
    return "pangram"

print(pangrams("The quick brown fox jumps over the lazy dog"))
