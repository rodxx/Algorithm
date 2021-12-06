import sys
input = sys.stdin.readline

n = int(input())
s = [[0]*3] + [list(map(int, input().split())) for _ in range(n)]
d = [[0]*3 for _ in range(n+1)]
for i in range(1, n+1):
    d[i][0] = s[i][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = s[i][1] + min(d[i-1][0], d[i-1][2])
    d[i][2] = s[i][2] + min(d[i-1][0], d[i-1][1])
print(min(d[n]))