from collections import deque
n = int(input())
d = deque()

for i in range(n):
    method = input().split()
    command = method[0]
    if command == "append":
        v = method[1]
        d.append(v)
    elif command == "appendleft":
        v = method[1]
        d.appendleft(v)
    elif command == "popleft":
        d.popleft()
    elif command == "pop":
        d.pop()

print(" ".join(d))