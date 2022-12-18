n = int(input())
d = {}
for i in range(n):
    product = input().split()
    name = " ".join(product[:-1])
    if name in d.keys():
        d[name] = int(d[name]) + int(product[-1])
    else:
        d[name] =  int(product[-1])

for di in d:
    print(f"{di} {d[di]}")
