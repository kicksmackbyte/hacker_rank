#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    return 1 if n == 1 else n*extraLongFactorials(n-1)

if __name__ == '__main__':
    fact = extraLongFactorials(100)
    print(fact)
