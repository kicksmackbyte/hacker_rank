#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    count = defaultdict(lambda: 0)

    for bird in arr:
        count[bird] += 1

    max_bird = max(count, key=count.get)
    value = count[max_bird]

    for bird in count:
        if bird < max_bird and count[bird] == value:
            max_bird = bird

    return max_bird


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

