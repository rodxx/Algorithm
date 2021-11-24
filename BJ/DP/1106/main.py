import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(x):
    if x <= 0:
        return 0

    if d[x] > 0:
        return d[x]

    d[x] = 100000
    for i in range(n):
        d[x] = min(d[x], sol(x-city[i][1]) + city[i][0])
    return d[x]

c, n = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
d = [-1]*(c+1)
print(sol(c))