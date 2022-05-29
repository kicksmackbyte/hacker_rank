#!/bin/python3

import math
import os
import random
import re
import sys


def permuations(xs):
    if len(xs) <= 1:
        yield xs
    else:
        for x in permuations(xs[1:]):
            for i in range(len(xs)):
                yield x[:i] + xs[0:1] + x[i:]


def is_magic(square):
    totals = []
    totals.append(sum(square[0]))
    totals.append(sum(square[1]))
    totals.append(sum(square[2]))

    totals.append(square[0][0] + square[1][0] + square[2][0])
    totals.append(square[0][1] + square[1][1] + square[2][1])
    totals.append(square[0][2] + square[1][2] + square[2][2])

    totals.append(square[0][0] + square[1][1] + square[2][2])
    totals.append(square[0][2] + square[1][1] + square[2][0])

    for total in totals:
        if total != 15:
            return False

    return True


def all_squares():
    squares = []
    all_permutations = permuations(list(range(1, 10)))

    for permutation in all_permutations:
        square = [permutation[0:3], permutation[3:6], permutation[6:9]]
        if is_magic(square):
            yield square


def calculate_cost(square_a, square_b):
    cost = 0
    for row_a, row_b in zip(square_a, square_b):
        for cell_a, cell_b in zip(row_a, row_b):
            cost += abs(cell_a-cell_b)

    return cost


def formingMagicSquare(s):
    #1. Generate all possible magic squares
    magic_squares = all_squares()

    #2. Calculate all square diffs
    costs = [calculate_cost(s, square) for square in magic_squares]

    #3. Return min
    return min(costs)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #for _ in range(3):
    #    s.append(list(map(int, input().rstrip().split())))

    s = [[2, 9, 8], [4, 2, 7], [5, 6, 7]]
    result = formingMagicSquare(s)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
