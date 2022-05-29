#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    elevation = 0
    num_valleys = 0
    in_valley = False

    for direction in path:
        if direction == 'U':
            elevation += 1
        else:
            elevation -= 1


        if not in_valley and elevation < 0:
            in_valley = True
            num_valleys += 1
        elif in_valley and elevation >= 0:
            in_valley = False

    return num_valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
