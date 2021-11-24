import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
d = [0]*n
c, p = 0, 0

for i in range(n):
    if s[i] % 2 == 0:
        d[i] = d[i-1]+1
        continue
    c += 1
    e = 0
    while c > k:
        if s[p] % 2 == 0:
            e += 1
        else:
            c -= 1
        p += 1
    d[i] = d[i-1] - e
print(max(d))