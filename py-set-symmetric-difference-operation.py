n = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))

print(len(s1.symmetric_difference(s2)))
