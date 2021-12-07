import sys
input = sys.stdin.readline

def sol(s, e, v):
    d = [[0] * (m + 1) for _ in range(n + 1)]
    sx, sy = s[0], s[1]
    ex, ey = e[0], e[1]
    d[sx][sy] = v

    for i in range(sx, ex+1):
        for j in range(sy, ey+1):
            d[i][j] += d[i-1][j] + d[i][j-1]

    return d[ex][ey]


n, m, k = map(int, input().split())
x, y = k//m+1, k % m
if y == 0:
    x -= 1
    y = m

if k > 0:
    print(sol((x, y), (n, m), (sol((1, 1), (x, y), 1))))
else:
    print(sol((1, 1), (n, m), 1))
