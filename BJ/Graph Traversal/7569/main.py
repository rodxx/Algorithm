import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, l):
    queue = deque(l)
    dx = [0,1,0,-1,0,0]
    dy = [1,0,-1,0,0,0]
    dz = [0,0,0,0,1,-1]
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            if x+dx[i] > n-1 or x+dx[i] < 0 or y+dy[i] > m-1 or y+dy[i] < 0 or z+dz[i] < 0 or z+dz[i] > h-1:
                continue
            if g[z+dz[i]][x+dx[i]][y+dy[i]] == 0:
                queue.append((x+dx[i],y+dy[i],z+dz[i]))
                g[z+dz[i]][x+dx[i]][y+dy[i]] = g[z][x][y] + 1

m, n, h = map(int, input().split())
store, rtmt = [[] for _ in range(h)], []
tomato = [0,0]

for k in range(h):
    for i in range(n):
        store[k].append(list(map(int, input().split())))
        for j in range(m):
            if store[k][i][j] < 0:
                continue
            if store[k][i][j] == 1:
                rtmt.append((i,j,k))
            tomato[store[k][i][j]] += 1

if tomato[1] == 0:
    print(-1)
elif tomato[0] == 0:
    print(0)
else:
    bfs(store,rtmt)
    cnt = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if store[k][i][j] == 0:
                    print(-1)
                    exit(0)
                if cnt < store[k][i][j]:
                    cnt = store[k][i][j]
    print(cnt-1)