import sys
from collections import deque

input = sys.stdin.readline


def bfs(c, s, value, gram):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    gx, gy = 0, 0
    gf = 0
    v = [[False] * m for _ in range(n)]
    t = [[0] * m for _ in range(n)]

    a, b = s
    queue = deque([s])
    v[a][b], t[a][b] = True, value

    while queue:
        x, y = queue.popleft()
        if c[x][y] == 2:
            gx, gy = x, y
            gf = 1
        for i in range(4):
            px, py = x + dx[i], y + dy[i]
            if px < 0 or px > n - 1 or py < 0 or py > m - 1:
                continue
            if not v[px][py]:
                if c[px][py] != 1 or (c[px][py] == 1 and gram):
                    queue.append((px, py))
                    v[px][py] = True
                    t[px][py] = t[x][y] + 1
    return t[n - 1][m - 1], (gx, gy), t[gx][gy], gf


n, m, l = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
r1, gp, gv, gf = bfs(castle, (0, 0), 0, 0)
if gf:
    r2 = bfs(castle, gp, gv, 1)[0]
    if r1 > 0:
        r = min(r1, r2)
    else:
        r = r2
else:
    r = r1

if r > l or r == 0:
    r = 'Fail'
print(r)