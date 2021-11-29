import sys
input = sys.stdin.readline

n = int(input())
s = [[0]]+[list(map(int, input().split())) for _ in range(n)]
d = [0]*(n+2)

for i in range(n, 0, -1):
    ti, pi = s[i][0], s[i][1]
    if i+ti-1 <= n:
        d[i] += pi
        if i+ti <= n:
            d[i] += d[i+ti]
    d[i] = max(d[i], d[i+1])
print(d[1])