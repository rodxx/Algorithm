import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, d, a, b):
    queue = deque()
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    queue.append((a,b))
    d[a][b] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if x+dx[i] > n-1 or x+dx[i] < 0 or y+dy[i] > n-1 or y+dy[i] < 0:
                continue
            if g[x+dx[i]][y+dy[i]] == 1 and not d[x+dx[i]][y+dy[i]]:
                queue.append((x+dx[i],y+dy[i]))
                d[x+dx[i]][y+dy[i]] = True
                cnt += 1
    return cnt

n = int(input())
m = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
result = []
for x in range(n):
    for y in range(n):
        if m[x][y] and not visit[x][y]:
            result.append(bfs(m,visit,x,y))

print(len(result))
for i in sorted(result):
    print(i)