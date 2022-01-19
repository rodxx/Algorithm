import sys
input = sys.stdin.readline

def parent(i):
    if p[i] != i:
        p[i] = parent(p[i])
    return p[i]

def union(x, y):
    px = parent(x)
    py = parent(y)

    if px > py:
        p[px] = py
    else:
        p[py] = px

n, m = map(int, input().split())
q = []
p = list(range(n+1))
g = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    q.append((0, a, b))

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if i == j:
            continue
        d = ((g[i][0] - g[j][0])**2 + (g[i][1] - g[j][1])**2)**0.5
        q.append((d, i, j))
q.sort()

r = 0
for d, a, b in q:
    if parent(a) != parent(b):
        union(a, b)
        r += d

print("%.2f"%r)