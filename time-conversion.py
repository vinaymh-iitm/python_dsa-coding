"""

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time
in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input

07:05:45PM
Sample Output

19:05:45

"""


def timeConversion(s):
    # Write your code here
    period = s[-2:]
    time = s[:-2]
    print(period)
    print(time)
    hours, minutes, seconds = time.split(":")
    print(hours)

    if period == "AM":
        if hours == "12":
            hours = "00"
    else:
        if hours != "12":
            hours = str(int(hours) + 12)

    return f"{hours}:{minutes}:{seconds}"


print(timeConversion("07:05:45PM"))