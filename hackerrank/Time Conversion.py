#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(time):
    #
    # Write your code here.
    #
    night = 0
    if 'PM' in time:
        night = 12

    time = time[:8].split(':')

    if time[0] == '12':
        time[0] = 0

    time[0] = str(int(time[0]) + night)

    newtime = str()
    for x in time:
        newtime += x + ':'

    if len(newtime) < 9:
        newtime = '0' + newtime

    return newtime[:8]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    time = input()

    result = timeConversion(time)

    f.write(result + '\n')

    f.close()
