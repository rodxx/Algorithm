import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [1,0,-1,0], [0,1,0,-1]


def rotate(x, y, d):
    s = [r[y:y+d] for r in a[x:x+d]]

    t = []
    for i in list(zip(*s)):
        t.append(list(i)[::-1])

    return t


def melting(s):
    queue = []
    for i in range(2**n):
        for j in range(2**n):

            if s[i][j] == 0:
                continue

            cnt = 0
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if nx < 0 or nx >= 2**n or ny < 0 or ny >= 2**n:
                    continue

                if s[nx][ny] > 0:
                    cnt += 1

            if cnt < 3:
                queue.append((i, j))

    while queue:
        i, j = queue.pop()
        s[i][j] -= 1


def bfs(x, y, s):
    queue = deque([(x, y)])

    r = s[x][y]
    cnt = 1
    s[x][y] = 0

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]

            if nx < 0 or nx >= 2 ** n or ny < 0 or ny >= 2 ** n:
                continue

            if s[nx][ny] > 0:
                r += s[nx][ny]
                s[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))

    return r, cnt


n, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(2**n)]
L = list(map(int, input().split()))
x, y = 0, 0

for l in L:
    A = []
    for i in range(2**(n-l)):
        na = [[] for _ in range(2 ** l)]
        for j in range(2**(n-l)):
            px, py = x + i*2**l, y + j*2**l

            t = rotate(px, py, 2**l)

            for k in range(2**l):
                na[k] += t[k]
        A += na

    melting(A)
    a = A

ice, count = 0, 0
for i in range(2**n):
    for j in range(2**n):
        if a[i][j] > 0:
            re, c = bfs(i, j, a)
            ice += re
            count = max(count, c)

print(ice, count, sep='\n')