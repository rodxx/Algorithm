import sys
input = sys.stdin.readline

n = int(input())
d = [[0]*10 for _ in range(n+1)]
d[1] = [1]*10
for i in range(2, n+1):
    d[i][0] = d[i-1][0]
    for j in range(1, 10):
        d[i][j] = d[i][j-1]+d[i-1][j]
print(sum(d[n]) % 10007)