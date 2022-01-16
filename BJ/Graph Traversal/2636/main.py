import sys
from collections import deque
input = sys.stdin.readline

def bfs(p):
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    v = [[False] * m for _ in range(n)]
    cnt = 0
    queue = deque([(0,0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            px, py = x+dx[i], y+dy[i]
            if px < 0 or px > n-1 or py < 0 or py > m-1:
                continue
            if not v[px][py]:
                v[px][py] = True
                if p[px][py] == 0:
                    queue.append((px, py))
                else:
                    p[px][py] = 0
                    cnt += 1
    return cnt

n, m = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(n)]
cnt, hour, result = 0, 0, 0

for i in plate:
    cnt += i.count(1)

while cnt > 0:
    result = cnt
    cnt -= bfs(plate)
    hour += 1
print(hour, result, sep='\n')