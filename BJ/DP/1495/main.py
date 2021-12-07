import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(i, c):
    if i == n:
        return c

    if d[i][c] >= -1:
        return d[i][c]

    d[i][c] = -1
    if c+v[i] <= m:
        d[i][c] = max(d[i][c], sol(i+1, c+v[i]))
    if c-v[i] >= 0:
        d[i][c] = max(d[i][c], sol(i+1, c-v[i]))

    return d[i][c]

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
d = [[-2]*1001 for _ in range(50)]
print(sol(0, s))