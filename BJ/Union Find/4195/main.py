import sys
input = sys.stdin.readline

def parent(x):
    if p[x] != x:
        p[x] = parent(p[x])
    return p[x]

def union(x, y):
    px = parent(x)
    py = parent(y)
    if px != py:
        p[py] = px
        c[px] += c[py]

for _ in range(int(input())):
    n = int(input())
    p, c = {}, {}
    for _ in range(n):
        f1, f2 = input().split()
        if f1 not in p.keys():
            p[f1] = f1
            c[f1] = 1
        if f2 not in p.keys():
            p[f2] = f2
            c[f2] = 1
        union(f1, f2)
        print(c[parent(f1)])