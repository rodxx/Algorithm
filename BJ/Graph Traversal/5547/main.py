import sys
from collections import deque
input = sys.stdin.readline

def bfs(g,v,a,b,k):
    dx = [[0, 0, 1, -1, -1, 1], [0, 0, 1, -1, -1, 1]]
    dy = [[1, -1, 0, 1, 0, 1], [1, -1, -1, 0, -1, 0]]
    r, hole = 0, 0
    queue = deque()

    queue.append((a,b))
    v[a][b] = True
    while queue:
        x, y = queue.popleft()
        cnt, d = 0, 0
        if x % 2 != 0:
            d = 1
        for i in range(6):
            px, py = x+dx[d][i], y+dy[d][i]
            if px > h-1 or px < 0 or py > w-1 or py < 0:
                continue
            if k == 0 and g[px][py] == 1:
                hole += 1
            if g[px][py] == k:
                cnt += 1
                if not v[px][py]:
                    v[px][py] = True
                    queue.append((px, py))
        r += (6-cnt)
    if k == 1 or (k == 0 and r == hole):
        return r
    return 0



w, h = map(int, input().split())
octagon = [list(map(int, input().split())) for _ in range(h)]
visited = [[False]*w for _ in range(h)]
result, unseen = 0, 0
for i in range(h):
    for j in range(w):
        if not visited[i][j]:
            k = bfs(octagon, visited, i, j, octagon[i][j])
            if not octagon[i][j] and k > 0:
                k *= -1
            result += k
print(result)