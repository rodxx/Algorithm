import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [[0]*(m+1)]+[[0]+list(map(int, input().split())) for _ in range(n)]
for x in range(1, n+1):
    for y in range(1, m+1):
        s[x][y] += max(s[x-1][y], s[x][y-1])
print(s[n][m])