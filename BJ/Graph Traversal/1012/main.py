import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(v, i, j):
    q = deque([(i, j)])
    v[i][j] = 2

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if v[nx][ny] == 1:
                q.append((nx, ny))
                v[nx][ny] = 2

for _ in range(int(input())):
    c, r, k = map(int, input().split())
    m = [[0]*c for _ in range(r)]
    cnt = 0
    for _ in range(k):
        b, a = map(int, input().split())
        m[a][b] = 1

    for i in range(r):
        for j in range(c):
            if m[i][j] == 1:
                bfs(m, i, j)
                cnt += 1

    print(cnt)