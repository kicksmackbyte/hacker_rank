#!/bin/python3

import math
import os
import random
import re
import sys



def all_squares():
    squares = []

    for i in range(10):
        for j in range(10):
            square = []
            nums = list(range(1, 10))
            for num in nums:
                square.append(num)

            squares.append([square[0:2], square[3:5], square[6:8]])

    return squares


def is_magic(square):
    totals = []
    totals.append(sum(square[0]))
    totals.append(sum(square[1]))
    totals.append(sum(square[2]))

    totals.append(square[0][0] + square[1][0] + square[2][0])
    totals.append(square[0][1] + square[1][1] + square[2][1])
    totals.append(square[0][2] + square[1][2] + square[2][2])

    for total in totals:
        if total != 15:
            return False

    return True


def calculate_cost(square_a, square_b):
    cost = 0
    for row_a, row_b in zip(square_a, square_b):
        for cell_a, cell_b in zip(row_a, row_b):
            cost += abs(cell_a-cell_b)

    return cost


def formingMagicSquare(s):
    #1. Generate all possible magic squares
    distinct_squares = all_squares()
    magic_squares = [square for square in distinct_squares if is_magic(square)]

    #2. Calculate all square diffs
    costs = [calculate_cost(s, square) for square in magic_squares]

    #3. Return min
    return min(costs)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = [[4, 5, 8], [2, 4, 1], [1, 9, 7]]

    #for _ in range(3):
    #    s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
