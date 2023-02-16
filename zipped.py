from functools import reduce

matrix= []
cow, row = list(map(int, input().split()))

for m in range(row):
    matrix.append( list(map( float, input().split())))

zipped_matrix = list(zip(*matrix))
[print(f"{sum(x)/row:.1f}") for x in zipped_matrix]
