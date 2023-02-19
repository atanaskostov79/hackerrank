#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
os.environ['OUTPUT_PATH'] = "junk.txt"
def getMoneySpent(keyboards, drives, b):
    total_sum = []
    for k in keyboards:
        for d in drives:
            if k + d <= b:
                total_sum.append(k+d)

    return max(total_sum) if total_sum else  -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
