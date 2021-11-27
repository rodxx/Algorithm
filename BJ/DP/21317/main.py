import sys
input = sys.stdin.readline

def sol(r, j):
    if r == n:
        return 0

    if j and d[r][0] >= 0 and 0 <= d[r][1] < 10**5:
        return min(d[r][0], d[r][1])

    m1, m2 = 10**5, 10**5
    if r+1 <= n:
        m1 = min(m1, s[r][0] + sol(r+1, j))
    if r+2 <= n:
        m1 = min(m1, s[r][1] + sol(r+2, j))
    if r+3 <= n and j:
        m2 = min(m2, k + sol(r+3, j-1))

    d[r][0], d[r][1] = m1, m2
    return min(m1, m2)

n = int(input())
s = [[0]] + [list(map(int, input().split())) for _ in range(n-1)]
k = int(input())
d = [[-1, -1] for _ in range(n)]

print(sol(1, 1))