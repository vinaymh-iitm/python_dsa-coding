"""

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of
the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long
integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of elements.

"""


def miniMaxSum(arr):
    # Write your code here
    n = len(arr)
    print(n)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

    i = 0
    min_sum = arr[i] + arr[i+1] + arr[i+2] + arr[i+3]
    max_sum = arr[i-1] + arr[i-2] + arr[i-3] + arr[i-4]
    print(f"{min_sum} {max_sum}")


miniMaxSum([9, 8, 5, 4, 3, 7, 6, 1])
