"""

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems.
The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus

"""


def plusMinus(arr):
    # Write your code here
    arr_len = len(arr)
    positive = []
    negative = []
    zero = []
    for i in range(arr_len):
        if arr[i] > 0:
            positive.append(arr[i])
        if arr[i] < 0:
            negative.append(arr[i])
        if arr[i] == 0:
            zero.append(arr[i])

        i += 1
    len_positive = len(positive)
    len_negative = len(negative)
    len_zero = len(zero)

    fraction_positive = f"{(len_positive / arr_len):.6f}"
    fraction_negative = f"{(len_negative / arr_len):.6f}"
    fraction_zero = f"{(len_zero / arr_len):.6f}"
    print(fraction_positive)
    print(fraction_negative)
    print(fraction_zero)


plusMinus([3, -4, 0, 8, -9, 2, 4, 6, 7, 8, 0, -2, 7, 0, 7, 10, 0, 8, -5])
