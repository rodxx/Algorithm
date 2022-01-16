import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, b, visit , v):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    queue = deque()

    queue.append(v)
    visit[v[0]][v[1]] = True
    while queue:
        x, y = queue.popleft()
        b[x][y] = '.'
        for i in range(4):
            if x+dx[i] > r-1 or x+dx[i] < 0 or y+dy[i] > c-1 or y+dy[i] < 0:
                continue
            if g[x+dx[i]][y+dy[i]] == 'O' and not visit[x+dx[i]][y+dy[i]]:
                queue.append((x+dx[i], y+dy[i]))
                visit[x+dx[i]][y+dy[i]] = True
            b[x+dx[i]][y+dy[i]] = '.'

r, c, n = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(r)]
bomb, visited, result = [], [], []

if n > 1:
    for _ in range(2):
        bomb = [['O'] * c for _ in range(r)]
        visited = [[False] * c for _ in range(r)]
        if n % 2 == 0:
            grid = bomb
            break

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O' and not visited[i][j]:
                    bfs(grid, bomb, visited, (i,j))
        grid = bomb
        if (n+1) % 4 == 0:
            break

for i in range(r):
    print(''.join(grid[i]))