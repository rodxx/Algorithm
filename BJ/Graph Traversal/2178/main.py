import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, d):
    queue = deque()
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    queue.append((0,0))
    d[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if x+dx[i] > n-1 or x+dx[i] < 0 or y+dy[i] > m-1 or y+dy[i] < 0:
                continue
            if g[x+dx[i]][y+dy[i]] == 1 and d[x+dx[i]][y+dy[i]] == 0:
                queue.append((x+dx[i],y+dy[i]))
                d[x+dx[i]][y+dy[i]] = d[x][y] + 1

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
distance = [[0]*m for _ in range(n)]
bfs(maze, distance)
print(distance[n-1][m-1])