#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    [print(f"{g % 5} {g} {g + (5 - g % 5)}") for g in grades]

    return [g if g < 38 or g % 5 < 3 else g + (5 - g % 5) for g in grades]

if __name__ == '__main__':
    fptr = open("out.txt", 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
