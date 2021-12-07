import sys
input = sys.stdin.readline

d = [[0]*(i+1) for i in range(1001)]
d[0][0] = 1
for i in range(1, 1001):
    for k in range(1, 4):
        if i-k >= 0:
            for j in range(i-k+1):
                d[i][j+1] += d[i-k][j]

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(d[n][m] % (10**9+9))