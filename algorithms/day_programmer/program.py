#!/bin/python3

import math
import os
import random
import re
import sys


def _is_leap_year(year):
    if year < 1918:
        return (year % 4 == 0)
    else:
        return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))


def dayOfProgrammer(year):

    if year == 1918:
        return f'26.09.1918'
    else:
        return f'12.09.{year}' if _is_leap_year(year) else f'13.09.{year}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

