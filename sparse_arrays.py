"""

There is a collection of input strings and a collection of query strings.
For each query string, determine how many times it occurs in the list of input strings.
Return an array of the results.

"""


def matchingStrings(strings, queries):
    # Write your code here
    result = []
    for query in queries:
        result.append(strings.count(query))
    return result


print(matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))
