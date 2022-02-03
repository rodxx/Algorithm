import sys
from collections import deque
input = sys.stdin.readline


def tornado(a, b, d):

    k = s[a][b]
    sx, nx = dx[d], dx[d-1]
    sy, ny = dy[d], dy[d-1]
    ndx = [sx, nx, -nx, sx+nx, sx-nx, -sx+nx, -sx-nx]
    ndy = [sy, ny, -ny, sy+ny, sy-ny, -sy+ny, -sy-ny]
    dk = [[0, 0.05], [0.07, 0.02], [0.07, 0.02], [0.1, 0], [0.1, 0], [0.01, 0], [0.01, 0]]
    cnt = 0
    res = 0

    multi = 2
    for i in range(7):
        if i > 2:
            multi = 1
        for j in range(multi):
            na, nb = a + (j+1)*ndx[i], b + (j+1)*ndy[i]
            send = int(k * dk[i][j])
            res += send
            if na < 0 or na >= n or nb < 0 or nb >= n:
                cnt += send
                continue
            s[na][nb] += send

    if a+sx < 0 or a+sx >= n or b+sy < 0 or b+sy >= n:
        cnt += k - res
    else:
        s[a+sx][b+sy] += (k - res)

    s[a][b] = 0
    return cnt


dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
x, y = n//2, n//2
step, r = 1, 0

while True:

    for i in range(4):
        if i == 2:
            step += 1

        for _ in range(step):
            if x == 0 and y == 0:
                print(r)
                exit()
            x += dx[i]
            y += dy[i]
            r += tornado(x, y, i)

    step += 1
