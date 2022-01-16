import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, l):
    queue = deque(l)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if x+dx[i] > n-1 or x+dx[i] < 0 or y+dy[i] > m-1 or y+dy[i] < 0:
                continue
            if g[x+dx[i]][y+dy[i]] == 0:
                queue.append((x+dx[i],y+dy[i]))
                g[x+dx[i]][y+dy[i]] = g[x][y] + 1

m, n = map(int, input().split())
store, rtmt = [], []
tomato = [0,0]

for i in range(n):
    store.append(list(map(int, input().split())))
    for j in range(m):
        if store[i][j] < 0:
            continue
        if store[i][j] == 1:
            rtmt.append((i,j))
        tomato[store[i][j]] += 1

if tomato[1] == 0:
    print(-1)
elif tomato[0] == 0:
    print(0)
else:
    bfs(store,rtmt)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if store[i][j] == 0:
                print(-1)
                exit(0)
            if cnt < store[i][j]:
                cnt = store[i][j]
    print(cnt-1)