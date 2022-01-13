import sys
input = sys.stdin.readline

def sol(i, w):

    if i == n+1:
        return 0

    if d[i][w] >= 0:
        return d[i][w]

    r1 = sol(i+1, w)
    r2 = 0
    if w - s[i][0] >= 0:
        r2 = s[i][1] + sol(i+1, w - s[i][0])

    d[i][w] = max(r1, r2)

    return d[i][w]

n, k = map(int, input().split())
s = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
d = [[-1]*(k+1) for _ in range(n+1)]
print(sol(1, k))