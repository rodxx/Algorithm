import sys
input = sys.stdin.readline

n = int(input())
s = [[0, 0]] + [([0] + list(map(int, input().split())) + [0]) for _ in range(n)]
d = [[0]*(i+2) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i+1):
        d[i][j] = s[i][j] + max(d[i-1][j], d[i-1][j-1])
print(max(d[n]))