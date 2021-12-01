import sys
input = sys.stdin.readline

n, h = map(int, input().split())
s, e = min(n, h), max(n, h)
d = [[0]*(e+1) for _ in range(e+1)]
d[s][s] = 1
for x in range(s+1, e+1):
    for y in range(s, x+1):
        if y == s:
            d[x][y] = d[x-1][y]
        else:
            d[x][y] = d[x-1][y] + d[x][y-1]
print(d[e][e])