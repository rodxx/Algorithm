import sys
input = sys.stdin.readline

n = int(input())
v = []
d = [0]*(n+1)
d[0], d[1] = 1, 1

for i in range(int(input())):
    k = int(input())
    v.append(k)
    v.append(k+1)

for i in range(2, n+1):
    if i in v:
        d[i] = d[i-1]
    else:
        d[i] = d[i-1] + d[i-2]
print(d[n])