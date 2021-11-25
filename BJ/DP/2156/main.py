import sys
input = sys.stdin.readline

n = int(input())
w = [0] + [int(input()) for _ in range(n)]
d = [0]*(n+1)
for i in range(1, n+1):
    if i < 3:
        d[i] = w[i] + w[i-1]
        continue
    d[i] = max(d[i-2] + w[i], w[i-1] + d[i-3] + w[i], d[i-1])
print(d[n])