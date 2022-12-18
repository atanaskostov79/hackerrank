import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

pattern = r"(?<=\w)([^\w\d]+)(?=\w)"
matrix = list(zip(*matrix))
s = ""
for words in matrix:
    s += ("".join(words))

print(re.sub(pattern, ' ', s))