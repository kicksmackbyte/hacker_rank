#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    broken_minimum = 0
    broken_maximum = 0

    minimum = scores[0]
    maximum = scores[0]

    for score in scores[1:]:

        if score < minimum:
            broken_minimum += 1
            minimum = score

        elif score > maximum:
            broken_maximum += 1
            maximum = score

    return broken_maximum, broken_minimum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

