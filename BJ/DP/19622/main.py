import sys
input = sys.stdin.readline

n = int(input())
s = [[0]] + [list(map(int, input().split())) for _ in range(n)]
d = [0]*(n+1)
d[1] = s[1][2]
for i in range(2, n+1):
    d[i] = max(d[i-2]+s[i][2], d[i-1])
print(d[n])