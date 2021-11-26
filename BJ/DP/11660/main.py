import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if x-1 >= 0:
            d[x][y] += d[x-1][y]
        if y-1 >= 0:
            d[x][y] += d[x][y-1]
        if x-1 >= 0 and y-1 >= 0:
            d[x][y] -= d[x-1][y-1]
        d[x][y] += s[x][y]

for _ in range(m):
    i = list(map(int, input().split()))
    x1, y1, x2, y2 = i[0]-1, i[1]-1, i[2]-1, i[3]-1
    r = d[x2][y2]

    if y1-1 >= 0:
        r -= d[x2][y1-1]
    if x1-1 >= 0:
        r -= d[x1-1][y2]
    if x1-1 >= 0 and y1-1 >= 0:
        r += d[x1-1][y1-1]

    print(r)