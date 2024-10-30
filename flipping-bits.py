"""You will be given a list of 32-bit unsigned integers. Flip all the bits ( and ) and return the result as an
unsigned integer.

Example

. We're working with 32 bits, so:



Return .

Function Description

Complete the flippingBits function in the editor below.

flippingBits has the following parameter(s):

int n: an integer
Returns

int: the unsigned decimal integer result
"""


def flippingBits(n):
    # Write your code here
    binary_32bit = format(n, '032b')
    print(binary_32bit)
    flip_string = ''
    binary_string = str(binary_32bit)
    print(binary_string)

    for i in binary_string:
        if i == '1':
            flip_string += '0'
        else:
            flip_string += "1"
    print(flip_string)
    # flip_int = int(flip_string)
    # print(flip_int)
    flip_string_reverse = flip_string[::-1]
    print(flip_string_reverse)

    decimal_number = 0
    for i in range(len(flip_string_reverse)):
        digit = int(flip_string_reverse[i])
        power = 2 ** i
        result = digit * power

        decimal_number += result
    return decimal_number



print(flippingBits(9))
