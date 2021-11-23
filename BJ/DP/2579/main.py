import sys
input = sys.stdin.readline

n = int(input())
s = [0] + [int(input()) for _ in range(n)]
d = [0]*(n+1)
for i in range(1, n+1):
    if i <= 2:
        d[i] = s[i] + d[i-1]
        continue
    d[i] = max(d[i-3] + s[i-1], d[i-2]) + s[i]
print(d[n])