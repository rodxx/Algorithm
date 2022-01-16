import sys
from collections import deque
input = sys.stdin.readline

def bfs(g,visit,a,b):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    u = [(a,b)]
    queue = deque([(a,b)])
    p = g[a][b]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            px, py = x+dx[i], y+dy[i]
            if px < 0 or px > n-1 or py < 0 or py > n-1:
                continue
            if l <= abs(g[x][y] - g[px][py]) <= r and not visit[px][py]:
                queue.append((px, py))
                u.append((px, py))
                visit[px][py] = True
                p += g[px][py]
    return p, u

n, l, r = map(int, input().split())
nation = [list(map(int, input().split())) for _ in range(n)]
union_cnt, cnt, people, union = 0, 0, 0, []

while union_cnt != n*n:
    visited = [[False]*n for _ in range(n)]
    union_cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                people, union = bfs(nation,visited,i,j)
                union_cnt += 1
                for x, y in union:
                    nation[x][y] = int(people/len(union))
    cnt += 1
print(cnt-1)