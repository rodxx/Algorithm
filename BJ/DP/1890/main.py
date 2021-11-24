import sys
input = sys.stdin.readline

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0] = 1
for x in range(n):
    for y in range(n):
        if d[x][y] > 0 and m[x][y] != 0:
            dx, dy = [m[x][y], 0], [0, m[x][y]]
            for i in range(2):
                nx, ny = x + dx[i], y + dy[i]
                if nx > n-1 or ny > n-1:
                    continue
                d[nx][ny] += d[x][y]
print(d[n-1][n-1])