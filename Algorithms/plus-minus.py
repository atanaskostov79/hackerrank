#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count_plus = 0
    count_minus = 0
    count_zero = 0

    for a in arr:
        if a > 0:
            count_plus += 1
        elif a < 0:
            count_minus +=1
        else:
            count_zero += 1

    print(f"{count_plus/len(arr):.6f}")
    print(f"{count_minus/len(arr):.6f}")
    print(f"{count_zero/len(arr):.6f}")





if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

"""
6
-4 3 -9 0 4 1 
"""