import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = [[0]*(m+1)] + [([0] + list(map(int, input().split()))) for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] += max(d[i-1][j], d[i][j-1], d[i-1][j-1])
print(d[n][m])