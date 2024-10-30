"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
"""


def diagonalDifference(arr):
    principal = 0
    secondary = 0
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                principal += arr[i][j]
            if (i + j) == (n - 1):
                secondary += arr[i][j]
    absolute_diff = abs(principal - secondary)

    return absolute_diff
