#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    lr = 0
    rl = 0
    l = len(arr)
    for i in range(l):
        lr += arr[i][i]
        rl += arr[i][l-i -1]
    return abs(lr - rl)


if __name__ == '__main__':
    fptr = open('junk.txt', 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
