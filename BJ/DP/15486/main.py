import sys
input = sys.stdin.readline

n = int(input())
day = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]
d = [0]*(n+2)
for i in range(n, 0, -1):
    ti, pi = day[i][0], day[i][1]
    if i + ti <= n+1:
        d[i] = max(d[i+1], pi + d[i+ti])
    else:
        d[i] = d[i+1]
print(d[1])