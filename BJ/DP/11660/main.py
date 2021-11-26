import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*(n+1) for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, n+1):
        d[x][y] = s[x-1][y-1] + d[x-1][y] + d[x][y-1] - d[x-1][y-1]

for _ in range(m):
    i = list(map(int, input().split()))
    x1, y1, x2, y2 = i[0], i[1], i[2], i[3]
    r = d[x2][y2] - d[x2][y1-1] - d[x1-1][y2] + d[x1-1][y1-1]
    print(r)