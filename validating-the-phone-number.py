import re
n = int(input())
pattern = r"^[789][\d]{9}$"
for i in range(n):
    s = input()
    match = re.match(pattern, s)
    if match:
        print("YES")
    else:
        print("NO")