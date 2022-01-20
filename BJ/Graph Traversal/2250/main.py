import sys
input = sys.stdin.readline
from collections import deque

class Node:
    x, y = 0, 0
    lc, rc = 0, 0
    ln, rn = 0, 0
    p = 0

def dfs(i):
    lc, rc = 0, 0
    ln, rn = g[i].ln, g[i].rn
    if ln > 0:
        lc = dfs(ln)
    if rn > 0:
        rc = dfs(rn)

    g[i].lc = lc
    g[i].rc = rc

    return lc + rc + 1

def bfs(i):
    g[i].x, g[i].y = 1, 1 + g[i].lc
    q = deque([i])
    while q:
        k = q.popleft()
        l, r = g[k].ln, g[k].rn
        f[g[k].x].append(g[k].y)

        if l > 0:
            g[l].x = g[k].x + 1
            g[l].y = g[k].y - g[l].rc - 1
            q.append(l)
        if r > 0:
            g[r].x = g[k].x + 1
            g[r].y = g[k].y + g[r].lc + 1
            q.append(r)

def find_root(i):
    if g[i].p == 0:
        return i
    return find_root(g[i].p)

n = int(input())
g = dict([(i, Node()) for i in range(1, n + 1)])
f = [[] for _ in range(50)]
for i in range(n):
    x, y, z = map(int, input().split())
    if y > 0:
        g[x].ln = y
        g[y].p = x
    if z > 0:
        g[x].rn = z
        g[z].p = x

root = find_root(1)
dfs(root)
bfs(root)

mi, mv = 0, 0
for i in range(1, 50):

    if len(f[i]) == 0:
        break

    v = max(f[i]) - min(f[i]) + 1
    if mv < v:
        mv = v
        mi = i
print(mi, mv)