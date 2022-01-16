import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(l,w,v):
    queue = deque(v)
    visit = [[False]*m for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for x, y in w:
        l[x][y] = 1

    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            px, py = x+dx[i], y+dy[i]
            if px < 0 or px > n-1 or py < 0 or py > m-1:
                continue
            if l[px][py] == 0 and not visit[px][py]:
                queue.append((px, py))
                visit[px][py] = True
                cnt += 1
    return cnt


n, m = map(int, input().split())
lab, virus, space, c = [], [], [], 0
for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(m):
        if lab[i][j] == 2:
            virus.append((i,j))
            continue
        elif lab[i][j] == 0:
            space.append((i,j))

com = combinations(space,3)
min_c = 64
for i in com:
    c = bfs(copy.deepcopy(lab), i, virus)
    if min_c > c:
        min_c = c

print(len(space)-3-min_c)