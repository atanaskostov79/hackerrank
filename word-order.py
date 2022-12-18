n = int(input())
d = {}

for i in range(n):
    word = input()

    if word in d.keys():
        d[word] +=1
    else:
        d[word] = 1

print(len(d))

for k, v in d.items():
    print(v, end=" ")