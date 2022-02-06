import sys
import pprint
input = sys.stdin.readline

def move(d, dis, cl, v):
    for i in cl:

        i[0] = (i[0] + dis * dx[d]) % n
        i[1] = (i[1] + dis * dy[d]) % n

        if i[0] < 0:
            i[0] += n
        if i[1] < 0:
            i[1] += n

        v[i[0]][i[1]] = False
        s[i[0]][i[1]] += 1

def bug(cl):
    ndx, ndy = [-1, 1, -1, 1], [1, 1, -1, -1]
    for x, y in cl:
        cnt = 0
        for i in range(4):
            nx, ny = x + ndx[i], y + ndy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            if s[nx][ny] > 0:
                cnt += 1
        s[x][y] += cnt

def cloud(v):
    r = []
    for i in range(n):
        for j in range(n):
            if s[i][j] >= 2 and v[i][j]:
                r.append([i, j])
                s[i][j] -= 2
    return r

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
c = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

for _ in range(m):
    visit = [[True] * n for _ in range(n)]
    di, si = map(int, input().split())
    move(di-1, si, c, visit)
    bug(c)
    c = cloud(visit)
print(sum([sum(i) for i in s]))
